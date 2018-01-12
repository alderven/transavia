import allure
from allure_commons.types import AttachmentType
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import Select
import selenium.common.exceptions as exceptions


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
    try:
        element.click()
    except exceptions.WebDriverException:
        driver.execute_script("arguments[0].click();", element)


def find_item_by_text(driver, item_name):
    return driver.find_elements_by_xpath("//*[contains(text(), '{}')]".format(item_name))


def checkbox_state(driver, config):
    return find_element(driver, config).is_selected()


def element_exist(driver, config):
    try:
        find_element(driver, config)
    except exceptions.NoSuchElementException:
        return False
    return True


def enter_text(driver, config, text):
    element = find_element(driver, config)
    element.clear()
    element.send_keys(text)
    element.send_keys(Keys.TAB)


def wait_for_title(driver, title):
    wait = WebDriverWait(driver, TIMEOUT)
    try:
        wait.until(EC.title_is(title))
    except exceptions.TimeoutException:
        assert False, 'Title "{}" not found. TimeoutException'.format(title)


def select_element(driver, config, value_to_select):
    element = find_element(driver, config)
    select = Select(element)
    select.select_by_visible_text(value_to_select)
