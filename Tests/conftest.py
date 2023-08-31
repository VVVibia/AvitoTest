import pytest
from selenium import webdriver


@pytest.fixture(scope="function")
def driver():
    """Для каждого теста будет запускаться свой экземпляр браузера и закрываться после завершения теста"""
    driver = webdriver.Chrome()
    yield driver
    driver.quit()



