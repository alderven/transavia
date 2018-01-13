import pytest
from pages import Home, MultipleDestinations


@pytest.allure.feature('Transavia')
@pytest.allure.story('Complicated route "Bologna-Eindhoven" (1st date) and "Amsterdam-Casablanca" (2nd date)')
@pytest.allure.severity(pytest.allure.severity_level.BLOCKER)
def test_9_complicated_route(driver):

    with pytest.allure.step('1 Open "transavia.com" website'):
        home = Home(driver)
        home.open_page()

    with pytest.allure.step('2. Check, that we are on booking page'):
        expected = 'Where do you want to go?'
        assert expected in home.text, 'Text "{}" not found on page: {}'.format(expected, home.text)

    with pytest.allure.step('3. Click "Add multiple destinations"'):
        home.click_add_multiple_destinations()

    with pytest.allure.step('4. Input "Bologna, Italy" into "Outbound flight" - "From" field'):
        md = MultipleDestinations(driver)
        md.input_outbound_from('Bologna, Italy')

    with pytest.allure.step('5. Input "Eindhoven, Netherlands" into "Outbound flight" - "To" field'):
        md.input_outbound_to('Eindhoven, Netherlands')

    with pytest.allure.step('6. Input outbound flight date'):
        md.input_outbound_date('12 Apr 2018')

    with pytest.allure.step('7. Input "Amsterdam (Schiphol), Netherlands" into "Inbound flight" - "From" field'):
        md.input_inbound_from('Amsterdam (Schiphol), Netherlands')

    with pytest.allure.step('8. Input "Casablanca, Morocco" into "Inbound flight" - "To" field'):
        md.input_inbound_to('Casablanca, Morocco')

    with pytest.allure.step('9. Input inbound flight date'):
        md.input_inbound_date('13 Apr 2018')

    with pytest.allure.step('10. Click "Search" button'):
        md.click_search()

    with pytest.allure.step('11. Click "Select" outbound flight'):
        md.click_select_outbound()

    with pytest.allure.step('12. Click "Select" inbound flight'):
        md.click_select_inbound()

    with pytest.allure.step('13. Check total amount'):
        expected = 116
        assert expected == md.total_amount, 'Expected/Actual total amount: {}/{}'.format(expected, md.total_amount)

    pass
