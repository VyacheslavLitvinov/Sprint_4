import allure
import pytest
from pages.locators_main_page import MainPage as MP
from pages.locators_order_page import OrderPage as OP
from pages.locators_track_page import TrackPage as TP


class TestOrderPage:

    @allure.title('Верхняя кнопка заказа на главной')
    @allure.description('Проверяем что работает переход на страницу заказа по верхней кнопке')
    def test_top_order_button_open_page(self, driver):
        main_page = MP(driver)
        main_page.site()
        order_page = OP(driver)
        main_page.wait_header()
        main_page.order_button_above_click()
        order_page.header_scooter_order_wait()

        assert order_page.header_scooter_order_text() == 'Для кого самокат'

    @allure.title('Центральная кнопка заказа на главной')
    @allure.description('Проверяем что работает переход на страницу заказа по центральной кнопке')
    def test_mid_order_button_open_page(self, driver):
        main_page = MP(driver)
        main_page.site()
        order_page = OP(driver)
        main_page.wait_header()
        main_page.scroll_mid_order()
        main_page.order_button_mid_wait()
        main_page.order_button_mid_click()

        assert order_page.header_scooter_order_text() == 'Для кого самокат'

    @allure.title('Кнопка "Посмотреть статус"')
    @allure.description('Проверяем наличие кнопки просмотра статуса после оформления заказа')
    @pytest.mark.parametrize("name, surname, phone, address, subway, date, days_lease, color_number, comment",
                             [('Андрей', 'Теймуровский', '+7999555000', 'Москва', 'Тёплый Стан', '31.12.2022', 3, 1,
                               'Очень надеюсь, что в этот раз будет без косяков')])
    def test_order_is_processed(self, driver, name, surname, phone, address, subway, date, days_lease, color_number, comment):
        main_page = MP(driver)
        main_page.site()
        order_page = OP(driver)
        main_page.wait_header()
        main_page.click_cookie()
        main_page.order_button_above_click()
        order_page.header_scooter_order_wait()
        order_page.set_first_page_order(name=name, surname=surname, phone=phone, address=address, subway=subway)
        order_page.click_next_button()
        order_page.set_second_page_order(date=date, days_lease=days_lease, color_number=color_number, comment=comment)
        order_page.button_to_order_click()
        order_page.wait_button_yes()
        order_page.button_yes_click()
        order_page.wait_button_status()

        text_button_status = order_page.button_status_text()

        assert text_button_status == 'Посмотреть статус'

    @allure.title('Кнопка "Отменить заказ"')
    @allure.description('Проверяем наличие кнопки отменить заказ и статуса при оформлении заказа')
    @pytest.mark.parametrize("name, surname, phone, address, subway, date, days_lease, color_number, comment",
                             [('Имя', 'Фамилия', '89999999999', 'Город', 'Бульвар Адмирала Ушакова', '17.11.2022', 6, 1,
                               'Спасибо')])
    def test_page_track_have_button_cancel(self, driver, name, surname, phone, address, subway, date, days_lease, color_number, comment):
        main_page = MP(driver)
        main_page.site()
        order_page = OP(driver)
        track_page = TP(driver)
        main_page.wait_header()
        main_page.click_cookie()
        main_page.order_button_above_click()
        order_page.header_scooter_order_wait()
        order_page.set_first_page_order(name=name, surname=surname, phone=phone, address=address, subway=subway)
        order_page.click_next_button()
        order_page.set_second_page_order(date=date, days_lease=days_lease, color_number=color_number, comment=comment)
        order_page.button_to_order_click()
        order_page.button_yes_click()
        order_page.button_status_click()
        track_page.cancel_button_wait()
        text_button_cancel = track_page.cancel_button_text()

        assert text_button_cancel == 'Отменить заказ'

    @allure.title('Диалоговое окно "Хотите отменить заказ?"')
    @allure.description('Проверяем наличие диалогового окна Хотите отменить заказ?')
    @pytest.mark.parametrize("name, surname, phone, address, subway, date, days_lease, color_number, comment",
                             [('Пётр', 'Первый', '00000000000', 'Санк-Петербург', 'Ленинский проспект', '01.01.2022', 0, 0,
                               '')])
    def test_ask_window_before_cancel_order(self, driver, name, surname, phone, address, subway, date, days_lease, color_number, comment):
        main_page = MP(driver)
        main_page.site()
        order_page = OP(driver)
        track_page = TP(driver)
        main_page.wait_header()
        main_page.click_cookie()
        main_page.scroll_mid_order()
        main_page.order_button_mid_wait()
        main_page.order_button_mid_click()
        order_page.header_scooter_order_wait()
        order_page.set_first_page_order(name=name, surname=surname, phone=phone, address=address, subway=subway)
        order_page.click_next_button()
        order_page.set_second_page_order(date=date, days_lease=days_lease, color_number=color_number, comment=comment)
        order_page.button_to_order_click()
        order_page.button_yes_click()
        order_page.button_status_click()
        track_page.cancel_button_wait()
        track_page.cancel_button_page_click()
        text_ask_window = track_page.ask_window_text()

        assert text_ask_window.split('\n')[0] == 'Хотите отменить заказ?'

    @allure.title('Отмена заказа')
    @allure.description('Проверяем текст при отмене заказа')
    @pytest.mark.parametrize("name, surname, phone, address, subway, date, days_lease, color_number, comment",
                             [('Геннадий', 'Прудовский', '2131231312312', 'Вашингтон', 'Площадь Революции', '11.11.2022', 5, 1,
                               'КОММЕНТАРИЙ')])
    def test_window_have_text_cancel_order(self, driver, name, surname, phone, address, subway, date, days_lease, color_number, comment):
        main_page = MP(driver)
        main_page.site()
        order_page = OP(driver)
        track_page = TP(driver)
        main_page.wait_header()
        main_page.click_cookie()
        main_page.scroll_mid_order()
        main_page.order_button_mid_wait()
        main_page.order_button_mid_click()
        order_page.header_scooter_order_wait()
        order_page.set_first_page_order(name=name, surname=surname, phone=phone, address=address, subway=subway)
        order_page.click_next_button()
        order_page.set_second_page_order(date=date, days_lease=days_lease, color_number=color_number, comment=comment)
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
    @pytest.mark.parametrize("name, surname, phone, address, subway, date, days_lease, color_number, comment",
                             [('Иванов', 'ВИван', '89995551122', 'Калининград', 'Спартак', '29.10.2022', 3, 1,
                               'Проблеме религиозных взглядов Петра Ильича Чайковского в настоящее время посвящена '
                               'обширная научная литература. Кандидат искусствоведения Ольга Захарова относила её '
                               '«к числу трудных и вызывающих в музыковедении прямо противоположные по своей '
                               'направленности ответы». Если современники не придавали большого значения религиозным '
                               'взглядам Петра Чайковского, а в советское время композитора однозначно относили к '
                               'материалистам, то в современной музыковедческой литературе появилось большое число '
                               'научных работ, которые, отталкиваясь от документальных свидетельств, по-разному '
                               'трактуют характер взглядов Чайковского на религию. ')])
    def test_order_succeed_text(self, driver, name, surname, phone, address, subway, date, days_lease, color_number, comment):
        main_page = MP(driver)
        main_page.site()
        order_page = OP(driver)
        main_page.wait_header()
        main_page.click_cookie()
        main_page.scroll_mid_order()
        main_page.order_button_mid_wait()
        main_page.order_button_mid_click()
        order_page.header_scooter_order_wait()
        order_page.set_first_page_order(name=name, surname=surname, phone=phone, address=address, subway=subway)
        order_page.click_next_button()
        order_page.set_second_page_order(date=date, days_lease=days_lease, color_number=color_number, comment=comment)
        order_page.button_to_order_click()
        order_page.button_yes_click()
        order_page.wait_order_text()
        text_order = order_page.order_text()

        assert text_order.split('\n')[0] == 'Заказ оформлен'

    @allure.title('Кнопка "Нет" при оформлении заказа')
    @allure.description('Проверяем закрытие окна оформления заказа при нажатии на кнопку "нет"')
    @allure.title('Успешное оформление заказа')
    @allure.description('Проверяем текст диалогового окна при успешном оформлении заказе')
    @pytest.mark.parametrize("name, surname, phone, address, subway, date, days_lease, color_number, comment",
                             [('Вильгельм', 'Прусский', '89995551122', 'Гамбург', 'ВДНХ', '29.10.2022', 0, 0,
                               'Я подумаю до завтра')])
    def test_order_button_not_goes_back(self, driver, name, surname, phone, address, subway, date, days_lease, color_number, comment):
        main_page = MP(driver)
        main_page.site()
        order_page = OP(driver)
        main_page.wait_header()
        main_page.click_cookie()
        main_page.scroll_mid_order()
        main_page.order_button_mid_wait()
        main_page.order_button_mid_click()
        order_page.header_scooter_order_wait()
        order_page.set_first_page_order(name=name, surname=surname, phone=phone, address=address, subway=subway)
        order_page.click_next_button()
        order_page.set_second_page_order(date=date, days_lease=days_lease, color_number=color_number, comment=comment)
        order_page.button_to_order_click()
        order_page.button_no_click()
        text_header = order_page.header_about_rent_text()

        assert text_header == 'Про аренду'

    @allure.title('Переход на предыдущую страницу при клике на кнопку "назад"')
    @allure.description('Проверяем что работает переход на последнюю страницу при нажатии на кнопку "назад"')
    @pytest.mark.parametrize("name, surname, phone, address, subway, date, days_lease, color_number, comment",
                             [('Вильгельмина', 'Прусская', '89995551122', 'Гамбург', 'ВДНХ', '29.10.2022', 1, 0,
                               'Буду ждать в черной шляпе в сером плаще, с милым корги')])
    def test_order_button_back_goes_last_page(self, driver, name, surname, phone, address, subway, date, days_lease, color_number, comment):
        main_page = MP(driver)
        main_page.site()
        order_page = OP(driver)
        main_page.wait_header()
        main_page.click_cookie()
        main_page.scroll_mid_order()
        main_page.order_button_mid_wait()
        main_page.order_button_mid_click()
        order_page.header_scooter_order_wait()
        order_page.set_first_page_order(name=name, surname=surname, phone=phone, address=address, subway=subway)
        order_page.click_next_button()
        order_page.set_second_page_order(date=date, days_lease=days_lease, color_number=color_number, comment=comment)
        order_page.button_back_click()
        order_page.header_scooter_order_wait()

        assert order_page.header_scooter_order_text() == 'Для кого самокат'

    @allure.title('Переход на главную по кнопке самоката')
    @allure.description('Проверяем что при нажатии на кнопку Самоката выполняется переход на главную страницу сайта')
    @pytest.mark.parametrize("name, surname, phone, address, subway, date, days_lease, color_number, comment",
                             [('Алиса', 'Яндекс', '89990000000', 'Станция', 'Алма-Атинская', '13.11.2022', 2, 0,
                               'Али́са — виртуальный голосовой помощник, созданный компанией Яндекс')])
    def test_click_scooter_page_goes_main_page(self, driver, name, surname, phone, address, subway, date, days_lease, color_number, comment):
        main_page = MP(driver)
        main_page.site()
        order_page = OP(driver)
        track_page = TP(driver)
        main_page.wait_header()
        main_page.click_cookie()
        main_page.order_button_above_click()
        order_page.header_scooter_order_wait()
        order_page.set_first_page_order(name=name, surname=surname, phone=phone, address=address, subway=subway)
        order_page.click_next_button()
        order_page.set_second_page_order(date=date, days_lease=days_lease, color_number=color_number, comment=comment)
        order_page.button_to_order_click()
        order_page.button_yes_click()
        order_page.button_status_click()
        track_page.cancel_button_wait()
        main_page.scooter_button_click()
        main_page.wait_header()

        assert main_page.url == 'https://qa-scooter.praktikum-services.ru/'

    @allure.title('Переход на дзен по кнопке Яндекс')
    @allure.description('Проверяем что при нажатии на кнопку Яндекса выполняется переход на сайт дзен')
    @pytest.mark.parametrize("name, surname, phone, address, subway, date, days_lease, color_number, comment",
                             [('Вильгельмина', 'Прусская', '89995551122', 'Гамбург', 'ВДНХ', '29.10.2022', 4, 0,
                               'Буду ждать в черной шляпе в сером плаще, с милым корги')])
    def test_click_yandex_page_goes_dzen(self, driver, name, surname, phone, address, subway, date, days_lease, color_number, comment):
        main_page = MP(driver)
        main_page.site()
        order_page = OP(driver)
        track_page = TP(driver)
        main_page.wait_header()
        main_page.click_cookie()
        main_page.order_button_above_click()
        order_page.header_scooter_order_wait()
        order_page.set_first_page_order(name=name, surname=surname, phone=phone, address=address, subway=subway)
        order_page.click_next_button()
        order_page.set_second_page_order(date=date, days_lease=days_lease, color_number=color_number, comment=comment)
        order_page.button_to_order_click()
        order_page.button_yes_click()
        order_page.button_status_click()
        track_page.cancel_button_wait()
        main_page.yandex_button_click()

        assert main_page.yandex_url == 'https://dzen.ru/?yredirect=true'
