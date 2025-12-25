import pytest
from selenium import webdriver
from selenium.webdriver.common.desired_capabilities import DesiredCapabilities


@pytest.fixture
def driver():
    # Указываем адрес Selenium Hub (в нашем случае это localhost:4444)
    hub_url = "http://localhost:4444/wd/hub"

    # Создаем capabilities для Chrome
    capabilities = DesiredCapabilities.CHROME.copy()

    # Создаем экземпляр удаленного драйвера
    driver = webdriver.Remote(command_executor=hub_url, desired_capabilities=capabilities)

    # Возвращаем драйвер
    yield driver

    # Закрываем драйвер после теста
    driver.quit()