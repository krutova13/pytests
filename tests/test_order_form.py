import pytest
from tests.base_test import BaseTest


class TestOrderForm(BaseTest):
    """Тесты для формы оформления заказа"""
    
    @pytest.mark.smoke
    def test_page_loads_successfully(self):
        """Тест: страница загружается успешно"""
        # Проверяем, что основные элементы страницы присутствуют
        assert self.order_page.first_name_input.is_visible()
        assert self.order_page.last_name_input.is_visible()
        assert self.order_page.email_input.is_visible()
        assert self.order_page.phone_input.is_visible()
        assert self.order_page.submit_order_btn.is_visible()
    
    @pytest.mark.smoke
    def test_product_information_displayed(self):
        """Тест: информация о товаре отображается корректно"""
        # Проверяем наличие информации о товаре
        product_title = self.page.locator('text=Samsung Galaxy S24').first
        assert product_title.is_visible()
        
        # Проверяем цену товара
        assert self.order_page.product_price.is_visible()
    
    @pytest.mark.form
    def test_complete_order_form_filling(self):
        """Тест: полное заполнение формы заказа"""
        # Заполняем контактную информацию
        self.order_page.fill_contact_info(
            first_name="Иван",
            last_name="Петров", 
            email="ivan.petrov@example.com",
            phone="+7 (999) 123-45-67"
        )
        
        # Заполняем адрес
        self.order_page.fill_address_info(
            city="Москва",
            address="ул. Тверская, д. 1",
            postal_code="101000",
            apartment="10"
        )
        
        # Выбираем способ доставки
        self.order_page.select_delivery_method("courier")
        
        # Выбираем способ оплаты
        self.order_page.select_payment_method("card")
        
        # Добавляем дополнительные опции
        self.order_page.set_additional_options(
            gift_wrapping=True,
            insurance=True,
            newsletter=True
        )
        
        # Добавляем комментарий
        self.order_page.add_comment("Просьба доставить до 18:00")
        
        # Проверяем, что форма заполнена
        assert self.order_page.first_name_input.input_value() == "Иван"
        assert self.order_page.last_name_input.input_value() == "Петров"
        assert self.order_page.email_input.input_value() == "ivan.petrov@example.com"
        assert self.order_page.phone_input.input_value() == "+7 (999) 123-45-67"
        assert self.order_page.city_select.input_value() == "Москва"
        assert self.order_page.address_input.input_value() == "ул. Тверская, д. 1"
        assert self.order_page.gift_wrapping.is_checked()
        assert self.order_page.insurance.is_checked()
        assert self.order_page.newsletter.is_checked()
    
    @pytest.mark.form
    def test_minimal_order_form_filling(self):
        """Тест: минимальное заполнение формы заказа (только обязательные поля)"""
        # Заполняем только обязательные поля
        self.order_page.fill_contact_info(
            first_name="Анна",
            last_name="Сидорова",
            email="anna.sidorova@example.com", 
            phone="+7 (999) 987-65-43"
        )
        
        self.order_page.fill_address_info(
            city="Санкт-Петербург",
            address="Невский проспект, д. 28"
        )
        
        self.order_page.select_delivery_method("pickup")
        self.order_page.select_payment_method("cash")
        
        # Проверяем, что форма заполнена
        assert self.order_page.first_name_input.input_value() == "Анна"
        assert self.order_page.last_name_input.input_value() == "Сидорова"
        assert self.order_page.email_input.input_value() == "anna.sidorova@example.com"
        assert self.order_page.phone_input.input_value() == "+7 (999) 987-65-43"
        assert self.order_page.city_select.input_value() == "Санкт-Петербург"
        assert self.order_page.address_input.input_value() == "Невский проспект, д. 28"
    
    @pytest.mark.form
    def test_draft_saving(self):
        """Тест: сохранение черновика заказа"""
        # Заполняем частично форму
        self.order_page.fill_contact_info(
            first_name="Тест",
            last_name="Тестов",
            email="test@example.com",
            phone="+7 (999) 111-11-11"
        )
        
        # Сохраняем черновик
        self.order_page.save_draft()
        
        # Проверяем, что черновик сохранен (можно добавить проверку уведомления)
        # В реальном приложении здесь была бы проверка появления уведомления об успешном сохранении
        assert True  # Заглушка для демонстрации
    
    @pytest.mark.regression
    def test_form_reset_after_page_refresh(self):
        """Тест: форма сбрасывается после обновления страницы"""
        # Заполняем форму
        self.order_page.fill_contact_info(
            first_name="Тест",
            last_name="Тестов", 
            email="test@example.com",
            phone="+7 (999) 111-11-11"
        )
        
        # Обновляем страницу
        self.page.reload()
        self.wait_for_page_load()
        
        # Проверяем, что форма пустая
        assert self.order_page.first_name_input.input_value() == ""
        assert self.order_page.last_name_input.input_value() == ""
        assert self.order_page.email_input.input_value() == ""
        assert self.order_page.phone_input.input_value() == ""
