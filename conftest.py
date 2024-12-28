import pytest
from selenium import webdriver
import urls



@pytest.fixture
def driver():
    driver = webdriver.Firefox()
    driver.maximize_window()
    driver.get(urls.main_page_url)
    yield driver
    driver.quit()