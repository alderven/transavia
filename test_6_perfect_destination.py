import pytest
from pages import Home, Destinations, AdvancedSearch


@pytest.allure.feature('Transavia')
@pytest.allure.story('Find the perfect destination from "Innsbruck, Austria" with budget less than 200 euro')
@pytest.allure.severity(pytest.allure.severity_level.MINOR)
def test_6_perfect_destination(driver):

    with pytest.allure.step('1. Open "transavia.com" website'):
        home = Home(driver)
        home.open_page()

    with pytest.allure.step('2. Check, that we are on booking page'):
        expected = 'Where do you want to go?'
        assert expected in home.text, 'Text "{}" not found on page: {}'.format(expected, home.text)

    with pytest.allure.step('3. Click "Destinations"'):
        home.click_destinations()

    with pytest.allure.step('4. Click "Find the perfect destination"'):
        destinations = Destinations(driver)
        destinations.find_destination()

    with pytest.allure.step('5. Input "Innsbruck, Austria" into "FROM" field'):
        advanced = AdvancedSearch(driver)
        advanced.from_enter_text('Innsbruck, Austria')

    with pytest.allure.step('6. Click button "What is your budget per person?"'):
        advanced.click_what_is_your_budget()

    with pytest.allure.step('7. input "200" into field "My budget"'):
        advanced.input_budget(200)

    with pytest.allure.step('8. Click "Search" button'):
        advanced.search()

    with pytest.allure.step('9. Check search results'):
        result = advanced.get_search_results()
        assert result, 'Search results not found!'
        pytest.allure.step('Search result: {}'.format(result))
