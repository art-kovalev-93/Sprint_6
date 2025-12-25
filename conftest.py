import pytest
from selenium import webdriver
import urls
from selenium.webdriver.chrome.options import Options


@pytest.fixture(scope="session")
def driver():
    chrome_options = Options()

    # Опции для Docker среды
    chrome_options.add_argument('--no-sandbox')
    chrome_options.add_argument('--disable-dev-shm-usage')
    chrome_options.add_argument('--disable-gpu')
    chrome_options.add_argument('--window-size=1920,1080')


    driver = webdriver.Remote(
        command_executor='http://localhost:4444/wd/hub',
        options=chrome_options
    )
    driver.implicitly_wait(10)

    yield driver
    driver.quit()