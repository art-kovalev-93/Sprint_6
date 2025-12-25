from locators.main_page_locators import MainPageLocators
import allure
from pages.base_page import BasePage


class MainPage(BasePage):

    @allure.step('Нажать кнопку Заказать в хидере')
    def click_order_button_on_header(self):
        self.click_element(locator=MainPageLocators.book_button_header_locator)

    @allure.step('Нажать кнопку Заказать в теле страницы')
    def click_order_button_on_page(self):
        self.click_element(locator=MainPageLocators.book_button_page_locator)

    @allure.step('Нажать на вопрос в блоке Вопросы о важном.')
    def click_accordion_button(self, i):
        self.click_i_obj(locator=MainPageLocators.accordion_button_locator,i=i)

    @allure.step('Ожидаем раскрытия вопроса')
    def wait_answer_text(self,i):
        self.wait_visibility_element(locator = MainPageLocators.accordion_text_locator[i])

    @allure.step('Получили текст Ответа со страницы')
    def get_answer_text(self, i):
        return self.find_element_get_text(locator=MainPageLocators.accordion_text_locator[i])

    @allure.step('Нажать кнопку Принять cookie')
    def click_accept_cookie(self):
        self.click_element(locator = MainPageLocators.accept_cookie_button)