import pytest
from selenium import webdriver
import urls



@pytest.fixture
def driver():
    driver = webdriver.Chrome()
    driver.maximize_window()
    driver.get(urls.base_url)
    yield driver
    driver.quit()