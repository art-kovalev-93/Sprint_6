from locators.main_page_locators import MainPageLocators
import allure
from pages.base_page import BasePage


class MainPage(BasePage):

    @allure.step('Нажать кнопку Заказать в хидере')
    def click_order_button_on_header(self):
        order_button_on_header = self.find_element(locator=MainPageLocators.book_button_header_locator)
        self.click(order_button_on_header)

    @allure.step('Нажать кнопку Заказать в теле страницы')
    def click_order_button_on_page(self):
        order_button_on_page=self.find_element(locator=MainPageLocators.book_button_page_locator)
        self.click(order_button_on_page) #я тут не понял замечания, нужно ли выносить .click() как отдельный метод в base_page ниже как я изначально подумал
        #self.find_element(locator=MainPageLocators.book_button_page_locator).click() тут вроде все лаконично и без лишних строк, но если надо вынести то реализация выше. (ниже использовал эту реализацию)

    @allure.step('Нажать на вопрос в блоке Вопросы о важном.')
    def click_accordion_button(self, i):
        accordions = self.find_elements(locator=MainPageLocators.accordion_button_locator)
        self.click_i_obj(objects=accordions,i=i) #реализация если надо использовать click() отдельным методом для i элемента

    @allure.step('Ожидаем раскрытия вопроса')
    def wait_answer_text(self,i):
        locator = MainPageLocators.accordion_text_locator[i]
        self.wait_visibility_element(locator = locator)

    @allure.step('Получили текст Ответа со страницы')
    def get_answer_text(self, i):
        locator = MainPageLocators.accordion_text_locator[i]
        return self.find_element_get_text(locator=locator)

    @allure.step('Нажать кнопку Принять cookie')
    def click_accept_cookie(self):
        accept_cookie = self.find_element(locator = MainPageLocators.accept_cookie_button)
        self.click(object=accept_cookie)