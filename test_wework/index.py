# coding:utf-8

from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By
from test_wework.login import Login
from test_wework.register import Register


class Index:
    '''
    首页的 po
    '''

    def __init__(self):
        '''
            1.cmd执行chrome --remote-debugging-port=9222，打开调试端口，
            2.selenium Options.debugger_address='127.0.0.1:9222'
            :return:
        '''
        # option = Options()
        # option.debugger_address = '127.0.0.1:9222'
        self.driver = webdriver.Chrome()
        self.driver.get('https://work.weixin.qq.com/')

    def goto_register(self):
        '''
        1.点击立即注册
        2.进入到注册 po
        :return:
        '''
        self.driver.find_element(By.CSS_SELECTOR, '.index_head_info_pCDownloadBtn').click()
        return Register(self.driver)

    def goto_login(self):
        '''
        1.点击企业登录
        2.进入企业登录 po
        :return:
        '''
        self.driver.find_element(By.CSS_SELECTOR, '.index_top_operation_loginBtn').click()
        return Login(self.driver)



