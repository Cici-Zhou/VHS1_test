#-*- coding:utf-8 -*-

import os
import sys
base_dir = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
sys.path.append(base_dir)

from selenium.webdriver.common.by import By
from page.VHS_login_page import VHSLoginPage
from utils.config import DATA_PATH
from utils.filereader import ExcelReader

class VHSLandingPage(VHSLoginPage):
    excel = DATA_PATH + '/VHSuser.xlsx'
    
    @property
    def result_links(self):
        datas = ExcelReader(self.excel).data
        for d in datas:
            message = self.find_elements(*(By.XPATH,d['Locator']))
            return (message)



