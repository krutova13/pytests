from playwright.sync_api import Page, Locator
from typing import Optional


class OrderPage:
    """Класс для работы со страницей оформления заказа"""
    
    def __init__(self, page: Page):
        self.page = page
        
        # Селекторы для полей формы (обновлены в соответствии с реальной структурой)
        self.first_name_input = page.locator('input[name="firstName"]')
        self.last_name_input = page.locator('input[name="lastName"]')
        self.email_input = page.locator('input[name="email"]')
        self.phone_input = page.locator('input[name="phone"]')
        
        # Селекторы для адреса
        self.city_select = page.locator('select[name="city"]')
        self.address_input = page.locator('textarea[name="address"]')
        self.postal_code_input = page.locator('input[name="postalCode"]')
        self.apartment_input = page.locator('input[name="apartment"]')
        
        # Селекторы для способа доставки (используем более точные селекторы)
        self.courier_delivery = page.locator('input[name="delivery"][value="courier"]')
        self.pickup_delivery = page.locator('input[name="delivery"][value="pickup"]')
        self.post_delivery = page.locator('input[name="delivery"][value="post"]')
        
        # Селекторы для способа оплаты (используем более точные селекторы)
        self.card_payment = page.locator('input[name="payment"][value="card"]')
        self.cash_payment = page.locator('input[name="payment"][value="cash"]')
        self.bank_transfer = page.locator('input[name="payment"][value="bank"]')
        
        # Дополнительные опции
        self.gift_wrapping = page.locator('input[name="giftWrap"]')
        self.insurance = page.locator('input[name="insurance"]')
        self.newsletter = page.locator('input[name="newsletter"]')
        
        # Комментарий
        self.comment_textarea = page.locator('textarea[name="comment"]')
        
        # Кнопки
        self.save_draft_btn = page.locator('button:has-text("Сохранить черновик")')
        self.submit_order_btn = page.locator('button[type="submit"]:has-text("Оформить заказ")')
        self.confirm_order_btn = page.locator('button:has-text("Подтвердить")')
        self.cancel_order_btn = page.locator('button:has-text("Отмена")')
        
        # Цены и итого (обновлены селекторы)
        self.product_price = page.locator('text=89 990 ₽').first
        self.delivery_price = page.locator('text=0 ₽').first
        self.additional_services_price = page.locator('text=0 ₽').first
        self.total_price = page.locator('text=89,990 ₽').first
        
        # Модальное окно подтверждения
        self.confirmation_modal = page.locator('h3:has-text("Подтверждение заказа")')
    
    def fill_contact_info(self, first_name: str, last_name: str, email: str, phone: str) -> None:
        """Заполняет контактную информацию"""
        self.first_name_input.fill(first_name)
        self.last_name_input.fill(last_name)
        self.email_input.fill(email)
        self.phone_input.fill(phone)
    
    def fill_address_info(self, city: str, address: str, postal_code: Optional[str] = None, 
                         apartment: Optional[str] = None) -> None:
        """Заполняет информацию об адресе"""
        self.city_select.select_option(city)
        self.address_input.fill(address)
        if postal_code:
            self.postal_code_input.fill(postal_code)
        if apartment:
            self.apartment_input.fill(apartment)
    
    def select_delivery_method(self, method: str) -> None:
        """Выбирает способ доставки"""
        if method == "courier":
            self.courier_delivery.check()
        elif method == "pickup":
            self.pickup_delivery.check()
        elif method == "post":
            self.post_delivery.check()
    
    def select_payment_method(self, method: str) -> None:
        """Выбирает способ оплаты"""
        if method == "card":
            self.card_payment.check()
        elif method == "cash":
            self.cash_payment.check()
        elif method == "bank":
            self.bank_transfer.check()
    
    def set_additional_options(self, gift_wrapping: bool = False, insurance: bool = False, 
                              newsletter: bool = False) -> None:
        """Устанавливает дополнительные опции"""
        if gift_wrapping:
            self.gift_wrapping.check()
        if insurance:
            self.insurance.check()
        if newsletter:
            self.newsletter.check()
    
    def add_comment(self, comment: str) -> None:
        """Добавляет комментарий к заказу"""
        self.comment_textarea.fill(comment)
    
    def submit_order(self) -> None:
        """Отправляет заказ"""
        self.submit_order_btn.click()
    
    def confirm_order(self) -> None:
        """Подтверждает заказ в модальном окне"""
        self.confirm_order_btn.click()
    
    def save_draft(self) -> None:
        """Сохраняет черновик заказа"""
        self.save_draft_btn.click()
    
    def get_total_price(self) -> str:
        """Получает итоговую цену"""
        return self.total_price.text_content()
    
    def is_confirmation_modal_visible(self) -> bool:
        """Проверяет, видно ли модальное окно подтверждения"""
        return self.confirmation_modal.is_visible()
    
    def get_validation_errors(self) -> list[str]:
        """Получает список ошибок валидации"""
        error_elements = self.page.locator('.error, .invalid, [class*="error"]')
        return [error.text_content() for error in error_elements.all() if error.text_content()]
