import allure
from selenium import webdriver
from locators_main_page import MainPage as MP


class TestFAQ:
    driver = None

    @classmethod
    def setup_class(cls):
        cls.driver = webdriver.Firefox()

    @allure.title('Кнопка "Сколько это стоит? И как оплатить?"')
    @allure.description('Проверяем что при клике на первый вопрос отображается нужный текст ответа')
    def test_faq_button_1(self):
        self.driver.get(MP.url)
        main_page = MP(self.driver)
        main_page.wait_header()
        main_page.scroll_faq()
        main_page.wait_button_faq_1()
        main_page.click_button_faq_1()
        main_page.wait_answer_faq_1()
        assert main_page.find_answer_faq_1() == 'Сутки — 400 рублей. Оплата курьеру — наличными или картой.'

    @allure.title('Кнопка "Хочу сразу несколько самокатов! Так можно?"')
    @allure.description('Проверяем что при клике на второй вопрос отображается нужный текст ответа')
    def test_faq_button_2(self):
        self.driver.get(MP.url)
        main_page = MP(self.driver)
        main_page.wait_header()
        main_page.scroll_faq()
        main_page.wait_button_faq_2()
        main_page.click_button_faq_2()
        main_page.wait_answer_faq_2()
        assert main_page.find_answer_faq_2() == 'Пока что у нас так: один заказ — один самокат. ' \
                                                'Если хотите покататься с друзьями, можете просто сделать несколько заказов — один за другим.'

    @allure.title('Кнопка "Как рассчитывается время аренды?"')
    @allure.description('Проверяем что при клике на третий вопрос отображается нужный текст ответа')
    def test_faq_button_3(self):
        self.driver.get(MP.url)
        main_page = MP(self.driver)
        main_page.wait_header()
        main_page.scroll_faq()
        main_page.wait_button_faq_3()
        main_page.click_button_faq_3()
        main_page.wait_answer_faq_3()
        assert main_page.find_answer_faq_3() == 'Допустим, вы оформляете заказ на 8 мая. Мы привозим самокат 8 мая в течение дня. ' \
                                                'Отсчёт времени аренды начинается с момента, когда вы оплатите заказ курьеру. ' \
                                                'Если мы привезли самокат 8 мая в 20:30, суточная аренда закончится 9 мая в 20:30.'

    @allure.title('Кнопка "Можно ли заказать самокат прямо на сегодня?"')
    @allure.description('Проверяем что при клике на четвертый вопрос отображается нужный текст ответа')
    def test_faq_button_4(self):
        self.driver.get(MP.url)
        main_page = MP(self.driver)
        main_page.wait_header()
        main_page.scroll_faq()
        main_page.wait_button_faq_4()
        main_page.click_button_faq_4()
        main_page.wait_answer_faq_4()
        assert main_page.find_answer_faq_4() == 'Только начиная с завтрашнего дня. Но скоро станем расторопнее.'

    @allure.title('Кнопка "Можно ли продлить заказ или вернуть самокат раньше?"')
    @allure.description('Проверяем что при клике на пятый вопрос отображается нужный текст ответа')
    def test_faq_button_5(self):
        self.driver.get(MP.url)
        main_page = MP(self.driver)
        main_page.wait_header()
        main_page.scroll_faq()
        main_page.wait_button_faq_5()
        main_page.click_button_faq_5()
        main_page.wait_answer_faq_5()
        assert main_page.find_answer_faq_5() == 'Пока что нет! Но если что-то срочное — всегда можно позвонить в поддержку по красивому номеру 1010.'

    @allure.title('Кнопка "Вы привозите зарядку вместе с самокатом?"')
    @allure.description('Проверяем что при клике на шестой вопрос отображается нужный текст ответа')
    def test_faq_button_6(self):
        self.driver.get(MP.url)
        main_page = MP(self.driver)
        main_page.wait_header()
        main_page.scroll_faq()
        main_page.wait_button_faq_6()
        main_page.click_button_faq_6()
        main_page.wait_answer_faq_6()
        assert main_page.find_answer_faq_6() == 'Самокат приезжает к вам с полной зарядкой. ' \
                                                'Этого хватает на восемь суток — даже если будете кататься без передышек и во сне. Зарядка не понадобится.'

    @allure.title('Кнопка "Можно ли отменить заказ?"')
    @allure.description('Проверяем что при клике на седьмой вопрос отображается нужный текст ответа')
    def test_faq_button_7(self):
        self.driver.get(MP.url)
        main_page = MP(self.driver)
        main_page.wait_header()
        main_page.scroll_faq()
        main_page.wait_button_faq_7()
        main_page.click_button_faq_7()
        main_page.wait_answer_faq_7()
        assert main_page.find_answer_faq_7() == 'Да, пока самокат не привезли. Штрафа не будет, объяснительной записки тоже не попросим. Все же свои.'

    @allure.title('Кнопка "Я жизу за МКАДом, привезёте?"')
    @allure.description('Проверяем что при клике на восьмой вопрос отображается нужный текст ответа')
    def test_faq_button_8(self):
        self.driver.get(MP.url)
        main_page = MP(self.driver)
        main_page.wait_header()
        main_page.scroll_faq()
        main_page.wait_button_faq_8()
        main_page.click_button_faq_8()
        main_page.wait_answer_faq_8()
        assert main_page.find_answer_faq_8() == 'Да, обязательно. Всем самокатов! И Москве, и Московской области.'

    @classmethod
    def teardown_class(cls):
        # закрой браузер
        cls.driver.quit()
