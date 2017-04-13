import time
import os
import os.path
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import NoSuchElementException
from selenium.common.exceptions import NoSuchElementException

class Test(object):

    def __init__(self): pass

    def with_driver(self, driver):
        self.driver = driver
        return self


    def with_keys(self, keys):
        self.keys = keys
        return self


    def with_app_location(self, app_location):
        self.app_location = app_location
        return self


    def assert_on_page(self, string):
        try:
            assert string in self.driver.page_source
        except AssertionError:
            print('--- ERROR: '+string+' not in '+self.driver.current_url+' page source.')


    def assert_not_on_page(self, string):
        try:
            assert string not in self.driver.page_source
        except AssertionError:
            print('--- ERROR: '+string+' in '+self.driver.current_url+' page source.')


    def input(self, element_id, input_data):
        try:
            field = self.driver.find_element_by_id(element_id)
            field.send_keys(input_data)
        except NoSuchElementException:
            print('--- ERROR: could not select input element '+element_id+'.')


    def input_file(self, element_id, input_data):
        try:
            file_path = os.path.join(os.getcwd(),'resources',input_data)
            field = self.driver.find_element_by_id(element_id)
            field.send_keys(file_path)
        except NoSuchElementException:
            print('--- ERROR: could not select element '+element_id+'.')


    def input_select(self, element_id):
        try:
            select = self.driver.find_element_by_id(element_id)
            for option in select.find_elements_by_tag_name('option'):
                option.click()
        except NoSuchElementException:
            print('--- ERROR: could not select element '+element_id+'.')


    def press(self, element_id):
        try:
            button = self.driver.find_element_by_id(element_id)
            button.click()
        except NoSuchElementException:
            print('--- ERROR: could not select element '+element_id+'.')


    def wait_for_page_to_load(self):
        time.sleep(8)


