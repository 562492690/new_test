# coding:utf-8
import time

from selenium import webdriver
from selenium.webdriver import TouchActions
from selenium.webdriver.common.by import By


class Test_TouchAction():

    def setup(self):
        # option=webdriver.ChromeOptions()
        # option.add_experimental_option('w3c', False)
        # self.driver=webdriver.Chrome(options=option)
        self.driver=webdriver.Chrome()
        self.driver.implicitly_wait(5)
        self.driver.maximize_window()
        self.action=TouchActions(self.driver)

    def teardown(self):
        self.driver.quit()

    def test_TouchAction(self):
        self.driver.get('https://www.baidu.com')
        self.driver.find_element(By.CSS_SELECTOR, '#kw').send_keys('selenium测试')
        click_elememnt=self.driver.find_element(By.CSS_SELECTOR, '#su')

        self.action.tap(click_elememnt).perform()
        self.action.scroll_from_element(click_elememnt,0,10000)
        self.action.perform()



