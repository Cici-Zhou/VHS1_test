#-*- coding:utf-8 -*-

"""
用例不是一次请求就OK了的，而是多个请求复合的，我们第二个请求可能会用到第一个请求
返回值中的数据，这就要我们再次进行封装，做一个抽取器，从结果中抽取部分信息
抽取器，从相应结果中抽取部分数据
"""

import json
import jmespath

import os
import sys
base_dir = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
sys.path.append(base_dir)




class JMESPathExtractor(object):
    """
    用JMESPath实现的抽取器，对于json格式数据实现简单方法的抽取。
    """
    def extract(self, query=None, body=None):
        try:
            return jmespath.search(query, json.loads(body))
        except Exception as e:
            raise ValueError("Invalid query: " + query + ":" + str(e))


if __name__ == '__main__':
    from utils.client import HTTPClient
    res = HTTPClient(url='http://wthrcdn.etouch.cn/weather_mini?citykey=101010100').send()
    print(res.text)

    j = JMESPathExtractor()
    j_1 = j.extract(query='data.forecast[1].date', body=res.text)
    j_2 = j.extract(query='data.ganmao', body=res.text)
    print(j_1, j_2)

    

    
