import pytest
import allure
import texts
import urls
from pages.main_page import MainPage
from conftest import driver



class TestMainPage:

    @allure.title('Проверка правильности текстов в ответах на главной странице.')
    @allure.description('На главной странице раскрываем вопросы и проверяем ответы.')
    @pytest.mark.parametrize("i", range(0,8))
    def test_qa_form_texts(self, i, driver):
        main_page = MainPage(driver)
        main_page.click_accept_cookie()
        main_page.click_accordion_button(i)
        main_page.wait_answer_text(i)
        assert main_page.get_answer_text(i) == texts.qa_texts[i]

    @allure.title('Проверка открытия страницы Заказа через хидер')
    def test_open_order_page_from_header(self, driver):
        main_page = MainPage(driver)
        main_page.click_accept_cookie()
        main_page.click_order_button_on_header()
        assert main_page.current_url() == urls.order_page_url

    @allure.title('Проверка открытия страницы Заказа через кнопку на странице')
    def test_open_order_page_from_page(self, driver):
        main_page = MainPage(driver)
        main_page.click_accept_cookie()
        main_page.click_order_button_on_page()
        assert main_page.current_url() == urls.order_page_url