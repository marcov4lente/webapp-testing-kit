from TestConfig import TestConfig
from selenium import webdriver
from datetime import datetime

class TestConductor(TestConfig):

    def __init__(self):
        super().import_tests()
        self.driver = webdriver.Firefox()


    def run_tests(self):
        test_start_time = datetime.now()
        print('Testing initiating...')

        for test in self.tests:
            print('- Testing: '+test.replace('_', ' ')+'...')
            test_obj = self.tests[test]()
            test_obj.with_driver(self.driver)
            test_obj.with_app_location(self.app_location)
            test_obj.test()
            print('- '+test.replace('_', ' ')+' complete.')

        print('Testing complete.')
        end_start_time = datetime.now()
        print('Test execution time: '+(test_start_time-end_start_time))


