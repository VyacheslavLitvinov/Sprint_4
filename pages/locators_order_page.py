import allure
from selenium.webdriver import Keys
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions


# https://qa-scooter.praktikum-services.ru/order
class OrderPage:
    header_scooter_order = [By.CLASS_NAME, 'Order_Header__BZXOb']  # Заголовок "Для кого самокат"
    name_field = [By.XPATH, '//div[2]/div[1]/input']  # Поле "Имя"
    surname_field = [By.XPATH, '//div[2]/input']  # Поле "Фамилия"
    address_field = [By.XPATH, '//div[3]/input']  # Поле "Адрес: куда привезти заказ"
    phone_field = [By.XPATH, '//div[5]/input']  # Поле "Телефон: на него позвонит курьер"
    next_button = [By.XPATH, './/*[text()="Далее"]']  # Кнопка "Далее"
    test_subway = [By.CLASS_NAME, 'select-search__input']  # Поле метро

    subway_window = [By.XPATH, '//div[4]/div/div[2]']  # Открытое поле метро
    # Страница "Про аренду"
    header_about_rent = [By.CLASS_NAME, 'Order_Header__BZXOb']  # Заголовок об аренде
    date_field = [By.XPATH, '//div[1]/div/input']  # Поле даты
    date_on_window_1 = [By.XPATH, '//div[5]/div[6]']  # Окно выбора даты
    lease_field = [By.XPATH, ".//*[@class='Dropdown-arrow']"]  # Поле выбора доставки
    lease_window = (By.XPATH, ".//*[@class='Dropdown-menu']/div")  # Выбор периода доставки
    test_color_scooter_black = [By.XPATH, '//label[1]']  # Чекбокс черного самоката
    test_color_scooter = [By.XPATH, ".//*[@class='Checkbox_Label__3wxSf']"]  # Чекбокс серого самоката
    comment_field = [By.XPATH, '//div[4]/input']  # Поле комментария
    button_back = [By.XPATH, '//div[2]/div[3]/button[1]']  # Кнопка "Назад"
    button_to_order = [By.XPATH, '//div[2]/div[3]/button[2]']  # Кнопка "Заказать"
    # Всплывающее окно "Хочешь оформить заказ?"
    button_yes = [By.XPATH, './/*[text()="Да"]']  # Кнопка "Да"
    button_no = [By.XPATH, './/*[text()="Нет"]']  # Кнопка "Нет"
    # Заказ оформлен
    text_order = [By.CLASS_NAME, 'Order_ModalHeader__3FDaJ']  # Поле оформленного заказа
    button_check_status = [By.XPATH, ".//button[(@class = 'Button_Button__ra12g Button_Middle__1CSJM' and text()='Посмотреть статус')]"]  # Кнопка "Проверить статус"


    def __init__(self, driver):
        self.driver = driver

    # Заголовок "Для кого самокат"
    @allure.step('ждем прогрузки заголовка "Для кого самокат"')
    def header_scooter_order_wait(self):
        return WebDriverWait(self.driver, 3).until(
            expected_conditions.visibility_of_element_located(self.header_scooter_order))

    def header_scooter_order_text(self):
        return self.driver.find_element(*self.header_scooter_order).text

    # Обязательные поля для заполнения
    def set_name(self, name):
        self.driver.find_element(*self.name_field).send_keys(name)

    def set_surname(self, surname):
        self.driver.find_element(*self.surname_field).send_keys(surname)

    def set_address(self, address):
        self.driver.find_element(*self.address_field).send_keys(address)

    def set_subway(self, subway):
        self.driver.find_element(*self.test_subway).click()
        self.driver.find_element(*self.test_subway).send_keys(subway)
        self.driver.find_element(*self.test_subway).send_keys(Keys.ARROW_DOWN + Keys.ENTER)

    def set_phone(self, phone):
        self.driver.find_element(*self.phone_field).send_keys(phone)

    @allure.step('нажимаем кнопку "Далее"')
    def click_next_button(self):
        self.driver.find_element(*self.next_button).click()

    # Шаг заполнения полей в окне заказа с тестовыми данными
    @allure.step('заполняем поля имя, фамилия, адрес, станция метро и телефон тестовыми данными')
    def set_first_page_order(self, name, surname, phone, address, subway):
        self.set_name(name)
        self.set_surname(surname)
        self.set_address(address)
        self.set_subway(subway)
        self.set_phone(phone)

    # Страница "Про аренду"
    @allure.step('выбираем дату')
    def set_date(self, test_date):
        self.driver.find_element(*self.date_field).send_keys(test_date)
        self.driver.find_element(*self.date_on_window_1).click()

    @allure.step('выбираем срок аренды')
    def set_lease(self, days_lease):
        self.driver.find_element(*self.lease_field).click()
        self.driver.find_elements(*self.lease_window)[days_lease].click()

    @allure.step('выбираем цвет самоката')
    def set_color_scooter(self, color_number):
        return self.driver.find_elements(*self.test_color_scooter)[color_number].click()

    @allure.step('пишем комментарий')
    def set_comment(self, comment):
        return self.driver.find_element(*self.comment_field).send_keys(comment)

    @allure.step('нажимаем на кнопку "Заказать"')
    def button_to_order_click(self):
        return self.driver.find_element(*self.button_to_order).click()

    @allure.step('нажимаем на кнопку "Назад"')
    def button_back_click(self):
        return self.driver.find_element(*self.button_back).click()

    # Шаг заполнения полей во втором окне заказа с тестовыми данными
    def set_second_page_order(self, date, days_lease, color_number, comment):
        self.set_date(date)
        self.set_lease(days_lease)
        self.set_color_scooter(color_number)
        self.set_comment(comment)

    @allure.step('нажимаем на кнопку "Да"')
    def button_yes_click(self):
        self.driver.find_element(*self.button_yes).click()

    def wait_button_yes(self):
        WebDriverWait(self.driver, 10).until(
            expected_conditions.element_to_be_clickable(self.button_yes))

    @allure.step('нажимаем на кнопку "Нет"')
    def button_no_click(self):
        return self.driver.find_element(*self.button_no).click()

    def wait_button_status(self):
        WebDriverWait(self.driver, 5).until(
            expected_conditions.element_to_be_clickable(self.button_check_status))

    def button_status_text(self):
        return self.driver.find_element(*self.button_check_status).text

    def button_status_click(self):
        return self.driver.find_element(*self.button_check_status).click()

    def order_text(self):
        return self.driver.find_element(*self.text_order).text

    def wait_order_text(self):
        WebDriverWait(self.driver, 5).until(
            expected_conditions.visibility_of_element_located(self.text_order))

    def header_about_rent_text(self):
        return self.driver.find_element(*self.header_about_rent).text

