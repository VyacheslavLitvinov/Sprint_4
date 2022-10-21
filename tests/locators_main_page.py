import allure
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions


# https://qa-scooter.praktikum-services.ru/
class MainPage:
    url = 'https://qa-scooter.praktikum-services.ru/'
    yandex_url = 'https://dzen.ru/?yredirect=true'
    header_scooter = [By.XPATH, '//*[@class="Home_Header__iJKdX"]']  # Заголовок "Самокат на пару дней"
    order_button_above = [By.XPATH, "//button[@class= 'Button_Button__ra12g']"]  # Верхняя кнопка заказа
    order_button_mid = [By.XPATH, '//div[5]/button']  # Нижняя кнопка заказа
    scroll = "arguments[0].scrollIntoView();"  # Скрипт для скролла
    scooter_button = [By.XPATH, '//a[2]/img']  # Кнопка "Самокат"
    yandex_button = [By.XPATH, '//a[1]/img']  # Кнопка "Яндекс"

    # кнопки вопросов
    faq_1 = [By.XPATH, '//div[@id="accordion__heading-0"]']
    answer_faq_1 = [By.XPATH, '//div[1]/div[2]/p']
    faq_2 = [By.XPATH, '//div[@id="accordion__heading-1"]']
    answer_faq_2 = [By.XPATH, '//div[2]/div[2]/p']
    faq_3 = [By.XPATH, '//*[@id="accordion__heading-2"]']
    answer_faq_3 = [By.XPATH, '//div[3]/div[2]/p']
    faq_4 = [By.XPATH, '//*[@id="accordion__heading-3"]']
    answer_faq_4 = [By.XPATH, '//div[4]/div[2]/p']
    faq_5 = [By.XPATH, '//*[@id="accordion__heading-4"]']
    answer_faq_5 = [By.XPATH, '//div[5]/div[2]/p']
    faq_6 = [By.XPATH, '//*[@id="accordion__heading-5"]']
    answer_faq_6 = [By.XPATH, '//div[6]/div[2]/p']
    faq_7 = [By.XPATH, '//*[@id="accordion__heading-6"]']
    answer_faq_7 = [By.XPATH, '//div[7]/div[2]/p']
    faq_8 = [By.XPATH, '//*[@id="accordion__heading-7"]']
    answer_faq_8 = [By.XPATH, '//div[8]/div[2]/p']

    def __init__(self, driver):
        self.driver = driver

    @allure.step('ждем пока прогрузится заголовок "Самокат"')
    def wait_header(self):
        return WebDriverWait(self.driver, 3).until(
            expected_conditions.visibility_of_element_located(self.header_scooter))

    @allure.step('выполняем скролл до первой кнопки вопроса')
    def scroll_faq(self):
        return self.driver.execute_script(self.scroll, self.button_faq_1())

    @allure.step('выполняем скролл до кнопки заказа')
    def scroll_mid_order(self):
        return self.driver.execute_script(self.scroll, self.order_button_mid_find())

    # Вопрос "Сколько это стоит? И как оплатить?"
    def button_faq_1(self):
        return self.driver.find_element(*self.faq_1)

    @allure.step('ждем когда кнопка с первым вопросом появится')
    def wait_button_faq_1(self):
        return WebDriverWait(self.driver, 3).until(
            expected_conditions.visibility_of_element_located(self.faq_1))

    @allure.step('нажимаем на кнопку первого вопроса')
    def click_button_faq_1(self):
        return self.driver.find_element(*self.faq_1).click()

    @allure.step('проверяем текст ответа')
    def find_answer_faq_1(self):
        return self.driver.find_element(*self.answer_faq_1).text

    @allure.step('ждем текст ответа')
    def wait_answer_faq_1(self):
        return WebDriverWait(self.driver, 3).until(
            expected_conditions.visibility_of_element_located(self.answer_faq_1))

    # Вопрос "Хочу сразу несколько самокатов! Так можно?"
    @allure.step('ждем когда кнопка со вторым вопросом появится')
    def wait_button_faq_2(self):
        return WebDriverWait(self.driver, 3).until(
            expected_conditions.visibility_of_element_located(self.faq_2))

    @allure.step('нажимаем на кнопку второго вопроса')
    def click_button_faq_2(self):
        return self.driver.find_element(*self.faq_2).click()

    @allure.step('проверяем текст ответа')
    def find_answer_faq_2(self):
        return self.driver.find_element(*self.answer_faq_2).text

    @allure.step('ждем текст ответа')
    def wait_answer_faq_2(self):
        return WebDriverWait(self.driver, 3).until(
            expected_conditions.visibility_of_element_located(self.answer_faq_2))

    # Вопрос "Как рассчитывается время аренды?"
    @allure.step('ждем когда кнопка с третьим вопросом появится')
    def wait_button_faq_3(self):
        return WebDriverWait(self.driver, 3).until(
            expected_conditions.visibility_of_element_located(self.faq_3))

    @allure.step('нажимаем на кнопку третьего вопроса')
    def click_button_faq_3(self):
        return self.driver.find_element(*self.faq_3).click()

    @allure.step('проверяем текст ответа')
    def find_answer_faq_3(self):
        return self.driver.find_element(*self.answer_faq_3).text

    @allure.step('ждем текст ответа')
    def wait_answer_faq_3(self):
        return WebDriverWait(self.driver, 3).until(
            expected_conditions.visibility_of_element_located(self.answer_faq_3))

    # Вопрос "Можно ли заказать самокат прямо на сегодня?"
    @allure.step('ждем когда кнопка с четвертым вопросом появится')
    def wait_button_faq_4(self):
        return WebDriverWait(self.driver, 3).until(
            expected_conditions.visibility_of_element_located(self.faq_4))

    @allure.step('нажимаем на кнопку четвертого вопроса')
    def click_button_faq_4(self):
        return self.driver.find_element(*self.faq_4).click()

    @allure.step('проверяем текст ответа')
    def find_answer_faq_4(self):
        return self.driver.find_element(*self.answer_faq_4).text

    @allure.step('ждем текст ответа')
    def wait_answer_faq_4(self):
        return WebDriverWait(self.driver, 3).until(
            expected_conditions.visibility_of_element_located(self.answer_faq_4))

    # Вопрос "Можно ли продлить заказ или вернуть самокат раньше?"
    @allure.step('ждем когда кнопка с пятым вопросом появится')
    def wait_button_faq_5(self):
        return WebDriverWait(self.driver, 3).until(
            expected_conditions.visibility_of_element_located(self.faq_5))

    @allure.step('нажимаем на кнопку пятого вопроса')
    def click_button_faq_5(self):
        return self.driver.find_element(*self.faq_5).click()

    @allure.step('проверяем текст ответа')
    def find_answer_faq_5(self):
        return self.driver.find_element(*self.answer_faq_5).text

    @allure.step('ждем текст ответа')
    def wait_answer_faq_5(self):
        return WebDriverWait(self.driver, 3).until(
            expected_conditions.visibility_of_element_located(self.answer_faq_5))

    # Вопрос "Вы привозите зарядку вместе с самокатом?"
    @allure.step('ждем когда кнопка с шестым вопросом появится')
    def wait_button_faq_6(self):
        return WebDriverWait(self.driver, 3).until(
            expected_conditions.visibility_of_element_located(self.faq_6))

    @allure.step('нажимаем на кнопку шестого вопроса')
    def click_button_faq_6(self):
        return self.driver.find_element(*self.faq_6).click()

    @allure.step('проверяем текст ответа')
    def find_answer_faq_6(self):
        return self.driver.find_element(*self.answer_faq_6).text

    @allure.step('ждем текст ответа')
    def wait_answer_faq_6(self):
        return WebDriverWait(self.driver, 3).until(
            expected_conditions.visibility_of_element_located(self.answer_faq_6))

    # Вопрос "Можно ли отменить заказ?"
    @allure.step('ждем когда кнопка с седьмым вопросом появится')
    def wait_button_faq_7(self):
        return WebDriverWait(self.driver, 3).until(
            expected_conditions.visibility_of_element_located(self.faq_7))

    @allure.step('нажимаем на кнопку седьмого вопроса')
    def click_button_faq_7(self):
        return self.driver.find_element(*self.faq_7).click()

    @allure.step('проверяем текст ответа')
    def find_answer_faq_7(self):
        return self.driver.find_element(*self.answer_faq_7).text

    @allure.step('ждем текст ответа')
    def wait_answer_faq_7(self):
        return WebDriverWait(self.driver, 3).until(
            expected_conditions.visibility_of_element_located(self.answer_faq_7))

    # Вопрос "Я живу за МКАДом, привезёте?"
    @allure.step('ждем когда кнопка с восьмым вопросом появится')
    def wait_button_faq_8(self):
        return WebDriverWait(self.driver, 3).until(
            expected_conditions.visibility_of_element_located(self.faq_8))

    @allure.step('нажимаем на кнопку восьмого вопроса')
    def click_button_faq_8(self):
        return self.driver.find_element(*self.faq_8).click()

    @allure.step('проверяем текст ответа')
    def find_answer_faq_8(self):
        return self.driver.find_element(*self.answer_faq_8).text

    @allure.step('ждем текст ответа')
    def wait_answer_faq_8(self):
        return WebDriverWait(self.driver, 3).until(
            expected_conditions.visibility_of_element_located(self.answer_faq_8))

    # Верхняя кнопка заказа
    @allure.step('нажимаем на верхнюю кнопку заказа')
    def order_button_above_click(self):
        return self.driver.find_element(*self.order_button_above).click()

    # Средняя кнопка заказа
    def order_button_mid_find(self):
        return self.driver.find_element(*self.order_button_mid)

    @allure.step('ждем центральную кнопку заказа')
    def order_button_mid_wait(self):
        return WebDriverWait(self.driver, 3).until(
            expected_conditions.visibility_of_element_located(self.order_button_above))

    @allure.step('нажимаем на центральную кнопку заказа')
    def order_button_mid_click(self):
        return self.driver.find_element(*self.order_button_mid).click()

    # Кнопка "Самокат"
    @allure.step('нажимаем на кнопку Самоката')
    def scooter_button_click(self):
        return self.driver.find_element(*self.scooter_button).click()

    # Кнопка "Яндекс"
    @allure.step('нажимаем на кнопку Яндекс')
    def yandex_button_click(self):
        return self.driver.find_element(*self.yandex_button).click()
