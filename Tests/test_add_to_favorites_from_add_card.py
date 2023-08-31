from .Pages.product_page import ProductPage
from .Pages.favorites_page import FavoritesPage


url = "https://www.avito.ru/nikel/knigi_i_zhurnaly/domain-driven_design_distilled_vaughn_vernon_2639542363"


def test_add_to_favorites(driver):
    page = ProductPage(driver, url)
    page.open()
    name_on_product_page = page.get_product_name()                            # получаем название товара
    page.add_to_favorites_from_add_card()                                     # добавляем в избранное со страницы товара
    page.go_to_favorites_page()                                               # переходим в избранное, клик по сердцу в хедере
    favorites_page = FavoritesPage(driver, driver.current_url)                # неявный переход между страницами
    name_on_favorites_page = favorites_page.get_product_name_in_favorites()   # ищем товар с таким же названием в избранном
    # проверяем, что товар в избранном, сравнивая названия со страницы товара и в избранном
    favorites_page.product_should_be_in_favorites(name_on_product_page, name_on_favorites_page)





















