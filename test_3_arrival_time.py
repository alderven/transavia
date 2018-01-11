import pytest
from pages import Home, Login


@pytest.allure.feature('Transavia')
@pytest.allure.story('Зайти в кабинет и проверить ожидаемое и фактическое время приземления самолета')
@pytest.allure.severity(pytest.allure.severity_level.BLOCKER)
def test_3_arrival_time(driver):

    with pytest.allure.step('1. Open "transavia.com" website'):
        home = Home(driver)
        home.open_page()

    with pytest.allure.step('2. Check, that we are on booking page'):
        expected = 'Where do you want to go?'
        assert expected in home.text, 'Text "{}" not found on page: {}'.format(expected, home.text)

    with pytest.allure.step('3. Click "Manage your booking" button'):
        home.click_manage_your_booking()

    with pytest.allure.step('4. Click "View your booking" button'):
        home.click_view_your_booking()

    with pytest.allure.step('5. Check, that we are on Login Page'):
        title = 'Log in'
        login = Login(driver)
        login.wait_for_title(title)

    with pytest.allure.step('6. Enter booking no. "MF8C9R"; last name "kukharau", flight date "9 June 2016"'):
        login.enter_booking_number('MF8C9R')
        login.enter_last_name('kukharau')
        login.enter_flight_date('9 June 2016')
        login.click_view_booking()

    with pytest.allure.step('7. Check, that login was successful'):
        title = 'Account overview'
        login = Login(driver)
        login.wait_for_title(title)

    with pytest.allure.step('8. Get arrival time'):
        pass  # unable to proceed due to invalid credentials
