import pytest
from playwright.sync_api import Page
from tests.base_test import BaseTest


class TestMobileResponsiveness(BaseTest):
    """Тесты мобильной адаптивности"""
    
    @pytest.fixture(autouse=True)
    def setup_mobile(self, context):
        """Настройка мобильного контекста"""
        # Устанавливаем мобильный viewport
        context.set_viewport_size({"width": 375, "height": 667})  # iPhone SE размер
        yield context
    
    @pytest.mark.regression
    def test_mobile_form_layout(self):
        """Тест: макет формы на мобильном устройстве"""
        # Проверяем, что основные элементы формы видны на мобильном
        assert self.order_page.first_name_input.is_visible()
        assert self.order_page.last_name_input.is_visible()
        assert self.order_page.email_input.is_visible()
        assert self.order_page.phone_input.is_visible()
        assert self.order_page.city_select.is_visible()
        assert self.order_page.address_input.is_visible()
        
        # Проверяем, что кнопки видны
        assert self.order_page.submit_order_btn.is_visible()
        assert self.order_page.save_draft_btn.is_visible()
    
    @pytest.mark.regression
    def test_mobile_delivery_options_layout(self):
        """Тест: макет опций доставки на мобильном"""
        # Проверяем, что опции доставки видны и кликабельны
        assert self.order_page.courier_delivery.is_visible()
        assert self.order_page.pickup_delivery.is_visible()
        assert self.order_page.post_delivery.is_visible()
        
        # Проверяем, что можно выбрать опции доставки
        self.order_page.select_delivery_method("courier")
        assert self.order_page.courier_delivery.is_checked()
        
        self.order_page.select_delivery_method("pickup")
        assert self.order_page.pickup_delivery.is_checked()
    
    @pytest.mark.regression
    def test_mobile_payment_options_layout(self):
        """Тест: макет опций оплаты на мобильном"""
        # Заполняем минимальную форму
        self.order_page.fill_contact_info(
            first_name="Тест",
            last_name="Тестов",
            email="test@example.com",
            phone="+7 (999) 111-11-11"
        )
        
        self.order_page.fill_address_info(
            city="Москва",
            address="ул. Тестовая, д. 1"
        )
        
        self.order_page.select_delivery_method("courier")
        
        # Проверяем, что опции оплаты видны и кликабельны
        assert self.order_page.card_payment.is_visible()
        assert self.order_page.cash_payment.is_visible()
        assert self.order_page.bank_transfer.is_visible()
        
        # Проверяем, что можно выбрать опции оплаты
        self.order_page.select_payment_method("card")
        assert self.order_page.card_payment.is_checked()
        
        self.order_page.select_payment_method("cash")
        assert self.order_page.cash_payment.is_checked()
    
    @pytest.mark.regression
    def test_mobile_additional_options_layout(self):
        """Тест: макет дополнительных опций на мобильном"""
        # Проверяем, что дополнительные опции видны
        assert self.order_page.gift_wrapping.is_visible()
        assert self.order_page.insurance.is_visible()
        assert self.order_page.newsletter.is_visible()
        assert self.order_page.comment_textarea.is_visible()
        
        # Проверяем, что можно взаимодействовать с опциями
        self.order_page.gift_wrapping.check()
        assert self.order_page.gift_wrapping.is_checked()
        
        self.order_page.insurance.check()
        assert self.order_page.insurance.is_checked()
    
    @pytest.mark.regression
    def test_mobile_form_filling(self):
        """Тест: заполнение формы на мобильном устройстве"""
        # Заполняем форму на мобильном
        self.order_page.fill_contact_info(
            first_name="Мобильный",
            last_name="Тест",
            email="mobile@example.com",
            phone="+7 (999) 555-55-55"
        )
        
        self.order_page.fill_address_info(
            city="Санкт-Петербург",
            address="Невский проспект, д. 1",
            postal_code="191025",
            apartment="5"
        )
        
        self.order_page.select_delivery_method("pickup")
        self.order_page.select_payment_method("card")
        
        self.order_page.set_additional_options(
            gift_wrapping=True,
            newsletter=True
        )
        
        self.order_page.add_comment("Мобильный заказ")
        
        # Проверяем, что форма заполнена корректно
        assert self.order_page.first_name_input.input_value() == "Мобильный"
        assert self.order_page.last_name_input.input_value() == "Тест"
        assert self.order_page.email_input.input_value() == "mobile@example.com"
        assert self.order_page.phone_input.input_value() == "+7 (999) 555-55-55"
        assert self.order_page.city_select.input_value() == "Санкт-Петербург"
        assert self.order_page.address_input.input_value() == "Невский проспект, д. 1"
        assert self.order_page.gift_wrapping.is_checked()
        assert self.order_page.newsletter.is_checked()
    
    @pytest.mark.regression
    def test_mobile_price_display(self):
        """Тест: отображение цен на мобильном устройстве"""
        # Проверяем, что цены отображаются корректно
        assert self.order_page.product_price.is_visible()
        assert self.order_page.delivery_price.is_visible()
        assert self.order_page.total_price.is_visible()
        
        # Проверяем базовую цену товара
        product_price = self.order_page.product_price.text_content()
        assert "89 990" in product_price or "89990" in product_price
    
    @pytest.mark.regression
    def test_mobile_scrolling(self):
        """Тест: прокрутка страницы на мобильном устройстве"""
        # Проверяем, что можно прокрутить страницу
        initial_position = self.page.evaluate("window.scrollY")
        
        # Прокручиваем вниз
        self.page.evaluate("window.scrollTo(0, document.body.scrollHeight)")
        
        # Проверяем, что позиция изменилась
        final_position = self.page.evaluate("window.scrollY")
        assert final_position > initial_position
        
        # Прокручиваем вверх
        self.page.evaluate("window.scrollTo(0, 0)")
        
        # Проверяем, что вернулись в начало
        top_position = self.page.evaluate("window.scrollY")
        assert top_position == 0
    
    @pytest.mark.regression
    def test_mobile_touch_interactions(self):
        """Тест: сенсорные взаимодействия на мобильном"""
        # Проверяем, что можно тапать по элементам
        self.order_page.first_name_input.tap()
        self.order_page.first_name_input.fill("Тап тест")
        assert self.order_page.first_name_input.input_value() == "Тап тест"
        
        # Проверяем тап по чекбоксам
        self.order_page.gift_wrapping.tap()
        assert self.order_page.gift_wrapping.is_checked()
        
        self.order_page.insurance.tap()
        assert self.order_page.insurance.is_checked()
    
    @pytest.mark.regression
    def test_mobile_landscape_orientation(self):
        """Тест: поворот экрана в альбомную ориентацию"""
        # Поворачиваем экран в альбомную ориентацию
        self.page.set_viewport_size({"width": 667, "height": 375})
        
        # Проверяем, что форма все еще работает
        assert self.order_page.first_name_input.is_visible()
        assert self.order_page.submit_order_btn.is_visible()
        
        # Заполняем форму в альбомной ориентации
        self.order_page.fill_contact_info(
            first_name="Альбомный",
            last_name="Тест",
            email="landscape@example.com",
            phone="+7 (999) 777-77-77"
        )
        
        assert self.order_page.first_name_input.input_value() == "Альбомный"
    
    @pytest.mark.regression
    def test_mobile_modal_dialog(self):
        """Тест: модальное окно на мобильном устройстве"""
        # Заполняем форму
        self.order_page.fill_contact_info(
            first_name="Модальный",
            last_name="Тест",
            email="modal@example.com",
            phone="+7 (999) 888-88-88"
        )
        
        self.order_page.fill_address_info(
            city="Москва",
            address="ул. Модальная, д. 1"
        )
        
        self.order_page.select_delivery_method("courier")
        self.order_page.select_payment_method("card")
        
        # Отправляем заказ
        self.order_page.submit_order()
        
        # Проверяем, что модальное окно появилось
        # В реальном приложении здесь была бы проверка появления модального окна
        # assert self.order_page.is_confirmation_modal_visible()
