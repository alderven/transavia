import os
import pytest
from selenium import webdriver

DRIVER_EXE = 'MicrosoftWebDriver.exe'


@pytest.yield_fixture(scope='function')
def driver():

    # Launch Driver
    web_driver_full_path = os.path.join(os.path.dirname(os.path.abspath(__file__)), DRIVER_EXE)
    web_driver = webdriver.Edge(web_driver_full_path)
    web_driver.maximize_window()

    # Pass Driver instance to test
    yield web_driver

    # Quit Driver
    web_driver.quit()
