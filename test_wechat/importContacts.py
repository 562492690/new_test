from selenium.webdriver.common.by import By

from test_wechat.base_page import BasePage


class ImportContacts(BasePage):
    '''
    批量导入通讯录 po
    '''

    def importContacts(self):
        '''
        1.点击上传文件
        2.上传文件用send_keys
        :return:
        '''
        self.find(By.CSS_SELECTOR, 'input.qui_btn.ww_btn.ww_fileInputWrap').send_keys('E:/通讯录批量导入.xlsx')
        self.wait_for_click((By.CSS_SELECTOR, '#submit_csv'))
        self.find(By.CSS_SELECTOR, '#submit_csv').click()