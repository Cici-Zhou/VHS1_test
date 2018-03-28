#coding: utf-8

import os
import sys
base_dir = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
sys.path.append(base_dir)


import time
import unittest
from selenium import webdriver
from selenium.webdriver.common.by import By
from utils.config import Config, DRIVER_PATH, DATA_PATH, REPORT_PATH
from utils.log import logger
from utils.filereader import ExcelReader
from utils.HTMLTestRunner_PY3 import HTMLTestRunner
from page.VHS_landing_page import VHSLandingPage, VHSLoginPage
from page.VHS_UserList_page import VHSUserListpage

class TestVHSlogin(unittest.TestCase):
    URL = Config().get('URL')
    excel = DATA_PATH + '/VHSuser.xlsx'

    def sub_setUp(self):
        #self.driver = webdriver.Chrome(executable_path=DRIVER_PATH + '\chromedriver.exe')
        # 初始页面是main page, 传入浏览器类型打开浏览器
        self.page = VHSLoginPage(browser_type='chrome').get(self.URL, maximize_window=False)
        #self.page2 = VHSLandingPage(browser_type='chrome').get(self.URL, maximize_window=False)        
        #self.driver.get(self.URL)

    def sub_tearDown(self):
        self.page.quit()


    def test_login(self):
        datas = ExcelReader(self.excel).data
        for d in datas:
            with self.subTest(data=d):
                self.sub_setUp()

                self.page.login(d['User'],d['Password'])
                time.sleep(3)
                self.page = VHSLandingPage(self.page)                
                items = self.page.result_links
                time.sleep(2)
                
                for item in items:
                    self.assertIn(d['Message'], item.text)
                    logger.info(item.text)

                self.page = VHSUserListpage(self.page)
                usernames = self.page.UserList
                time.sleep(2)
                for item in usernames:
                    self.assertEqual(d['tablename'], usernames.text)
                self.sub_tearDown()

if __name__ == '__main__':
    #unittest.main()

    testunit = unittest.TestSuite()
    testunit.addTest(TestVHSlogin('test_login'))
    report = REPORT_PATH + '\\report.html'
    fp = open(report, 'wb')
    runner = HTMLTestRunner(stream = fp,title=u'从0搭建测试框架 灰蓝', description='修改HTML报告')
    runner.run(testunit)
    fp.close()

