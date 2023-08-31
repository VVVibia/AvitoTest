from .locators import BasePageLocators


class BasePage:
    def __init__(self, driver, url):
        self.driver = driver
        self.url = url


    def go_to_favorites_page(self):
        """Переходим в избранное, клик по сердцу в хедере"""
        favorites_link = self.driver.find_element(*BasePageLocators.FAVORITES_LINK)
        favorites_link.click()


    def open(self):
        self.driver.get(self.url)



