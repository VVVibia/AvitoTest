from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from .base_page import BasePage
from .locators import ProductPageLocators


class ProductPage(BasePage):
    def favorites_button_should_change_name(self):
        """Текст кнопки "Добавить в избранное" меняется на "В избранном" """
        favorites_button_new = WebDriverWait(self.driver, 10).until(
            EC.presence_of_element_located(*ProductPageLocators.FAVORITES_BUTTON_NEW)
        )
        assert favorites_button_new.text == "В избранном", "Button text 'Добавить в избранное' hasn't changed to 'В избранном'"


    def get_product_name(self):
        """Получаем название товара"""
        product_name = self.driver.find_element(*ProductPageLocators.PRODUCT_NAME)
        return product_name.text


    def add_to_favorites_from_add_card(self):
         """Добавляем в избранное"""
         favorites_button = self.driver.find_element(*ProductPageLocators.FAVORITES_BUTTON)
         favorites_button.click()



