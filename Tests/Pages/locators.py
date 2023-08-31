from selenium.webdriver.common.by import By


class BasePageLocators:
    FAVORITES_LINK = (By.CSS_SELECTOR, ".desktop-1gzlbya")


class FavoritesPageLocators:
    PRODUCT_NAME_IN_FAVORITES = (By.TAG_NAME, "strong")
    # PRODUCT_NAME_IN_FAVORITES = (By.XPATH, "//*[text()='Domain-Driven Design Distilled Vaughn Vernon']")


class ProductPageLocators:
    FAVORITES_BUTTON_NEW = (By.CSS_SELECTOR, ".desktop-p6xjn6")
    PRODUCT_NAME = (By.CSS_SELECTOR, ".title-info-title-text")
    FAVORITES_BUTTON = (By.CSS_SELECTOR, ".desktop-usq1f1")

