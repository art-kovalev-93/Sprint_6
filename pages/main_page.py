from selenium.webdriver.support import expected_conditions
from selenium.webdriver.support.wait import WebDriverWait
from locators.main_page_locators import MainPageLocators
import allure


class MainPage:
    def __init__(self, driver):
        self.driver = driver

    @allure.step('Нажать кнопку Заказать в хидере')
    def click_order_button_on_header(self):
        self.driver.find_element(*MainPageLocators.book_button_header_locator).click()

    @allure.step('Нажать кнопку Заказать в теле страницы')
    def click_order_button_on_page(self):
        self.driver.find_element(*MainPageLocators.book_button_page_locator).click()

    @allure.step('Нажать на вопрос в блоке Вопросы о важном.')
    def click_accordion_button(self, i):
        accordions = self.driver.find_elements(*MainPageLocators.accordion_button_locator)
        accordions[i].click()

    @allure.step('Ожидаем раскрытия вопроса')
    def wait_answer_text(self,i):
        locator = MainPageLocators.accordion_text_locator[i]
        WebDriverWait(self.driver, 3).until(expected_conditions.visibility_of_element_located((locator)))

    @allure.step('Получили текст Ответа со страницы')
    def get_answer_text(self, i):
        locator = MainPageLocators.accordion_text_locator[i]
        return self.driver.find_element(*locator).text

    @allure.step('Нажать кнопку Принять cookie')
    def click_accept_cookie(self):
        self.driver.find_element(*MainPageLocators.accept_cookie_button).click()