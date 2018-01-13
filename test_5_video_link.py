import pytest
from pages import Home, HandLuggage, YouTube


@pytest.allure.feature('Transavia')
@pytest.allure.story('Check Name and Author for "Handluggage" video instruction')
@pytest.allure.severity(pytest.allure.severity_level.MINOR)
def test_5_video_link(driver):

    with pytest.allure.step('1. Open "transavia.com" website'):
        home = Home(driver)
        home.open_page()

    with pytest.allure.step('2. Check, that we are on booking page'):
        expected = 'Where do you want to go?'
        assert expected in home.text, 'Text "{}" not found on page: {}'.format(expected, home.text)

    with pytest.allure.step('3. Click "Service"'):
        home.click_service()

    with pytest.allure.step('4. Click "Handluggage"'):
        home.click_hand_luggage()

    with pytest.allure.step('5. Go to "Hand luggage tips" section'):
        hl = HandLuggage(driver)
        hl.click_tips()

    with pytest.allure.step('6. Get the video link and open it'):

        you_tube = YouTube(driver)
        you_tube.open_video_page(hl.video_link)

    with pytest.allure.step('8. Check video Name and Author'):
        author_expected = 'Transavia'
        name_expected = 'Luggage'
        assert you_tube.author == author_expected, 'Author expected/actual: {}/{}'.format(author_expected, you_tube.author)
        assert you_tube.name == name_expected, 'Name expected/actual: {}/{}'.format(name_expected, you_tube.author)
