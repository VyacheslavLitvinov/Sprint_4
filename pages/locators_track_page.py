import allure
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions


# https://qa-scooter.praktikum-services.ru/order
class TrackPage:
    cancel_button_page = [By.XPATH, '//div[2]/div[2]/div[1]/button']  # кнопка отмены на странице
    ask_window = [By.XPATH, '//body/div/div/div[2]/div[4]/div[1]']  # сообщение "Хотите отменить заказ?"
    cancel_button_window = [By.XPATH, '//div[4]/div[2]/button[2]']  # кнопка отмены в окне
    cancel_window = [By.XPATH, '//body/div/div/div[2]/div[4]/div[1]']  # сообщение об отмене заказа

    def __init__(self, driver):
        self.driver = driver

    @allure.step('ждем отображения кнопки "Отменить заказ"')
    def cancel_button_wait(self):
        return WebDriverWait(self.driver, 3).until(
            expected_conditions.visibility_of_element_located(self.cancel_button_page))

    def cancel_button_text(self):
        return self.driver.find_element(*self.cancel_button_page).text

    @allure.step('нажимаем на кнопку "Отменить заказ"')
    def cancel_button_page_click(self):
        return self.driver.find_element(*self.cancel_button_page).click()

    @allure.step('текст диалогового окна "Хотите отменить заказ?"')
    def ask_window_text(self):
        return self.driver.find_element(*self.ask_window).text

    @allure.step('нажимаем на кнопку отмены заказа в диалоговом окне')
    def cancel_button_window_click(self):
        return self.driver.find_element(*self.cancel_button_window).click()

    @allure.step('Текст сообщения "Заказ отменен"')
    def cancel_window_text(self):
        return self.driver.find_element(*self.cancel_window).text

    def cancel_window_wait(self):
        return WebDriverWait(self.driver, 3).until(
            expected_conditions.text_to_be_present_in_element(self.cancel_window, 'Заказ отменён'))