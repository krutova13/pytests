"""
Конфигурация Playwright для тестов
"""
import os
from playwright.sync_api import sync_playwright


def get_browser_config():
    """Возвращает конфигурацию браузера"""
    return {
        "headless": os.getenv("HEADLESS", "true").lower() == "true",
        "slow_mo": int(os.getenv("SLOW_MO", "0")),
        "timeout": int(os.getenv("TIMEOUT", "30000")),
    }


def get_viewport_config():
    """Возвращает конфигурацию viewport"""
    return {
        "width": int(os.getenv("VIEWPORT_WIDTH", "1920")),
        "height": int(os.getenv("VIEWPORT_HEIGHT", "1080")),
    }


def get_mobile_viewport_config():
    """Возвращает конфигурацию мобильного viewport"""
    return {
        "width": int(os.getenv("MOBILE_WIDTH", "375")),
        "height": int(os.getenv("MOBILE_HEIGHT", "667")),
    }
