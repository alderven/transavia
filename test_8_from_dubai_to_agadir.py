import pytest
from pages import Home, Flight


@pytest.allure.feature('Transavia')
@pytest.allure.story('Найти рейсы из Dubai в Agadir, Morocco')
@pytest.allure.severity(pytest.allure.severity_level.BLOCKER)
def test_8_from_dubai_to_agadir(driver):

    with pytest.allure.step('1 Open "transavia.com" website'):
        home = Home(driver)
        home.open_page()

    with pytest.allure.step('2. Check, that we are on booking page'):
        expected = 'Where do you want to go?'
        assert expected in home.text, 'Text "{}" not found on page: {}'.format(expected, home.text)

    with pytest.allure.step('3. Input "Dubai" into "FROM" field'):
        fly_from = 'Dubai'
        home.from_enter_text(fly_from)

    with pytest.allure.step('4. Input "Agadir, Morocco" into "TO" field'):
        fly_to = 'Agadir, Morocco'
        home.to_enter_text(fly_to)

    with pytest.allure.step('5. Enter "Search" button'):
        home.click_search()

    with pytest.allure.step('6. Verify error message'):
        flight = Flight(driver)
        expected = 'Unfortunately we do not fly from Dubai, United Arab Emirates to Agadir, Morocco. ' \
                   'However, we do fly from Dubai, United Arab Emirates to other destinations. ' \
                   'Please change your destination and try again.'
        assert expected == flight.error_message, 'Error expected/actual: "{}"/"{}"'.format(expected, flight.error_message)
