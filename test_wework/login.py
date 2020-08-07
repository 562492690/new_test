# coding:utf-8
from selenium.webdriver.common.by import By
from selenium.webdriver.remote.webdriver import WebDriver

from test_wework.register import Register


class Login:
    '''
    登录页面 po
    '''

    def __init__(self, driver: WebDriver):
        self.driver = driver

    def scan(self):
        '''
        扫描二维码
        :return:
        '''
        pass

    def goto_register(self):
        '''
        1.点击企业注册
        2.进入到注册 po
        :return:
        '''
        self.driver.find_element(By.CSS_SELECTOR, '.login_registerBar_link').click()
        return Register(self.driver)