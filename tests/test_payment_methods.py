import pytest
from tests.base_test import BaseTest


class TestPaymentMethods(BaseTest):
    """Тесты для способов оплаты"""
    
    @pytest.mark.payment
    def test_card_payment_selection(self):
        """Тест: выбор оплаты банковской картой"""
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
        
        # Выбираем оплату картой
        self.order_page.select_payment_method("card")
        
        # Проверяем, что оплата картой выбрана
        assert self.order_page.card_payment.is_checked()
        assert not self.order_page.cash_payment.is_checked()
        assert not self.order_page.bank_transfer.is_checked()
    
    @pytest.mark.payment
    def test_cash_payment_selection(self):
        """Тест: выбор оплаты наличными"""
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
        
        # Выбираем курьерскую доставку (необходимо для оплаты наличными)
        self.order_page.select_delivery_method("courier")
        
        # Выбираем оплату наличными
        self.order_page.select_payment_method("cash")
        
        # Проверяем, что оплата наличными выбрана
        assert self.order_page.cash_payment.is_checked()
        assert not self.order_page.card_payment.is_checked()
        assert not self.order_page.bank_transfer.is_checked()
    
    @pytest.mark.payment
    def test_bank_transfer_payment_selection(self):
        """Тест: выбор оплаты банковским переводом"""
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
        
        # Выбираем оплату банковским переводом
        self.order_page.select_payment_method("bank")
        
        # Проверяем, что оплата банковским переводом выбрана
        assert self.order_page.bank_transfer.is_checked()
        assert not self.order_page.card_payment.is_checked()
        assert not self.order_page.cash_payment.is_checked()
    
    @pytest.mark.payment
    def test_payment_method_switching(self):
        """Тест: переключение между способами оплаты"""
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
        
        # Сначала выбираем оплату картой
        self.order_page.select_payment_method("card")
        assert self.order_page.card_payment.is_checked()
        
        # Переключаемся на оплату наличными
        self.order_page.select_payment_method("cash")
        assert self.order_page.cash_payment.is_checked()
        assert not self.order_page.card_payment.is_checked()
        
        # Переключаемся на банковский перевод
        self.order_page.select_payment_method("bank")
        assert self.order_page.bank_transfer.is_checked()
        assert not self.order_page.cash_payment.is_checked()
    
    @pytest.mark.payment
    def test_cash_payment_availability_with_delivery_methods(self):
        """Тест: доступность оплаты наличными в зависимости от способа доставки"""
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
        
        # Проверяем доступность оплаты наличными для курьерской доставки
        self.order_page.select_delivery_method("courier")
        assert self.order_page.cash_payment.is_enabled()
        
        # Проверяем недоступность оплаты наличными для самовывоза
        self.order_page.select_delivery_method("pickup")
        assert not self.order_page.cash_payment.is_enabled()
        
        # Проверяем недоступность оплаты наличными для доставки почтой
        self.order_page.select_delivery_method("post")
        assert not self.order_page.cash_payment.is_enabled()
    
    @pytest.mark.payment
    def test_payment_method_descriptions(self):
        """Тест: отображение описаний способов оплаты"""
        # Проверяем наличие описаний для каждого способа оплаты
        card_description = self.page.locator('text=Visa, MasterCard, МИР').first
        assert card_description.is_visible()
        
        cash_description = self.page.locator('text=Только для курьерской доставки').first
        assert cash_description.is_visible()
        
        bank_description = self.page.locator('text=Счет будет отправлен на email').first
        assert bank_description.is_visible()
    
    @pytest.mark.payment
    def test_payment_method_validation(self):
        """Тест: валидация выбора способа оплаты"""
        # Заполняем форму без выбора способа оплаты
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
        # Не выбираем способ оплаты
        
        # Пытаемся отправить форму
        self.order_page.submit_order()
        
        # Проверяем наличие ошибки валидации
        errors = self.order_page.get_validation_errors()
        payment_error = any("оплат" in error.lower() or "payment" in error.lower() for error in errors)
        assert payment_error, "Должна появиться ошибка валидации для невыбранного способа оплаты"
    
    @pytest.mark.payment
    def test_payment_method_with_additional_services(self):
        """Тест: работа способов оплаты с дополнительными услугами"""
        # Заполняем форму с дополнительными услугами
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
        
        # Добавляем дополнительные услуги
        self.order_page.set_additional_options(
            gift_wrapping=True,
            insurance=True,
            newsletter=True
        )
        
        # Проверяем работу всех способов оплаты с дополнительными услугами
        self.order_page.select_payment_method("card")
        assert self.order_page.card_payment.is_checked()
        
        self.order_page.select_payment_method("cash")
        assert self.order_page.cash_payment.is_checked()
        
        self.order_page.select_payment_method("bank")
        assert self.order_page.bank_transfer.is_checked()
    
    @pytest.mark.payment
    def test_total_price_calculation_with_payment_methods(self):
        """Тест: расчет итоговой цены с разными способами оплаты"""
        # Заполняем форму
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
        
        # Проверяем, что итоговая цена одинакова для всех способов оплаты
        self.order_page.select_payment_method("card")
        card_total = self.order_page.get_total_price()
        
        self.order_page.select_payment_method("cash")
        cash_total = self.order_page.get_total_price()
        
        self.order_page.select_payment_method("bank")
        bank_total = self.order_page.get_total_price()
        
        # Итоговая цена должна быть одинаковой для всех способов оплаты
        assert card_total == cash_total == bank_total
