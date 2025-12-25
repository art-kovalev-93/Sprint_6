import pytest
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.chrome.service import Service


@pytest.fixture(scope="function")
def driver():
    """Используем локальный Chrome в том же контейнере."""

    chrome_options = Options()

    # Обязательные опции
    chrome_options.add_argument('--no-sandbox')
    chrome_options.add_argument('--disable-dev-shm-usage')
    #chrome_options.add_argument('--headless')
    chrome_options.add_argument('--disable-gpu')

    # Используем Chrome напрямую, без Selenium Standalone
    # В образе selenium/standalone-chrome уже есть Chrome и chromedriver
    driver = webdriver.Chrome(
        service=Service('/usr/bin/chromedriver'),  # путь в selenium/standalone-chrome образе
        options=chrome_options
    )

    driver.implicitly_wait(10)
    driver.maximize_window()

    yield driver

    driver.quit()