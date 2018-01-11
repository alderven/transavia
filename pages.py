import os
import time
import configparser
import selenium_methods

CONFIG = 'config.cfg'
SLEEP = 5


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

    def from_enter_text(self, text):
        selenium_methods.enter_text(self.driver, self.config['HOME']['FROM'], text)

    def to_enter_text(self, text):
        selenium_methods.enter_text(self.driver, self.config['HOME']['TO'], text)

    def click_return_on(self):
        selenium_methods.click(self.driver, self.config['HOME']['RETURN_ON'])

    def click_search(self):
        selenium_methods.click(self.driver, self.config['HOME']['SEARCH'])

    def open_passengers_menu(self):
        selenium_methods.click(self.driver, self.config['HOME']['PASSENGERS'])

    def add_adult_passenger(self):
        selenium_methods.click(self.driver, self.config['HOME']['ADD_ADULT'])

    def add_children_passenger(self):
        selenium_methods.click(self.driver, self.config['HOME']['ADD_CHILDREN'])

    def click_manage_your_booking(self):
        selenium_methods.click(self.driver, self.config['HOME']['MANAGE_YOUR_BOOKING'])

    def click_view_your_booking(self):
        selenium_methods.click(self.driver, self.config['HOME']['VIEW_YOUR_BOOKING'])

    def click_add_multiple_destinations(self):
        selenium_methods.click(self.driver, self.config['HOME']['ADD_MULTIPLE_DESTINATIONS'])


class Flight(Base):

    @property
    def flight_available(self):
        return selenium_methods.element_exist(self.driver, self.config['FLIGHT']['PRICE'])

    @property
    def error_message(self):
        return selenium_methods.find_element(self.driver, self.config['FLIGHT']['ERROR']).text

    def select_outbound(self):
        time.sleep(SLEEP)
        selenium_methods.click(self.driver, self.config['FLIGHT']['OUTBOUND_CHOOSE'])
        selenium_methods.click(self.driver, self.config['FLIGHT']['OUTBOUND_SELECT'])

    def select_inbound(self):
        selenium_methods.click(self.driver, self.config['FLIGHT']['INBOUND_CHOOSE'])
        selenium_methods.click(self.driver, self.config['FLIGHT']['INBOUND_SELECT'])

    def next(self):
        time.sleep(SLEEP)
        selenium_methods.click(self.driver, self.config['FLIGHT']['NEXT'])


class Login(Base):

    def wait_for_title(self, title):
        selenium_methods.wait_for_title(self.driver, title)

    @property
    def title(self):
        return self.driver.current_url

    def enter_booking_number(self, booking_number):
        selenium_methods.enter_text(self.driver, self.config['LOGIN']['BOOKING_NUMBER'], booking_number)

    def enter_last_name(self, last_name):
        selenium_methods.enter_text(self.driver, self.config['LOGIN']['LAST_NAME'], last_name)

    def enter_flight_date(self, flight_date):
        selenium_methods.enter_text(self.driver, self.config['LOGIN']['FLIGHT_DATE'], flight_date)

    def click_view_booking(self):
        selenium_methods.click(self.driver, self.config['LOGIN']['VIEW_BOOKING'])


class Fare(Base):

    @property
    def plus_price_per_person(self):
        element = selenium_methods.find_element(self.driver, self.config['FARE']['PLUS_PRICE_PER_PERSON']).text
        return int(''.join(filter(str.isdigit, element)))

    @property
    def total_amount(self):
        time.sleep(SLEEP)
        element = selenium_methods.find_element(self.driver, self.config['FARE']['TOTAL_AMOUNT']).text
        return int(''.join(filter(str.isdigit, element))) / 100  # make price without cents

    def select_plus(self):
        time.sleep(SLEEP)
        selenium_methods.click(self.driver, self.config['FARE']['PLUS'])


class MultipleDestinations(Base):

    @property
    def total_amount(self):
        time.sleep(SLEEP)
        element = selenium_methods.find_element(self.driver, self.config['MULTIPLE_DESTINATIONS']['TOTAL_AMOUNT']).text
        return int(''.join(filter(str.isdigit, element))) / 100  # make price without cents

    def input_outbound_from(self, text):
        selenium_methods.enter_text(self.driver, self.config['MULTIPLE_DESTINATIONS']['OUTBOUND_FROM'], text)

    def input_outbound_to(self, text):
        selenium_methods.enter_text(self.driver, self.config['MULTIPLE_DESTINATIONS']['OUTBOUND_TO'], text)

    def input_outbound_date(self, date):
        selenium_methods.enter_text(self.driver, self.config['MULTIPLE_DESTINATIONS']['OUTBOUND_DATE'], date)

    def click_select_outbound(self):
        time.sleep(SLEEP)
        selenium_methods.click(self.driver, self.config['MULTIPLE_DESTINATIONS']['OUTBOUND_SELECT'])

    def input_inbound_from(self, text):
        selenium_methods.enter_text(self.driver, self.config['MULTIPLE_DESTINATIONS']['INBOUND_FROM'], text)

    def input_inbound_to(self, text):
        selenium_methods.enter_text(self.driver, self.config['MULTIPLE_DESTINATIONS']['INBOUND_TO'], text)

    def input_inbound_date(self, date):
        selenium_methods.enter_text(self.driver, self.config['MULTIPLE_DESTINATIONS']['INBOUND_DATE'], date)

    def click_select_inbound(self):
        time.sleep(SLEEP)
        selenium_methods.click(self.driver, self.config['MULTIPLE_DESTINATIONS']['INBOUND_SELECT'])

    def click_search(self):
        selenium_methods.click(self.driver, self.config['MULTIPLE_DESTINATIONS']['SEARCH'])
