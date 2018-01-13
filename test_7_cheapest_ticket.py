import pytest
from pages import Home, AdvancedSearch


@pytest.allure.feature('Transavia')
@pytest.allure.story('Find cheapest ticket for Netherlands-France destination for specific month and day')
@pytest.allure.severity(pytest.allure.severity_level.MINOR)
def test_7_cheapest_ticket(driver):

    with pytest.allure.step('1. Open "transavia.com" website'):
        home = Home(driver)
        home.open_page()

    with pytest.allure.step('2. Check, that we are on booking page'):
        expected = 'Where do you want to go?'
        assert expected in home.text, 'Text "{}" not found on page: {}'.format(expected, home.text)

    with pytest.allure.step('3. Click "Plain and book"'):
        home.click_plain_and_book()

    with pytest.allure.step('4. Click "Advanced search"'):
        home.click_advanced_search()

    with pytest.allure.step('5. Input "Netherlands" into "FROM" field'):
        advanced = AdvancedSearch(driver)
        advanced.from_enter_text('Netherlands')

    with pytest.allure.step('6. Input "France" into "TO" field'):
        advanced.to_enter_text('France')

    with pytest.allure.step('7. Click "When will you be taking off?"'):
        advanced.click_when_will_you_be_taking_off()

    with pytest.allure.step('8. Select "Single flight"'):
        advanced.select_flight_type('Single flight')

    with pytest.allure.step('9. Select "August 2018" in "Specific month"'):
        advanced.select_specific_month('August 2018')

    with pytest.allure.step('10. Select "Sunday" in the "Day of the week"'):
        advanced.select_day_of_the_week('Sunday')

    with pytest.allure.step('11. Click "Search" button'):
        advanced.search()

    with pytest.allure.step('12. Get Price and City name from the first row of the table "We found the following destinations for you"'):
        price, city = advanced.get_price_and_city()
        price_expected = 32
        city_expected = 'Nice'
        assert price_expected == price, 'Price expected/actual: {}/{}'.format(price_expected, price)
        assert city_expected == city, 'City expected/actual: {}/{}'.format(city_expected, city)
