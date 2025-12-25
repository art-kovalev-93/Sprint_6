import pytest
from selenium import webdriver
from selenium.webdriver.chrome.options import Options


@pytest.fixture(scope="function")
def driver():
    """Фикстура для инициализации и закрытия драйвера Selenium."""

    # Настройки Chrome
    chrome_options = Options()

    # Обязательные опции для работы в Docker
    chrome_options.add_argument('--no-sandbox')
    chrome_options.add_argument('--disable-dev-shm-usage')
    chrome_options.add_argument('--disable-gpu')
    #chrome_options.add_argument('--headless')  # раскомментировать для headless режима

    # Дополнительные опции для стабильности
    chrome_options.add_argument('--disable-blink-features=AutomationControlled')
    chrome_options.add_experimental_option("excludeSwitches", ["enable-automation"])
    chrome_options.add_experimental_option('useAutomationExtension', False)

    # Для Selenium 4.x используем только options
    driver = webdriver.Remote(
        command_executor='http://localhost:4444/wd/hub',
        options=chrome_options
    )

    # Устанавливаем неявные ожидания
    driver.implicitly_wait(10)

    # Максимизируем окно браузера
    driver.maximize_window()

    yield driver

    # Закрываем браузер после теста
    driver.quit()