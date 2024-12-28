from selenium.webdriver.common.by import By



class MainPageLocators:
    accordion_button_locator = [By.CSS_SELECTOR, ".accordion__button"]
    accordion_text_locator = [[By.XPATH, '//*[@id="accordion__panel-0"]/p'],[By.XPATH, '//*[@id="accordion__panel-1"]/p'],[By.XPATH, '//*[@id="accordion__panel-2"]/p'],[By.XPATH, '//*[@id="accordion__panel-3"]/p'],[By.XPATH, '//*[@id="accordion__panel-4"]/p'],[By.XPATH, '//*[@id="accordion__panel-5"]/p'],[By.XPATH, '//*[@id="accordion__panel-6"]/p'],[By.XPATH, '//*[@id="accordion__panel-7"]/p']]
    book_button_in_header_locator = [By.CSS_SELECTOR, ".Header_Nav__AGCXC .Button_Button__ra12g"]
    book_button_header_locator = [By.CLASS_NAME, "Button_Button__ra12g"]
    book_button_page_locator = [By.CSS_SELECTOR, ".Button_Middle__1CSJM"]
    accept_cookie_button = [By.CSS_SELECTOR, "#rcc-confirm-button"]
