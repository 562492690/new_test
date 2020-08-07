# coding:utf-8

from selenium.webdriver.common.by import By

from test_wechat.addMember import AddMember
from test_wechat.base_page import BasePage
from test_wechat.importContacts import ImportContacts


class AddressBook(BasePage):
    '''
    通讯录页 po
    '''
    # _base_url = 'https://work.weixin.qq.com/wework_admin/frame#contacts'

    def add_member_condition(self,ele1_class,ele2_class):
        elements = len(self.finds(By.CSS_SELECTOR, ele1_class))
        if elements <= 0:
            self.find(By.CSS_SELECTOR, ele2_class).click()
        return elements > 0

    def goto_addMember(self):
        '''
        进入添加成员页面 po
        :return:
        '''

        def add_member_condition(x):
            elements = len(self.finds(By.CSS_SELECTOR,'#username'))
            if elements <= 0:
                self.find(By.CSS_SELECTOR, '.js_has_member .qui_btn.ww_btn.js_add_member').click()
            return elements > 0

        self.find(By.CSS_SELECTOR, '#menu_contacts').click()
        self.wait_for_conditions(add_member_condition)
        return AddMember(self._driver)

    def goto_ImportContacts(self):
        '''
        1.首页>点击通讯录页面点击批量导入
        2.点击文件导入
        :return:
        '''
        self.find(By.CSS_SELECTOR, '#menu_contacts').click()
        self.find(By.CSS_SELECTOR, '.js_has_member .ww_btn_PartDropdown_left').click()
        self.find(By.CSS_SELECTOR, '.js_has_member .qui_dropdownMenu_itemLink.ww_dropdownMenu_itemLink.js_import_member').click()
        return ImportContacts(self._driver)


