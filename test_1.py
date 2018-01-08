import pytest
from pages import Home, Flight


@pytest.allure.feature('Transavia')
@pytest.allure.story('Заполнение поля "Where do you want to go?" для выбора одиночного перелета на одну персону в одну сторону')
@pytest.allure.severity(pytest.allure.severity_level.BLOCKER)
def test_1(driver):

    with pytest.allure.step('1. Открываем страничку "Where do you want to go?"'):
        home = Home(driver)
        home.open_page()

    with pytest.allure.step('2. Проверяем, что мы находимся на страничке "Where do you want to go?"'):
        expected = 'Where do you want to go?'
        assert expected in home.text, 'Текст "{}" не найден на странице: {}'.format(expected, home.text)

    with pytest.allure.step('3. Кликаем на поле "FROM"'):
        home.click_from()

    with pytest.allure.step('4. Проверяем, что появляется выпадающий список с названиями доступных мест для перелета в поле "FROM"'):
        expected = 'Edinburgh, United Kingdom'
        assert expected in home.text, 'Текст "{}" не найден на странице: {}'.format(expected, home.text)

    with pytest.allure.step('5. Выбираем "{}" из списка "FROM"'.format(expected)):
        home.select_from(expected)

    with pytest.allure.step('6. Кликаем на поле "TO"'):
        home.click_to()

    with pytest.allure.step('7. Проверяем, что появляется выпадающий список с названием доступных мест в поле "TO"'):
        expected = 'Paris (Orly South), France'
        assert expected in home.text, 'Текст "{}" не найден на странице: {}'.format(expected, home.text)

    with pytest.allure.step('8. Выбираем "{}" из списка "TO"'.format(expected)):
        home.select_to(expected)

    with pytest.allure.step('9. Переводим checkbox "Return on" в состояние unchecked'):
        home.click_return_on()

    with pytest.allure.step('10. Проверяем, что checkbox "Return on" в состоянии unchecked'):
        checkbox_state = home.return_on
        assert checkbox_state is False, 'Checkbox "Return on" в состоянии {}. Ожидается состояние: False (unchecked)'.format(checkbox_state)

    with pytest.allure.step('11. Нажимаем кнопку "Search"'):
        home.click_search()

    with pytest.allure.step('12. Проверяем, что найден хотя бы один рейс в период от 1 до 7 дней'):
        flight = Flight(driver)
        assert flight.flight_available, 'Ни один рейс не найден за период от 1 до 7 дней'
