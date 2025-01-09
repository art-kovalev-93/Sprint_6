from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from urls import base_url


class BasePage:
    def __init__(self, driver):
        self.driver = driver
        self.url = base_url

    def go_to_site(self):
        self.driver.get(self.url)

    def find_element(self, locator, time = 5):
        return WebDriverWait(self.driver, time).until(EC.presence_of_element_located(locator), message=f'Not find element {locator}')

    def click_element(self, locator):
        return self.find_element(locator=locator).click()

    def click_i_obj(self, locator, i):
        return self.find_elements(locator = locator)[i].click()

    def find_element_get_text(self, locator):
        return self.find_element(locator=locator).text

    def find_elements(self, locator, time = 5):
        return WebDriverWait(self.driver, time).until(EC.visibility_of_all_elements_located(locator), message=f'Not find elements {locator}')

    def wait_visibility_element(self, locator, time = 5):
        return WebDriverWait(self.driver, time).until(EC.visibility_of_element_located(locator), message=f'Not find element {locator}')

    def current_url(self):
        return self.driver.current_url

    def send_keys(self, locator, text):
        return self.find_element(locator=locator).send_keys(text)

    def wait_url_to_be(self, url, time = 5):
        return WebDriverWait(self.driver, time).until(EC.url_to_be(url))

    def open_next_tab(self):
        handles = self.driver.window_handles
        return self.driver.switch_to.window(handles[-1])