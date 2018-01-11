import pytest
from pages import Home, Flight, Fare


@pytest.allure.feature('Transavia')
@pytest.allure.story('Проверка total суммы выбранных билетов. '
                     'Двое взрослых и один ребенок(2-11 age) из Лондона в Париж в обе стороны.'
                     'Выбрать билет с Hold Luggage 20kg.')
@pytest.allure.severity(pytest.allure.severity_level.BLOCKER)
def test_2_total_amount(driver):

    with pytest.allure.step('1. Open "transavia.com" website'):
        home = Home(driver)
        home.open_page()

    with pytest.allure.step('2. Check, that we are on booking page'):
        expected = 'Where do you want to go?'
        assert expected in home.text, 'Text "{}" not found on page: {}'.format(expected, home.text)

    with pytest.allure.step('3. Input "Edinburgh" into "FROM" field'):
        fly_from = 'Edinburgh'
        home.from_enter_text(fly_from)

    with pytest.allure.step('4. Input "Paris" into "TO" field'):
        fly_to = 'Paris'
        home.to_enter_text(fly_to)

    with pytest.allure.step('5. Open "Who will be travelling?" menu'):
        home.open_passengers_menu()

    with pytest.allure.step('6. Add 1 Adult passenger'):
        home.add_adult_passenger()

    with pytest.allure.step('7. Add 1 Children passenger'):
        home.add_children_passenger()

    with pytest.allure.step('8. Enter "Search" button'):
        home.click_search()

    with pytest.allure.step('9. Select available Outbound flight'):
        flight = Flight(driver)
        flight.select_outbound()

    with pytest.allure.step('10. Select available Inbound flight'):
        flight = Flight(driver)
        flight.select_inbound()

    with pytest.allure.step('11. Click "Next"'):
        flight.next()

    with pytest.allure.step('12. Select "Plus" fare'):
        fare = Fare(driver)
        fare.select_plus()

    with pytest.allure.step('13. Check total amount'):
        expected = fare.plus_price_per_person * 3
        actual = fare.total_amount
        err_msg = 'Expected/actual total amount: {}/{}'.format(expected, actual)
        assert expected == actual, err_msg
