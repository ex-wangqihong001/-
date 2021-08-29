'''
@Project:Test_ecshop
@Time:2021/8/28 10:35
@Author:Xiaowang
'''

import unittest
import time
import os
import logging
from test_runner.html_test_runner import  HTMLTestRunner


# 主程序

# 获取项目的根目录
test_dir = os.path.join(os.getcwd())
# print(test_dir)

# 自动搜索项目根目录下的所有case，构建测试集；返回TestSuite对象
discover = unittest.defaultTestLoader.discover(test_dir,pattern='test_*.py')

# 实例化TextTestRunner类
# runner = unittest.TextTestRunner(verbosity=2)

now = time.strftime('%Y-%m-%d %H_%M_%S')    #获取到当前日期
# print(now)
result = test_dir + '\\result\\' + now + '_result.html'     #这里个人感觉可以优化下
# D:\接口自动化测试\lotto\result\2021-08-28 10:47:34_result.html
# print(result)
log =  test_dir + '\\result\\' + now + '_log.txt'
# print(log)

#filename 日志文件路径 level 日志的级别 format 格式
logging.basicConfig(filename=log,level=logging.INFO,filemode="w",format = '%(asctime)s - %(name)s - %(levelname)s - %(message)s')

# 写入方式wb
fp = open(result,'wb')

#构造runner

runner = HTMLTestRunner(stream=fp, title='接口自动化测试报告', description='aguest_master项目用例执行情况',verbosity=2)


# 使用run()方法运行测试套件（即运行测试套件中的所有用例）
runner.run(discover)

