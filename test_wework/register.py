# coding:utf-8
from selenium.webdriver.common.by import By
from selenium.webdriver.remote.webdriver import WebDriver


class Register:
    '''
    注册 po
    '''
    def __init__(self, driver: WebDriver):
        self.driver = driver

    def register(self):

        '''
        1.填入信息
        2.点击同意
        3.点击注册
        :return:
        '''

        self.driver.find_element(By.CSS_SELECTOR, '#corp_name').send_keys('name')
        self.driver.find_element(By.CSS_SELECTOR, '#manager_name').send_keys('liverpool')
        return True
