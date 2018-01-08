import os
import configparser
import selenium_methods

CONFIG = 'config.cfg'


class Base(object):

    def __init__(self, driver):
        self.driver = driver

    @property
    def config(self):
        cfg = configparser.ConfigParser()
        cfg_path = os.path.join(os.path.dirname(os.path.abspath(__file__)), CONFIG)
        cfg.read(cfg_path)
        return cfg


class Home(Base):

    def open_page(self):
        return self.driver.get(self.config['SITE']['URL'])

    @property
    def text(self):
        return self.driver.page_source

    @property
    def return_on(self):
        return selenium_methods.checkbox_state(self.driver, self.config['HOME']['RETURN_ON'])

    @property
    def flight_available(self):
        return None

    def click_from(self):
        selenium_methods.click(self.driver, self.config['HOME']['FROM'])

    def click_to(self):
        selenium_methods.click(self.driver, self.config['HOME']['TO'])

    def select_from(self, item_name):
        elements = selenium_methods.find_item_by_text(self.driver, item_name)
        elements[1].click()

    def select_to(self, item_name):
        elements = selenium_methods.find_item_by_text(self.driver, item_name)
        elements[2].click()

    def click_return_on(self):
        element = selenium_methods.find_element(self.driver, self.config['HOME']['RETURN_ON'])
        self.driver.execute_script("arguments[0].click();", element)

    def click_search(self):
        selenium_methods.click(self.driver, self.config['HOME']['SEARCH'])


class Flight(Base):

    @property
    def flight_available(self):
        return selenium_methods.element_exist(self.driver, self.config['FLIGHT']['PRICE'])
