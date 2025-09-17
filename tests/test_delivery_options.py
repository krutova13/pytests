import pytest
from tests.base_test import BaseTest


class TestDeliveryOptions(BaseTest):
    """Тесты для способов доставки"""
    
    @pytest.mark.delivery
    def test_courier_delivery_selection(self):
        """Тест: выбор курьерской доставки"""
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
        
        # Выбираем курьерскую доставку
        self.order_page.select_delivery_method("courier")
        self.order_page.select_payment_method("card")
        
        # Проверяем, что курьерская доставка выбрана
        assert self.order_page.courier_delivery.is_checked()
        assert not self.order_page.pickup_delivery.is_checked()
        assert not self.order_page.post_delivery.is_checked()
    
    @pytest.mark.delivery
    def test_pickup_delivery_selection(self):
        """Тест: выбор самовывоза"""
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
        
        # Выбираем самовывоз
        self.order_page.select_delivery_method("pickup")
        self.order_page.select_payment_method("card")
        
        # Проверяем, что самовывоз выбран
        assert self.order_page.pickup_delivery.is_checked()
        assert not self.order_page.courier_delivery.is_checked()
        assert not self.order_page.post_delivery.is_checked()
    
    @pytest.mark.delivery
    def test_post_delivery_selection(self):
        """Тест: выбор доставки почтой России"""
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
        
        # Выбираем доставку почтой
        self.order_page.select_delivery_method("post")
        self.order_page.select_payment_method("card")
        
        # Проверяем, что доставка почтой выбрана
        assert self.order_page.post_delivery.is_checked()
        assert not self.order_page.courier_delivery.is_checked()
        assert not self.order_page.pickup_delivery.is_checked()
    
    @pytest.mark.delivery
    def test_delivery_method_switching(self):
        """Тест: переключение между способами доставки"""
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
        
        self.order_page.select_payment_method("card")
        
        # Сначала выбираем курьерскую доставку
        self.order_page.select_delivery_method("courier")
        assert self.order_page.courier_delivery.is_checked()
        
        # Переключаемся на самовывоз
        self.order_page.select_delivery_method("pickup")
        assert self.order_page.pickup_delivery.is_checked()
        assert not self.order_page.courier_delivery.is_checked()
        
        # Переключаемся на доставку почтой
        self.order_page.select_delivery_method("post")
        assert self.order_page.post_delivery.is_checked()
        assert not self.order_page.pickup_delivery.is_checked()
    
    @pytest.mark.delivery
    def test_delivery_price_calculation(self):
        """Тест: расчет стоимости доставки"""
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
        
        self.order_page.select_payment_method("card")
        
        # Проверяем стоимость для курьерской доставки (бесплатно)
        self.order_page.select_delivery_method("courier")
        delivery_price = self.order_page.delivery_price.text_content()
        assert "0" in delivery_price or "бесплатно" in delivery_price.lower()
        
        # Проверяем стоимость для самовывоза (бесплатно)
        self.order_page.select_delivery_method("pickup")
        delivery_price = self.order_page.delivery_price.text_content()
        assert "0" in delivery_price or "бесплатно" in delivery_price.lower()
        
        # Проверяем стоимость для доставки почтой (300 ₽)
        self.order_page.select_delivery_method("post")
        delivery_price = self.order_page.delivery_price.text_content()
        assert "300" in delivery_price
    
    @pytest.mark.delivery
    def test_delivery_time_display(self):
        """Тест: отображение времени доставки"""
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
        
        self.order_page.select_payment_method("card")
        
        # Проверяем отображение времени для разных способов доставки
        self.order_page.select_delivery_method("courier")
        # Ищем текст с временем доставки (1-2 дня)
        courier_text = self.page.locator('text=1-2 дня').first
        assert courier_text.is_visible()
        
        self.order_page.select_delivery_method("pickup")
        # Ищем текст с временем самовывоза (сегодня)
        pickup_text = self.page.locator('text=Сегодня').first
        assert pickup_text.is_visible()
        
        self.order_page.select_delivery_method("post")
        # Ищем текст с временем доставки почтой (3-7 дней)
        post_text = self.page.locator('text=3-7 дней').first
        assert post_text.is_visible()
    
    @pytest.mark.delivery
    def test_cash_payment_with_courier_delivery(self):
        """Тест: оплата наличными доступна только для курьерской доставки"""
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
        
        # Выбираем курьерскую доставку
        self.order_page.select_delivery_method("courier")
        
        # Проверяем, что оплата наличными доступна
        assert self.order_page.cash_payment.is_enabled()
        
        # Переключаемся на самовывоз
        self.order_page.select_delivery_method("pickup")
        
        # Проверяем, что оплата наличными недоступна
        assert not self.order_page.cash_payment.is_enabled()
        
        # Переключаемся на доставку почтой
        self.order_page.select_delivery_method("post")
        
        # Проверяем, что оплата наличными недоступна
        assert not self.order_page.cash_payment.is_enabled()
