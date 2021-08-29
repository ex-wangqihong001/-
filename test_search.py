'''
@Project:Test_ecshop
@Time:2021/8/28 15:47
@Author:Xiaowang
'''

# 查询中奖结果
import requests
import unittest
import logging
class  Test_lotto_dlt(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        cls.url1 = 'http://apis.juhe.cn//lottery/bonus'
    @classmethod
    def tearDownclass(cls):
        pass

    def setUp(self):
        pass
    def tearDown(self):
        pass
    def test01(self):
        '''lottery_id为大乐透'''
        params = {
            'key':'098da4754ea96454b65b83464f342ebe',
            'lottery_id':'dlt',
            'lottery_res':'01,07,21,30,35@08,11',
            'lottery_no':'21089'
        }

        r = requests.get(url=self.url1,params=params)
        # r = r.json()['error_code']
        reason = r.json()['reason']
        logging.info('case:{}\n请求地址：{.url}\t请求方式：{.request.method}\n响应头：{.headers}\n响应正文{.text}'.format(reason,r,r,r,r))

if __name__ == '__main__':
    unittest.main(verbosity=2)



