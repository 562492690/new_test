from selenium.webdriver.common.by import By
from test_wechat.addMember import AddMember
from test_wechat.base_page import BasePage
from test_wechat.importContacts import ImportContacts


class Index(BasePage):
    '''
    登录后首页 po
    '''
    _base_url = 'https://work.weixin.qq.com/wework_admin/frame#index'

    def goto_addMember(self):
        '''
        1.首页点击添加成员
        2.进入添加成员页面
        :return:
        '''
        self.find(By.CSS_SELECTOR, '.ww_indexImg_AddMember').click()
        return AddMember(self._driver)
    def goto_importContacts(self):
        '''
        点击导入通讯录
        进入导入通讯录页面 po
        :return:
        '''
        self.find(By.CSS_SELECTOR, '.index_service_cnt.js_service_list>a:nth-child(2)>div').click()
        return ImportContacts(self._driver)