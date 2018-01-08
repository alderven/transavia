import allure
from allure_commons.types import AttachmentType
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By
from selenium.common.exceptions import NoSuchElementException

TIMEOUT = 30
DELIMITER = ','


def main(driver, ec, config):
    locator_type, locator = config.split(DELIMITER)
    locator_type = eval('By.' + locator_type)
    element = WebDriverWait(driver, TIMEOUT).until(ec((locator_type, locator)))
    allure.attach(driver.get_screenshot_as_png(), name='Screenshot', attachment_type=AttachmentType.PNG)
    return element


def find_element(driver, config):
    element = main(driver, EC.presence_of_element_located, config)
    return element


def click(driver, config):
    element = find_element(driver, config)
    element.click()


def find_item_by_text(driver, item_name):
    return driver.find_elements_by_xpath("//*[contains(text(), '{}')]".format(item_name))


def checkbox_state(driver, config):
    return find_element(driver, config).is_selected()


def element_exist(driver, config):
    try:
        find_element(driver, config)
    except NoSuchElementException:
        return False
    return True
