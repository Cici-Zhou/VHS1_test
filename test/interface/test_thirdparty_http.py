import unittest
import os
import sys
base_dir = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
sys.path.append(base_dir)


from utils.config import Config, REPORT_PATH
from utils.client import HTTPClient
from utils.log import logger
from utils.HTMLTestRunner_PY3 import HTMLTestRunner
from utils.assertion import assertHTTPCode


class TestVHSHTTP(unittest.TestCase):
    URL = Config().get('URL')

    def setUp(self):
        self.client = HTTPClient(url=self.URL, method='GET')

    def test_VHS_http(self):
        res = self.client.send()
        logger.debug(res.text)
        assertHTTPCode(res,[200])
        self.assertIn(u'192.168.0.58', res.text)

if __name__ == '__main__':
    testunit = unittest.TestSuite()
    testunit.addTest(TestVHSHTTP('test_VHS_http'))
    report = REPORT_PATH + '\\portreport.html'
    fp = open(report, 'wb')
    runner = HTMLTestRunner(stream=fp, title=u'从0搭建测试框架 灰蓝', description='接口报告')
    runner.run(testunit)
    fp.close()
