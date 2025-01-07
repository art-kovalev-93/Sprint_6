from selenium import webdriver
from pages.main_page import MainPage
from pages.order_page import OrderPage
import urls
import allure
from conftest import driver

class TestOrderPage:

    @allure.title('Проверка позитивного сценария Заказа самоката')
    @allure.description('С главной страницы открываем страницу заказа и заполняем все поля.')
    def test_order_scooter_success(self, driver):
        main_page = MainPage(driver)
        main_page.click_accept_cookie()
        main_page.click_order_button_on_header()
        order_page = OrderPage(driver)
        order_page.set_name()
        order_page.set_second_name()
        order_page.set_address()
        order_page.set_metro()
        order_page.set_telephone()
        order_page.click_next()
        order_page.set_delivery_date()
        order_page.set_period()
        order_page.select_grey()
        order_page.select_black()
        order_page.set_comment()
        order_page.click_order()
        order_page.click_approve()
        assert "Заказ оформлен" in order_page.get_status()

    @allure.title('Проверка Открытия главной страницы через лого Самокат в хидере')
    def test_open_main_page_by_logo(self, driver):
        main_page = MainPage(driver)
        main_page.click_accept_cookie()
        main_page.click_order_button_on_header()
        order_page = OrderPage(driver)
        order_page.click_scooter_logo()
        assert main_page.current_url() == urls.base_url

    @allure.title('Проверка открытия Dzen страницы через лого Яндекс в хидере')
    def test_open_dzen_by_yandex_logo(self, driver):
        main_page = MainPage(driver)
        main_page.click_accept_cookie()
        main_page.click_order_button_on_header()
        order_page = OrderPage(driver)
        order_page.click_yandex_logo()
        order_page.open_next_tab()
        order_page.wait_dzen_url()
        assert main_page.current_url() == urls.dzen_url
