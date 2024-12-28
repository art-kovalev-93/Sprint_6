from selenium.webdriver.common.by import By



class OrderPageLocators:
    title_locator = [By.CSS_SELECTOR, ".Order_Header__BZXOb"]
    name_locator = [By.CSS_SELECTOR, "[placeholder='* Имя']"]
    second_name_locator = [By.CSS_SELECTOR, "[placeholder='* Фамилия']"]
    address_locator = [By.CSS_SELECTOR, "[placeholder='* Адрес: куда привезти заказ']"]
    metro_locator = [By.CSS_SELECTOR, ".select-search__input"]
    telephone_locator = [By.CSS_SELECTOR, "[placeholder='* Телефон: на него позвонит курьер']"]
    next_button = [By.CSS_SELECTOR, ".Order_NextButton__1_rCA button"]
    calendar_locator = [By.CSS_SELECTOR, ".react-datepicker__input-container input"]
    calendar_date_locator = [By.CSS_SELECTOR, ".react-datepicker__day--keyboard-selected"]
    metro_station_locator = [By.CSS_SELECTOR, "[data-index='0']"]
    rent_period_locator = [By.CSS_SELECTOR, ".Dropdown-arrow"]
    rent_period_day_locator = [By.CSS_SELECTOR, ".Dropdown-option"]
    color_black_selector = [By.CSS_SELECTOR, "#black"]
    color_grey_selector = [By.CSS_SELECTOR, "#grey"]
    comment_selector = [By.CSS_SELECTOR, "[placeholder = 'Комментарий для курьера']"]
    order_button_locator = [By.CSS_SELECTOR, ".Button_Middle__1CSJM"]
    success_popup_locator = [By.CLASS_NAME, "Order_ModalHeader__3FDaJ"]
    scooter_logo_locator = [By.CSS_SELECTOR, "[alt='Scooter']"]
    yandex_logo_locator = [By.CSS_SELECTOR, "[alt='Yandex']"]
    dzen_logo_locator = [By.CSS_SELECTOR, "[href='/'] use"]
    approve_order_locator = [By.CSS_SELECTOR, "div.Order_Buttons__1xGrp:nth-child(2) > button:nth-child(2)"]
