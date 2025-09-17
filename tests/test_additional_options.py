import pytest
from tests.base_test import BaseTest


class TestAdditionalOptions(BaseTest):
    """Тесты для дополнительных опций"""
    
    @pytest.mark.regression
    def test_gift_wrapping_option(self):
        """Тест: опция подарочной упаковки"""
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
        self.order_page.select_payment_method("card")
        
        # Проверяем, что опция подарочной упаковки не выбрана по умолчанию
        assert not self.order_page.gift_wrapping.is_checked()
        
        # Выбираем подарочную упаковку
        self.order_page.set_additional_options(gift_wrapping=True)
        assert self.order_page.gift_wrapping.is_checked()
        
        # Проверяем, что цена изменилась
        total_price = self.order_page.get_total_price()
        assert "500" in total_price  # +500 ₽ за подарочную упаковку
    
    @pytest.mark.regression
    def test_insurance_option(self):
        """Тест: опция страхования посылки"""
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
        self.order_page.select_payment_method("card")
        
        # Проверяем, что опция страхования не выбрана по умолчанию
        assert not self.order_page.insurance.is_checked()
        
        # Выбираем страхование
        self.order_page.set_additional_options(insurance=True)
        assert self.order_page.insurance.is_checked()
        
        # Проверяем, что цена изменилась
        total_price = self.order_page.get_total_price()
        assert "200" in total_price  # +200 ₽ за страхование
    
    @pytest.mark.regression
    def test_newsletter_option(self):
        """Тест: опция подписки на рассылку"""
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
        self.order_page.select_payment_method("card")
        
        # Проверяем, что опция подписки не выбрана по умолчанию
        assert not self.order_page.newsletter.is_checked()
        
        # Выбираем подписку
        self.order_page.set_additional_options(newsletter=True)
        assert self.order_page.newsletter.is_checked()
        
        # Подписка не должна влиять на цену
        total_price = self.order_page.get_total_price()
        assert "89 990" in total_price  # Базовая цена товара
    
    @pytest.mark.regression
    def test_multiple_additional_options(self):
        """Тест: выбор нескольких дополнительных опций"""
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
        self.order_page.select_payment_method("card")
        
        # Выбираем все дополнительные опции
        self.order_page.set_additional_options(
            gift_wrapping=True,
            insurance=True,
            newsletter=True
        )
        
        # Проверяем, что все опции выбраны
        assert self.order_page.gift_wrapping.is_checked()
        assert self.order_page.insurance.is_checked()
        assert self.order_page.newsletter.is_checked()
        
        # Проверяем итоговую цену (89 990 + 500 + 200 = 90 690)
        total_price = self.order_page.get_total_price()
        assert "90 690" in total_price or "90690" in total_price
    
    @pytest.mark.regression
    def test_additional_options_toggle(self):
        """Тест: переключение дополнительных опций"""
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
        self.order_page.select_payment_method("card")
        
        # Выбираем подарочную упаковку
        self.order_page.gift_wrapping.check()
        assert self.order_page.gift_wrapping.is_checked()
        
        # Отключаем подарочную упаковку
        self.order_page.gift_wrapping.uncheck()
        assert not self.order_page.gift_wrapping.is_checked()
        
        # Выбираем страхование
        self.order_page.insurance.check()
        assert self.order_page.insurance.is_checked()
        
        # Отключаем страхование
        self.order_page.insurance.uncheck()
        assert not self.order_page.insurance.is_checked()
    
    @pytest.mark.regression
    def test_comment_field(self):
        """Тест: поле комментария к заказу"""
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
        self.order_page.select_payment_method("card")
        
        # Проверяем, что поле комментария пустое по умолчанию
        assert self.order_page.comment_textarea.input_value() == ""
        
        # Добавляем комментарий
        comment = "Просьба доставить до 18:00. Звонить заранее."
        self.order_page.add_comment(comment)
        
        # Проверяем, что комментарий сохранен
        assert self.order_page.comment_textarea.input_value() == comment
    
    @pytest.mark.regression
    def test_long_comment(self):
        """Тест: длинный комментарий к заказу"""
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
        self.order_page.select_payment_method("card")
        
        # Добавляем длинный комментарий
        long_comment = "Очень длинный комментарий к заказу. " * 10
        self.order_page.add_comment(long_comment)
        
        # Проверяем, что длинный комментарий сохранен
        assert self.order_page.comment_textarea.input_value() == long_comment
    
    @pytest.mark.regression
    def test_additional_options_with_different_delivery_methods(self):
        """Тест: дополнительные опции с разными способами доставки"""
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
        
        # Выбираем дополнительные опции
        self.order_page.set_additional_options(
            gift_wrapping=True,
            insurance=True,
            newsletter=True
        )
        
        # Проверяем работу с курьерской доставкой
        self.order_page.select_delivery_method("courier")
        assert self.order_page.gift_wrapping.is_checked()
        assert self.order_page.insurance.is_checked()
        assert self.order_page.newsletter.is_checked()
        
        # Проверяем работу с самовывозом
        self.order_page.select_delivery_method("pickup")
        assert self.order_page.gift_wrapping.is_checked()
        assert self.order_page.insurance.is_checked()
        assert self.order_page.newsletter.is_checked()
        
        # Проверяем работу с доставкой почтой
        self.order_page.select_delivery_method("post")
        assert self.order_page.gift_wrapping.is_checked()
        assert self.order_page.insurance.is_checked()
        assert self.order_page.newsletter.is_checked()
