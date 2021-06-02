# -*- coding: utf-8 -*-
# @Time    : 13/5/2021 下午 8:21
# @Author  : 海励
# @File    : test_case.py
from ddt import ddt,data,unpack
import unittest
import ast

from tools.handle_excel import HandleExcel
#from login import LoginCase

#获取测试用例
case_list = HandleExcel(file_path='testCase.xlsx',sheet_name='sheet1',).get_case_data_dict()
print('这里是从excel获取的测试用例')
print(case_list)
#实例化业务逻辑
login = LoginCase()
@ddt
class TestDemo(unittest.TestCase):
    #初始化函数，后置清理函数都可以不写，因为我们没有前置条件，也没有后置清理
    @data(*case_list)
    def test_login(self,case):
        """测试用例"""
        print('这里是测试用例传进来的参数')
        print(case)
        #业务逻辑
        response = login.user_login(url=case['url'],data=ast.literal_eval(case['data']))
        # 获取响应结果
        actual_data = {'code': response['code'], 'msg': response['msg']}
        #断言
        self.assertEqual(first=ast.literal_eval(case['expected_data']),second=actual_data)



# for i  in  case_list:
#     def test_login(i):
#         pass




