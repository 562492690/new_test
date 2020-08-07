from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.chrome.webdriver import WebDriver
from selenium.webdriver.support import expected_conditions
from selenium.webdriver.support.wait import WebDriverWait


class BasePage:
    _driver = None
    _base_url=''

    def __init__(self,driver: WebDriver = None):
        '''
            1.cmd执行chrome --remote-debugging-port=9222，打开调试端口，
            2.selenium Options.debugger_address='127.0.0.1:9222'
            :return:
        '''
        if driver is None:
            option = Options()
            option.debugger_address = '127.0.0.1:9222'
            self._driver = webdriver.Chrome(options=option)
            self._driver.implicitly_wait(3)

        else:
            self._driver = driver

        if self._base_url != '':
            self._driver.get(self._base_url)

    def find(self,by,locator):
        return self._driver.find_element(by, locator)

    def finds(self,by,locator):
        return self._driver.find_elements(by,locator)

    def wait_for_click(self,locator):
        WebDriverWait(self._driver,10).until(expected_conditions.element_to_be_clickable(locator))

    def wait_for_conditions(self,condition):
        WebDriverWait(self._driver, 10).until(condition)

