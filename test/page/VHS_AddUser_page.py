#-*- coding:utf-8 -*-

import os
import sys

base_dir = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
sys.path.append(base_dir)

from slenium.webdriver.common.by import By
from page.VHS_login_page import VHSLoginPage
from utils.config import DATA_PATH
from utils.filereader import ExcelReader

class VHSAddUserPage(VHSLoginPage):
    excel = DATA_PATH + '/VHAddUser.xlsx'
    
    locator_AddUser = (By.XPATH,'//input[@value="AddUser"]')
    locator_FirstName = (By.ID, 'afn')
    locator_LastName = (By.ID, 'aln')
    locator_Phone = (By.ID, 'ap')
    locator_AreaCode = (By.ID, 'aac')


    def AddUser(self,usr):
        self.driver.find_element(*self.locator_AddUser).click()
        self.driver.find_element(*self.locator_FirstName).clear()
        self.driver.find_element(*self.locator_firstName).send_keys(usr)

