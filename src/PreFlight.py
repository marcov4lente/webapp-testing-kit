import importlib

class PreFlight():

    def __check_system_dependencies(self):
        selenium = importlib.util.find_spec('time')
        if selenium is None:
            print('Dependency error: time not found, please ensure it\'s installed before trying again')
            exit()


    def __check_selenium_dependencies(self):
        selenium = importlib.util.find_spec('selenium')
        if selenium is None:
            print('Dependency error: selenium not found, please ensure it\'s installed before trying again')
            exit()

        selenium = importlib.util.find_spec('selenium.webdriver.support.ui')
        if selenium is None:
            print('Dependency error: selenium.webdriver.support.ui not found, please ensure it\'s installed before trying again')
            exit()

        selenium = importlib.util.find_spec('selenium.webdriver.support')
        if selenium is None:
            print('Dependency error: selenium.webdriver.support not found, please ensure it\'s installed before trying again')
            exit()

        selenium = importlib.util.find_spec('selenium.common.exceptions')
        if selenium is None:
            print('Dependency error: selenium.common.exceptions not found, please ensure it\'s installed before trying again')
            exit()

        selenium = importlib.util.find_spec('selenium.webdriver.common.keys')
        if selenium is None:
            print('Dependency error: selenium.webdriver.common.keys not found, please ensure it\'s installed before trying again')
            exit()


    def check(self):
        self.__check_system_dependencies()
        self.__check_selenium_dependencies()
