from selenium.webdriver.support import expected_conditions
from selenium.webdriver.support.wait import WebDriverWait

import urls
from locators.order_page_locators import OrderPageLocators
import allure

from pages.base_page import BasePage


class OrderPage(BasePage):

    @allure.step('Заполнить поле Имя')
    def set_name(self):
        self.send_keys(locator=OrderPageLocators.name_locator, text = "Иван")

    @allure.step('Заполнить поле Фамилия')
    def set_second_name(self):
        self.send_keys(locator=OrderPageLocators.second_name_locator, text="Тостеров")

    @allure.step('Заполнить поле Адрес')
    def set_address(self):
        self.send_keys(locator=OrderPageLocators.address_locator, text="Москва, пр. Ленина, д. 11")

    @allure.step('Заполнить поле Метро')
    def set_metro(self):
        self.find_element(OrderPageLocators.metro_locator).click()
        self.find_element(OrderPageLocators.metro_station_locator).click()

    @allure.step('Заполнить поле Телефон')
    def set_telephone(self):
        self.send_keys(locator=OrderPageLocators.telephone_locator, text="88005553535")

    @allure.step('Заполнить поле Когда привезти самокат')
    def set_delivery_date(self):
        self.find_element(OrderPageLocators.calendar_locator).click()
        self.find_element(OrderPageLocators.calendar_date_locator).click()

    @allure.step('Заполнить поле Срок аренды')
    def set_period(self):
        self.find_element(OrderPageLocators.rent_period_locator).click()
        self.find_element(OrderPageLocators.rent_period_day_locator).click()

    @allure.step('Активировать чекбокс Черный жемчуг')
    def select_black(self):
        self.find_element(OrderPageLocators.color_black_selector).click()

    @allure.step('Активировать чекбокс Серая безысходность')
    def select_grey(self):
        self.find_element(OrderPageLocators.color_grey_selector).click()

    @allure.step('Заполнить комментарий для курьера')
    def set_comment(self):
        self.send_keys(locator = OrderPageLocators.comment_selector, text = "Нужен хороший самокат, плохой не нужен.")

    @allure.step('Нажать кнопку заказать')
    def click_order(self):
        order_btn = self.find_elements(locator=OrderPageLocators.order_button_locator)
        self.click_i_obj(order_btn, i=1)

    @allure.step('Нажать кнопку далее')
    def click_next(self):
        self.find_element(OrderPageLocators.next_button).click()

    @allure.step('Получили текст статуса Заказа')
    def get_status(self):
        return self.find_element(OrderPageLocators.success_popup_locator).text

    @allure.step('Нажать на лого Самокат в хидере')
    def click_scooter_logo(self):
        self.find_element(OrderPageLocators.scooter_logo_locator).click()

    @allure.step('Нажать на лого Яндекс в хидере')
    def click_yandex_logo(self):
        self.find_element(OrderPageLocators.yandex_logo_locator).click()

    @allure.step('Ждем загрузки сайта dzen')
    def wait_dzen_url(self):
        self.wait_url_to_be(url = urls.dzen_url)

    @allure.step('Нажать на кнопку Подтвердить')
    def click_approve(self):
        self.find_element(OrderPageLocators.approve_order_locator).click()