#-*- coding:utf-8 -*-

import os
import sys
base_dir = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
sys.path.append(base_dir)


from selenium.webdriver.common.by import By
from page.VHS_login_page import VHSLoginPage
from utils.config import DATA_PATH
from utils.filereader import ExcelReader

class VHSUserListpage(VHSLoginPage):
    excel = DATA_PATH + '/VHAddUser.xlsx'

    locator_SystemManager = (By.XPATH, '//ul[@id="leftul"]/li[1]')
    locator_AgentList = (By.XPATH,'//ul[@class="zi"]/li[1]')
    locator_Username = (By.XPATH,'//div[@id="divValue"]/tr/td[1]')
    


    @property
    def UserList(self):
        self.find_element(*self.locator_SystemManager).click()
        self.find_element(*self.locator_AgentList).click()
        s = self.find_elements(*self.locator_Username)
        return (s)
        
        


    
    

    
