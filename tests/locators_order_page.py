import allure
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
    next_button = [By.XPATH, '//div[2]/div[3]/button']  # Кнопка "Далее"
    #  первые тестовые данные
    test_name_1 = 'Дэвид'  # Поле имени тестовые данные №1
    test_surname_1 = 'Бекхэм'  # Поле фамилии тестовые данные №1
    test_address_1 = 'Лондон'  # Поле адреса тестовые данные №1
    test_phone_1 = '89879766655'  # Поле телефона тестовые данные №1
    test_subway = [By.CLASS_NAME, 'select-search__input']  # Поле метро
    test_subway_window_1 = [By.XPATH, '//li[6]/button']  # Открытое поле метро первый вариант
    #  вторые тестовые данные
    test_name_2 = 'Семён'  # Поле имени тестовые данные №2
    test_surname_2 = 'РимскийКорсаков'  # Поле имени тестовые данные №2
    test_address_2 = 'ЛЕНИНГРАД'  # Поле адреса тестовые данные №2
    test_phone_2 = '+781151515151'  # Поле телефона тестовые данные №2
    test_subway_window_2 = [By.XPATH, '//li[10]/button']  # Открытое поле метро второй вариант
    # Страница "Про аренду"
    header_about_rent = [By.CLASS_NAME, 'Order_Header__BZXOb']  # Заголовок об аренде
    date_field = [By.XPATH, '//div[1]/div/input']  # Поле даты
    test_date_1 = '31.12.2022'  # Тестовая дата №1
    test_date_2 = '23.10.2022'  # Тестовая дата №2
    date_on_window_1 = [By.XPATH, '//div[5]/div[6]']  # Окно выбора даты
    lease_field = [By.XPATH, '//div[2]/div[2]/div[2]/div/div[1]']  # Поле выбора доставки
    test_lease_day_1 = [By.XPATH, '//div[2]/div[2]/div[2]/div[2]/div[1]']  # Выбор периода доставки 1 день
    test_lease_day_7 = [By.XPATH, '//div[2]/div[2]/div[2]/div[2]/div[7]']  # Выбор периода доставки 7 дней
    test_color_scooter_black = [By.XPATH, '//label[1]']  # Чекбокс черного самоката
    test_color_scooter_grey = [By.XPATH, '//label[2]']  # Чекбокс серого самоката
    comment_field = [By.XPATH, '//div[4]/input']  # Поле комментария
    test_comment_1 = 'Буду ждать в черной шляпе в сером плаще, с милым корги'  # Поле комментария тестовый №1
    test_comment_2 = 'Canada is the second largest country in the world. ' \
                     'Its territory stretches practically from the North Pole to the subtropical regions, from the Pacific Ocean to the Atlantic Ocean.' \
                     ' Along with the capital — Ottawa, the largest metropolitan areas are Montreal, Calgary, Winnipeg and Toronto. ' \
                     'A large number of islands make up the Canadian territory, including Baffin’s Land, Victoria, Newfoundland and others.'

    button_back = [By.XPATH, '//div[2]/div[3]/button[1]']  # Кнопка "Назад"
    button_to_order = [By.XPATH, '//div[2]/div[3]/button[2]']  # Кнопка "Заказать"
    # Всплывающее окно "Хочешь оформить заказ?"
    button_yes = [By.XPATH, '//div[5]/div[2]/button[2]']  # Кнопка "Да"
    button_no = [By.XPATH, '//div[5]/div[2]/button[2]']  # Кнопка "Нет"
    # Заказ оформлен
    text_order = [By.CLASS_NAME, 'Order_ModalHeader__3FDaJ']  # Поле оформленного заказа
    button_check_status = [By.XPATH, '//div[2]/div[5]/div[2]/button']  # Кнопка "Проверить статус"

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
    def set_name(self, test_name):
        self.driver.find_element(*self.name_field).send_keys(test_name)

    def set_surname(self, test_surname):
        self.driver.find_element(*self.surname_field).send_keys(test_surname)

    def set_address(self, test_address):
        self.driver.find_element(*self.address_field).send_keys(test_address)

    def set_subway_1(self):
        self.driver.find_element(*self.test_subway).click()
        WebDriverWait(self.driver, 3).until(
            expected_conditions.visibility_of_element_located(self.test_subway_window_1))
        self.driver.find_element(*self.test_subway_window_1).click()

    def set_subway_2(self):
        self.driver.find_element(*self.test_subway).click()
        WebDriverWait(self.driver, 3).until(
            expected_conditions.visibility_of_element_located(self.test_subway_window_2))
        self.driver.find_element(*self.test_subway_window_2).click()

    def set_phone(self, test_phone):
        self.driver.find_element(*self.phone_field).send_keys(test_phone)

    @allure.step('нажимаем кнопку "Далее"')
    def click_next_button(self):
        self.driver.find_element(*self.next_button).click()

    # Шаг заполнения полей в окне заказа с тестовыми данными №1
    @allure.step('заполняем поля имя, фамилия, адрес, станция метро и телефон тестовыми данными №1')
    def set_first_page_order_1(self):
        self.set_name(self.test_name_1)
        self.set_surname(self.test_surname_1)
        self.set_address(self.test_address_1)
        self.set_subway_1()
        self.set_phone(self.test_phone_1)

    # Шаг заполнения полей в окне заказа с тестовыми данными №2
    @allure.step('заполняем поля имя, фамилия, адрес, станция метро и телефон тестовыми данными №2')
    def set_first_page_order_2(self):
        self.set_name(self.test_name_2)
        self.set_surname(self.test_surname_2)
        self.set_address(self.test_address_2)
        self.set_subway_2()
        self.set_phone(self.test_phone_2)

    # Страница "Про аренду"
    @allure.step('выбираем дату')
    def set_date(self, test_date):
        self.driver.find_element(*self.date_field).send_keys(test_date)
        self.driver.find_element(*self.date_on_window_1).click()

    @allure.step('выбираем срок аренды 1 день')
    def set_lease_1(self):
        self.driver.find_element(*self.lease_field).click()
        WebDriverWait(self.driver, 3).until(
            expected_conditions.visibility_of_element_located(self.test_lease_day_1))
        return self.driver.find_element(*self.test_lease_day_1).click()

    @allure.step('выбираем срок аренды 7 дней')
    def set_lease_7(self):
        self.driver.find_element(*self.lease_field).click()
        WebDriverWait(self.driver, 3).until(
            expected_conditions.visibility_of_element_located(self.test_lease_day_7))
        return self.driver.find_element(*self.test_lease_day_7).click()

    @allure.step('выбираем цвет самоката - черный')
    def set_color_scooter_black(self):
        return self.driver.find_element(*self.test_color_scooter_black).click()

    @allure.step('выбираем цвет самоката - серый')
    def set_color_scooter_grey(self):
        return self.driver.find_element(*self.test_color_scooter_grey).click()

    @allure.step('пишем комментарий')
    def set_comment(self, test_comment):
        return self.driver.find_element(*self.comment_field).send_keys(test_comment)

    @allure.step('нажимаем на кнопку "Заказать"')
    def button_to_order_click(self):
        return self.driver.find_element(*self.button_to_order).click()

    @allure.step('нажимаем на кнопку "Назад"')
    def button_back_click(self):
        return self.driver.find_element(*self.button_back).click()

    # Шаг заполнения полей во втором окне заказа с тестовыми данными №1
    def set_second_page_order_1(self):
        self.set_date(self.test_date_1)
        self.set_lease_1()
        self.set_color_scooter_black()
        self.set_comment(self.test_comment_1)

    # Шаг заполнения полей во втором окне заказа с тестовыми данными №2
    def set_second_page_order_2(self):
        self.set_date(self.test_date_2)
        self.set_lease_7()
        self.set_color_scooter_grey()
        self.set_comment(self.test_comment_2)

    @allure.step('нажимаем на кнопку "Да"')
    def button_yes_click(self):
        return self.driver.find_element(*self.button_yes).click()

    @allure.step('нажимаем на кнопку "Нет"')
    def button_no_click(self):
        return self.driver.find_element(*self.button_no).click()

    def button_status_text(self):
        return self.driver.find_element(*self.button_check_status).text

    def button_status_click(self):
        return self.driver.find_element(*self.button_check_status).click()

    def order_text(self):
        return self.driver.find_element(*self.text_order).text

    def header_about_rent_text(self):
        return self.driver.find_element(*self.header_about_rent).text

