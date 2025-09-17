import pytest
from playwright.sync_api import sync_playwright, Browser, BrowserContext, Page
from typing import Generator
import os


@pytest.fixture(scope="session")
def browser() -> Generator[Browser, None, None]:
    """Фикстура для создания браузера"""
    with sync_playwright() as p:
        # Можно изменить браузер: chromium, firefox, webkit
        browser = p.chromium.launch(
            headless=os.getenv("HEADLESS", "true").lower() == "true",
            slow_mo=1000 if os.getenv("SLOW_MO") else 0
        )
        yield browser
        browser.close()


@pytest.fixture(scope="function")
def context(browser: Browser) -> Generator[BrowserContext, None, None]:
    """Фикстура для создания контекста браузера"""
    context = browser.new_context(
        viewport={"width": 1920, "height": 1080},
        user_agent="Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36"
    )
    yield context
    context.close()


@pytest.fixture(scope="function")
def page(context: BrowserContext) -> Generator[Page, None, None]:
    """Фикстура для создания страницы"""
    page = context.new_page()
    yield page
    page.close()


@pytest.fixture(scope="function")
def order_page(page: Page) -> Page:
    """Фикстура для загрузки страницы оформления заказа"""
    page.goto("https://qa-mts.netlify.app/")
    page.wait_for_load_state("networkidle")
    return page
