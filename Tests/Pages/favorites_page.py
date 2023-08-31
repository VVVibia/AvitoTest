from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from .base_page import BasePage
from .locators import FavoritesPageLocators


class FavoritesPage(BasePage):
    def get_product_name_in_favorites(self):
        """Ищем товар с таким же названием в избранном"""
        product_name_in_favorites = WebDriverWait(self.driver, 10).until(
            EC.presence_of_element_located(FavoritesPageLocators.PRODUCT_NAME_IN_FAVORITES)
        )
        return product_name_in_favorites.text


    def product_should_be_in_favorites(self, name1, name2):
        """Сравниваем названия со страницы товара и в избранном"""
        assert name1 == name2, "Item not in favorites, but should be"

