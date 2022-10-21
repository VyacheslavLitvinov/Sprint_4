import allure
from selenium import webdriver
from locators_main_page import MainPage as MP
from locators_order_page import OrderPage as OP
from locators_track_page import TrackPage as TP


class TestOrderPage:
    driver = None

    @classmethod
    def setup_class(cls):
        cls.driver = webdriver.Firefox()

    @allure.title('Верхняя кнопка заказа на главной')
    @allure.description('Проверяем что работает переход на страницу заказа по верхней кнопке')
    def test_top_order_button_open_page(self):
        self.driver.get(MP.url)
        main_page = MP(self.driver)
        order_page = OP(self.driver)
        main_page.wait_header()
        main_page.order_button_above_click()
        order_page.header_scooter_order_wait()

        assert order_page.header_scooter_order_text() == 'Для кого самокат'

    @allure.title('Центральная кнопка заказа на главной')
    @allure.description('Проверяем что работает переход на страницу заказа по центральной кнопке')
    def test_mid_order_button_open_page(self):
        self.driver.get(MP.url)
        main_page = MP(self.driver)
        order_page = OP(self.driver)
        main_page.wait_header()
        main_page.scroll_mid_order()
        main_page.order_button_mid_wait()
        main_page.order_button_mid_click()

        assert order_page.header_scooter_order_text() == 'Для кого самокат'

    @allure.title('Кнопка "Посмотреть статус"')
    @allure.description('Проверяем наличие кнопки просмотра статуса после оформления заказа')
    def test_order_is_processed(self):
        self.driver.get(MP.url)
        main_page = MP(self.driver)
        order_page = OP(self.driver)
        main_page.wait_header()
        main_page.order_button_above_click()
        order_page.header_scooter_order_wait()
        order_page.set_first_page_order_1()
        order_page.click_next_button()
        order_page.set_second_page_order_1()
        order_page.button_to_order_click()
        order_page.button_yes_click()
        text_button_status = order_page.button_status_text()

        assert text_button_status == 'Посмотреть статус'

    @allure.title('Кнопка "Отменить заказ"')
    @allure.description('Проверяем наличие кнопки отменить заказ и статуса при оформлении заказа')
    def test_page_track_have_button_cancel(self):
        self.driver.get(MP.url)
        main_page = MP(self.driver)
        order_page = OP(self.driver)
        track_page = TP(self.driver)
        main_page.wait_header()
        main_page.order_button_above_click()
        order_page.header_scooter_order_wait()
        order_page.set_first_page_order_1()
        order_page.click_next_button()
        order_page.set_second_page_order_1()
        order_page.button_to_order_click()
        order_page.button_yes_click()
        order_page.button_status_click()
        track_page.cancel_button_wait()
        text_button_cancel = track_page.cancel_button_text()

        assert text_button_cancel == 'Отменить заказ'

    @allure.title('Диалоговое окно "Хотите отменить заказ?"')
    @allure.description('Проверяем наличие диалогового окна Хотите отменить заказ?')
    def test_ask_window_before_cancel_order(self):
        self.driver.get(MP.url)
        main_page = MP(self.driver)
        order_page = OP(self.driver)
        track_page = TP(self.driver)
        main_page.wait_header()
        main_page.scroll_mid_order()
        main_page.order_button_mid_wait()
        main_page.order_button_mid_click()
        order_page.header_scooter_order_wait()
        order_page.set_first_page_order_1()
        order_page.click_next_button()
        order_page.set_second_page_order_1()
        order_page.button_to_order_click()
        order_page.button_yes_click()
        order_page.button_status_click()
        track_page.cancel_button_wait()
        track_page.cancel_button_page_click()
        text_ask_window = track_page.ask_window_text()

        assert text_ask_window.split('\n')[0] == 'Хотите отменить заказ?'

    @allure.title('Отмена заказа')
    @allure.description('Проверяем текст при отмене заказа')
    def test_window_have_text_cancel_order(self):
        self.driver.get(MP.url)
        main_page = MP(self.driver)
        order_page = OP(self.driver)
        track_page = TP(self.driver)
        main_page.wait_header()
        main_page.scroll_mid_order()
        main_page.order_button_mid_wait()
        main_page.order_button_mid_click()
        order_page.header_scooter_order_wait()
        order_page.set_first_page_order_2()
        order_page.click_next_button()
        order_page.set_second_page_order_1()
        order_page.button_to_order_click()
        order_page.button_yes_click()
        order_page.button_status_click()
        track_page.cancel_button_wait()
        track_page.cancel_button_page_click()
        track_page.cancel_button_window_click()
        track_page.cancel_window_wait()
        text_cancel_window = track_page.cancel_window_text()

        assert text_cancel_window.split('\n')[0] == 'Заказ отменён'

    @allure.title('Успешное оформление заказа')
    @allure.description('Проверяем текст диалогового окна при успешном оформлении заказе')
    def test_order_succeed_text(self):
        self.driver.get(MP.url)
        main_page = MP(self.driver)
        order_page = OP(self.driver)
        main_page.wait_header()
        main_page.scroll_mid_order()
        main_page.order_button_mid_wait()
        main_page.order_button_mid_click()
        order_page.header_scooter_order_wait()
        order_page.set_first_page_order_2()
        order_page.click_next_button()
        order_page.set_second_page_order_2()
        order_page.button_to_order_click()
        order_page.button_yes_click()
        text_order = order_page.order_text()

        assert text_order.split('\n')[0] == 'Заказ оформлен'

    @allure.title('Кнопка "Нет" при оформлении заказа')
    @allure.description('Проверяем закрытие окна оформления заказа при нажатии на кнопку "нет"')
    def test_order_button_not_goes_back(self):
        self.driver.get(MP.url)
        main_page = MP(self.driver)
        order_page = OP(self.driver)
        main_page.wait_header()
        main_page.scroll_mid_order()
        main_page.order_button_mid_wait()
        main_page.order_button_mid_click()
        order_page.header_scooter_order_wait()
        order_page.set_first_page_order_2()
        order_page.click_next_button()
        order_page.set_second_page_order_2()
        order_page.button_to_order_click()
        order_page.button_no_click()
        text_header = order_page.header_about_rent_text()

        assert text_header == 'Про аренду'

    @allure.title('Переход на предыдущую страницу при клике на кнопку "назад"')
    @allure.description('Проверяем что работает переход на последнюю страницу при нажатии на кнопку "назад"')
    def test_order_button_back_goes_last_page(self):
        self.driver.get(MP.url)
        main_page = MP(self.driver)
        order_page = OP(self.driver)
        main_page.wait_header()
        main_page.scroll_mid_order()
        main_page.order_button_mid_wait()
        main_page.order_button_mid_click()
        order_page.header_scooter_order_wait()
        order_page.set_first_page_order_2()
        order_page.click_next_button()
        order_page.set_second_page_order_2()
        order_page.button_back_click()
        order_page.header_scooter_order_wait()

        assert order_page.header_scooter_order_text() == 'Для кого самокат'

    @allure.title('Переход на главную по кнопке самоката')
    @allure.description('Проверяем что при нажатии на кнопку Самоката выполняется переход на главную страницу сайта')
    def test_click_scooter_page_goes_main_page(self):
        self.driver.get(MP.url)
        main_page = MP(self.driver)
        order_page = OP(self.driver)
        track_page = TP(self.driver)
        main_page.wait_header()
        main_page.order_button_above_click()
        order_page.header_scooter_order_wait()
        order_page.set_first_page_order_1()
        order_page.click_next_button()
        order_page.set_second_page_order_1()
        order_page.button_to_order_click()
        order_page.button_yes_click()
        order_page.button_status_click()
        track_page.cancel_button_wait()
        main_page.scooter_button_click()
        main_page.wait_header()

        assert main_page.url == 'https://qa-scooter.praktikum-services.ru/'

    @allure.title('Переход на дзен по кнопке Яндекс')
    @allure.description('Проверяем что при нажатии на кнопку Яндекса выполняется переход на сайт дзен')
    def test_click_yandex_page_goes_dzen(self):
        self.driver.get(MP.url)
        main_page = MP(self.driver)
        order_page = OP(self.driver)
        track_page = TP(self.driver)
        main_page.wait_header()
        main_page.order_button_above_click()
        order_page.header_scooter_order_wait()
        order_page.set_first_page_order_1()
        order_page.click_next_button()
        order_page.set_second_page_order_1()
        order_page.button_to_order_click()
        order_page.button_yes_click()
        order_page.button_status_click()
        track_page.cancel_button_wait()
        main_page.yandex_button_click()

        assert main_page.yandex_url == 'https://dzen.ru/?yredirect=true'

    @classmethod
    def teardown_class(cls):
        # закрой браузер
        cls.driver.quit()
