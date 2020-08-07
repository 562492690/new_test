from selenium.webdriver.common.by import By
from test_wechat.base_page import BasePage

class AddMember(BasePage):
    '''
    添加成员
    '''

    def add_Member(self):
        self.find(By.CSS_SELECTOR, '#username').send_keys('hello_')
        self.find(By.CSS_SELECTOR, '#memberAdd_acctid').send_keys('real')
        self.find(By.CSS_SELECTOR, '#memberAdd_phone').send_keys('13562656551')
        self.find(By.CSS_SELECTOR, '.qui_btn.ww_btn.js_btn_save').click()
