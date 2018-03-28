#-*- coding:utf-8 -*-

import os
import sys
base_dir = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
sys.path.append(base_dir)

from selenium.webdriver.common.by import By
from common.Page import Page
from selenium.webdriver.support.select import Select

class VHSLoginPage(Page):
    locator_username = (By.ID, 'txtUserName')
    locator_password = (By.ID, 'txtPassword')
    #locator_language = (By.ID, 'dropLanguage')
    locator_loginButton = (By.ID, 'btnLogin')

    def login(self,usr,pws):
        """搜索功能"""
        self.find_element(*self.locator_username).clear()
        self.find_element(*self.locator_username).send_keys(usr)
        self.find_element(*self.locator_password).clear()
        self.find_element(*self.locator_password).send_keys(pws)
        #s = self.driver.find_element(*self.locator_language)
        #Select(s).select_by_index(2)
        self.find_element(*self.locator_loginButton).click()
