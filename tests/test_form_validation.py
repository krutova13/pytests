import pytest
from tests.base_test import BaseTest


class TestFormValidation(BaseTest):
    """Тесты валидации полей формы"""
    
    @pytest.mark.validation
    def test_required_fields_validation(self):
        """Тест: валидация обязательных полей"""
        # Пытаемся отправить пустую форму
        self.order_page.submit_order()
        
        # Проверяем, что появились ошибки валидации
        errors = self.order_page.get_validation_errors()
        assert len(errors) > 0, "Должны появиться ошибки валидации для обязательных полей"
    
    @pytest.mark.validation
    def test_email_validation(self):
        """Тест: валидация email адреса"""
        # Заполняем форму с невалидным email
        self.order_page.fill_contact_info(
            first_name="Тест",
            last_name="Тестов",
            email="invalid-email",
            phone="+7 (999) 111-11-11"
        )
        
        self.order_page.fill_address_info(
            city="Москва",
            address="ул. Тестовая, д. 1"
        )
        
        self.order_page.select_delivery_method("courier")
        self.order_page.select_payment_method("card")
        
        # Пытаемся отправить форму
        self.order_page.submit_order()
        
        # Проверяем наличие ошибки валидации email
        errors = self.order_page.get_validation_errors()
        email_error = any("email" in error.lower() or "почта" in error.lower() for error in errors)
        assert email_error, "Должна появиться ошибка валидации для невалидного email"
    
    @pytest.mark.validation
    def test_phone_validation(self):
        """Тест: валидация номера телефона"""
        # Заполняем форму с невалидным телефоном
        self.order_page.fill_contact_info(
            first_name="Тест",
            last_name="Тестов",
            email="test@example.com",
            phone="123"  # Невалидный номер
        )
        
        self.order_page.fill_address_info(
            city="Москва",
            address="ул. Тестовая, д. 1"
        )
        
        self.order_page.select_delivery_method("courier")
        self.order_page.select_payment_method("card")
        
        # Пытаемся отправить форму
        self.order_page.submit_order()
        
        # Проверяем наличие ошибки валидации телефона
        errors = self.order_page.get_validation_errors()
        phone_error = any("телефон" in error.lower() or "phone" in error.lower() for error in errors)
        assert phone_error, "Должна появиться ошибка валидации для невалидного телефона"
    
    @pytest.mark.validation
    def test_empty_required_fields(self):
        """Тест: проверка пустых обязательных полей"""
        # Заполняем только часть обязательных полей
        self.order_page.fill_contact_info(
            first_name="",  # Пустое имя
            last_name="Тестов",
            email="",  # Пустой email
            phone="+7 (999) 111-11-11"
        )
        
        self.order_page.fill_address_info(
            city="Москва",
            address=""  # Пустой адрес
        )
        
        self.order_page.select_delivery_method("courier")
        self.order_page.select_payment_method("card")
        
        # Пытаемся отправить форму
        self.order_page.submit_order()
        
        # Проверяем наличие ошибок для пустых полей
        errors = self.order_page.get_validation_errors()
        assert len(errors) > 0, "Должны появиться ошибки для пустых обязательных полей"
    
    @pytest.mark.validation
    def test_city_selection_required(self):
        """Тест: проверка обязательного выбора города"""
        # Заполняем форму без выбора города
        self.order_page.fill_contact_info(
            first_name="Тест",
            last_name="Тестов",
            email="test@example.com",
            phone="+7 (999) 111-11-11"
        )
        
        # Не выбираем город
        self.order_page.fill_address_info(
            city="",  # Пустой город
            address="ул. Тестовая, д. 1"
        )
        
        self.order_page.select_delivery_method("courier")
        self.order_page.select_payment_method("card")
        
        # Пытаемся отправить форму
        self.order_page.submit_order()
        
        # Проверяем наличие ошибки для города
        errors = self.order_page.get_validation_errors()
        city_error = any("город" in error.lower() or "city" in error.lower() for error in errors)
        assert city_error, "Должна появиться ошибка валидации для невыбранного города"
    
    @pytest.mark.validation
    def test_delivery_method_required(self):
        """Тест: проверка обязательного выбора способа доставки"""
        # Заполняем форму без выбора способа доставки
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
        
        # Не выбираем способ доставки
        self.order_page.select_payment_method("card")
        
        # Пытаемся отправить форму
        self.order_page.submit_order()
        
        # Проверяем наличие ошибки для способа доставки
        errors = self.order_page.get_validation_errors()
        delivery_error = any("доставк" in error.lower() or "delivery" in error.lower() for error in errors)
        assert delivery_error, "Должна появиться ошибка валидации для невыбранного способа доставки"
    
    @pytest.mark.validation
    def test_payment_method_required(self):
        """Тест: проверка обязательного выбора способа оплаты"""
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
        
        # Проверяем наличие ошибки для способа оплаты
        errors = self.order_page.get_validation_errors()
        payment_error = any("оплат" in error.lower() or "payment" in error.lower() for error in errors)
        assert payment_error, "Должна появиться ошибка валидации для невыбранного способа оплаты"
