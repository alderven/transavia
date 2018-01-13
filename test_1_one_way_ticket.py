import pytest
from pages import Home, Flight


@pytest.allure.feature('Transavia')
@pytest.allure.story('One way ticket')
@pytest.allure.severity(pytest.allure.severity_level.BLOCKER)
def test_1_one_way_ticket(driver):

    with pytest.allure.step('1. Open "transavia.com" website'):
        home = Home(driver)
        home.open_page()

    with pytest.allure.step('2. Check, that we are on booking page'):
        expected = 'Where do you want to go?'
        assert expected in home.text, 'Text "{}" not found on page: {}'.format(expected, home.text)

    with pytest.allure.step('3. Click "FROM" field'):
        home.click_from()

    with pytest.allure.step('4. Check, that drop down list with appears'):
        expected = 'Edinburgh, United Kingdom'
        assert expected in home.text, 'Text "{}" not found on page: {}'.format(expected, home.text)

    with pytest.allure.step('5. Select "{}" from the "FROM" list'.format(expected)):
        home.select_from(expected)

    with pytest.allure.step('6. Click "TO" field'):
        home.click_to()

    with pytest.allure.step('7. Check, that drop down list with destinations appears'):
        expected = 'Paris (Orly South), France'
        assert expected in home.text, 'Text "{}" not found on page: {}'.format(expected, home.text)

    with pytest.allure.step('8. Select "{}" from the "TO" list'.format(expected)):
        home.select_to(expected)

    with pytest.allure.step('9. Uncheck "Return on" checkbox'):
        home.click_return_on()

    with pytest.allure.step('10. Check, that "Return on" unchecked'):
        checkbox_state = home.return_on
        assert checkbox_state is False, 'Expected/actual "Return on" state is "False" (unchecked)/"{}"'.format(checkbox_state)

    with pytest.allure.step('11. Press "Search" button'):
        home.click_search()

    with pytest.allure.step('12. Check, that there is at least one flight avaiable in the periof from 1 to 7 days'):
        flight = Flight(driver)
        assert flight.flight_available, 'No flights are found in the period from 1 to 7 days'
