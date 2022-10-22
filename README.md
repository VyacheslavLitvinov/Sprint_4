# qa_python_tasks

# Проект автоматизации позитивных сценариев сайта для аренды самокатов
1. Основа для написания автотестов — фреймворк pytest.
2. Установить зависимости — pip install -r requirements.txt.
3. Команда для запуска — pytest -v. 

# Проверяемые кейсы:
1. test_faq - тест кнопок с вопросами на главной странице
2. test_ordering - тест основного функционала при оформлении заказа
    # test_top_order_button_open_page - переход на страницу заказа по верхней кнопке
    # test_mid_order_button_open_page - переход на страницу заказа по центральной кнопке
    # test_order_is_processed - наличие кнопки просмотра статуса после оформления заказа
    # test_page_track_have_button_cancel - проверка статуса при оформлении заказа
    # test_ask_window_before_cancel_order - открытие сообщения Хотите отменить заказ?
    # test_window_have_text_cancel_order - текст с успешной отменой заказа
    # test_order_succeed_text - текст с успешным оформлением заказа
    # test_order_button_not_goes_back - закрытие окна с сообщением при нажатии на кнопку "нет"
    # test_order_button_back_goes_last_page - работает переход на последнюю страницу при нажатии на кнопку "назад"
    # test_click_scooter_page_goes_main_page - при нажатии на кнопку Самоката выполняется переход на главную страницу
    # test_click_yandex_page_goes_dzen - при нажатии на кнопку Яндекса выполняется переход на сайт дзен