import unittest
import ast
import traceback
from unittestreport import ddt,list_data


from tools.handle_loging import my_logger

from tools.handle_excel import HandleExcel
from tools.handle_path import case_data_dir
from tools.handle_ini import conf
from tools.handle_request import SendRequest
from tools.handle_phone import SendPhone
from tools.handle_db import mysql
from tools.handle_check_db_data import CheckDb
from tools.handel_replace import HandleReplace
from tools.handle_attribute import HandleAttribute

#获取测试用例
case_list = HandleExcel(file_path=case_data_dir,sheet_name=conf.get('sheet','name')).get_case_data_dict()
print('这里是从excel获取的测试用例')
print(case_list)
#实例化业务逻辑

@ddt
class TestDemo(unittest.TestCase):

    @classmethod
    def setUpClass(cls) -> None:
        cls.send_request = SendRequest()
        cls.send_phone = SendPhone()
        cls.checkdb = CheckDb()
        cls.handle_replace = HandleReplace()

    @classmethod
    def tearDownClass(cls) -> None:
        mysql.close()

    @list_data(case_list)
    def test_register(self,case):

        my_logger.info(msg=case['data'])

        # 替换数据
        if '#mobile#' in case['data']:
            #拿到未注册手机号
            my_logger.info(msg='需要替换')
            phone = self.send_phone.get_phone()
            request_data = case['data'].replace('#mobile#',phone)
        else:
            request_data = case['data']
            my_logger.info(msg='不需要替换')
            phone =None



        ##数据库校验sql替换
        if case['check_db']:
            if '#mobile#' in case['check_db']:
                check_db = case['check_db'].replace('#mobile#',getattr(HandleAttribute,'mobile'))
                my_logger.info(msg='数据库校验语句：{}'.format(check_db))

            else:
                check_db = case['check_db']
                my_logger.info(msg='数据库校验语句：{}'.format(check_db))

        else:
            check_db = None
            my_logger.info(msg='数据库无需替换')


        #发起请求
        response = self.send_request.send_request(method=case["method"],url=case['url'],data=ast.literal_eval(request_data))

        # 获取响应结果
        actual_data = {'code': response['code'], 'msg': response['msg']}
        #响应断言
        self.assertEqual(first=ast.literal_eval(case['expected_data']),second=actual_data)

        #数据库校验
        self.checkdb.check_db(check_db=check_db)



if __name__ == '__main__':
    unittest.main()