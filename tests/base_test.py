import pytest
from playwright.sync_api import Page
from pages.order_page import OrderPage


class BaseTest:
    """Базовый класс для всех тестов"""
    
    @pytest.fixture(autouse=True)
    def setup(self, order_page: Page):
        """Настройка для каждого теста"""
        self.page = order_page
        self.order_page = OrderPage(order_page)
    
    def take_screenshot(self, name: str) -> None:
        """Делает скриншот страницы"""
        self.page.screenshot(path=f"reports/screenshots/{name}.png")
    
    def wait_for_page_load(self) -> None:
        """Ждет полной загрузки страницы"""
        self.page.wait_for_load_state("networkidle")
