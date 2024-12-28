from selenium.webdriver.support import expected_conditions
from selenium.webdriver.support.wait import WebDriverWait
from locators.order_page_locators import OrderPageLocators
import allure

class OrderPage:
    def __init__(self, driver):
        self.driver = driver

    @allure.step('Ждем загрузки формы заказа')
    def wait_loading_form(self, title):
        WebDriverWait(self.driver, 3).until(expected_conditions.visibility_of_element_located(self.driver.find_element(OrderPageLocators.title_locator)))

    @allure.step('Заполнить поле Имя')
    def set_name(self):
        self.driver.find_element(*OrderPageLocators.name_locator).send_keys("Иван")

    @allure.step('Заполнить поле Фамилия')
    def set_second_name(self):
        self.driver.find_element(*OrderPageLocators.second_name_locator).send_keys("Тостеров")

    @allure.step('Заполнить поле Адрес')
    def set_address(self):
        self.driver.find_element(*OrderPageLocators.address_locator).send_keys("Москва, пр. Ленина, д. 11")

    @allure.step('Заполнить поле Метро')
    def set_metro(self):
        self.driver.find_element(*OrderPageLocators.metro_locator).click()
        self.driver.find_element(*OrderPageLocators.metro_station_locator).click()

    @allure.step('Заполнить поле Телефон')
    def set_telephone(self):
        self.driver.find_element(*OrderPageLocators.telephone_locator).send_keys("88005553535")

    @allure.step('Заполнить поле Когда привезти самокат')
    def set_delivery_date(self):
        self.driver.find_element(*OrderPageLocators.calendar_locator).click()
        self.driver.find_element(*OrderPageLocators.calendar_date_locator).click()

    @allure.step('Заполнить поле Срок аренды')
    def set_period(self):
        self.driver.find_element(*OrderPageLocators.rent_period_locator).click()
        self.driver.find_element(*OrderPageLocators.rent_period_day_locator).click()

    @allure.step('Активировать чекбокс Черный жемчуг')
    def select_black(self):
        self.driver.find_element(*OrderPageLocators.color_black_selector).click()

    @allure.step('Активировать чекбокс Серая безысходность')
    def select_grey(self):
        self.driver.find_element(*OrderPageLocators.color_grey_selector).click()

    @allure.step('Заполнить комментарий для курьера')
    def set_comment(self):
        self.driver.find_element(*OrderPageLocators.comment_selector).send_keys("Нужен хороший самокат, плохой не нужен.")

    @allure.step('Нажать кнопку заказать')
    def click_order(self):
        self.driver.find_elements(*OrderPageLocators.order_button_locator)[1].click()

    @allure.step('Нажать кнопку далее')
    def click_next(self):
        self.driver.find_element(*OrderPageLocators.next_button).click()

    @allure.step('Получили текст статуса Заказа')
    def get_status(self):
        return self.driver.find_element(*OrderPageLocators.success_popup_locator).text

    @allure.step('Нажать на лого Самокат в хидере')
    def click_scooter_logo(self):
        self.driver.find_element(*OrderPageLocators.scooter_logo_locator).click()

    @allure.step('Нажать на лого Яндекс в хидере')
    def click_yandex_logo(self):
        self.driver.find_element(*OrderPageLocators.yandex_logo_locator).click()

    @allure.step('Ждем загрузки сайта dzen')
    def wait_dzen_url(self):
        WebDriverWait(self.driver, 3).until(expected_conditions.url_to_be('https://dzen.ru/?yredirect=true'))

    @allure.step('Нажать на кнопку Подтвердить')
    def click_approve(self):
        self.driver.find_element(*OrderPageLocators.approve_order_locator).click()
