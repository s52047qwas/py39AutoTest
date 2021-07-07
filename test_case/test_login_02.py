

#from ddt import ddt,data,unpack
import unittest
import ast
# import traceback

import pytest

import os
import sys
rootpath=str('/var/jenkins_home/workspace/py_auto39')
syspath=sys.path
sys.path=[]
sys.path.append(rootpath)#将工程根目录加入到python搜索路径中
sys.path.extend([rootpath+i for i in os.listdir(rootpath) if i[0]!="."])#将工程目录下的一级目录添加到python搜索路径中
sys.path.extend(syspath)

from tools.handle_excel import HandleExcel
from tools.handle_path import case_data_dir
from tools.handle_ini import conf
# from tools.handle_request import SendRequest
# from tools.handle_phone import HandlePhone
# from tools.handle_db import mysql
# from tools.handle_check_db_data import CheckDb
# from tools.handle_replace import HandleReplace
from tools.handle_attribute import HandleAttribute

#获取测试用例
case_list = HandleExcel(file_path=case_data_dir,sheet_name=conf.get('sheet','name')).get_case_data_dict()
print('这里是从excel获取的测试用例')
print(case_list)
#实例化业务逻辑

@pytest.mark.usefixtures('init1')
class TestDemo():

    @pytest.mark.parametrize('case',case_list)
    def test_register(self,case,init1):
        print(case)
        send_request, handle_phone, MYSQL_TEST, handle_replace = init1
        new_request_data = handle_replace.replace_request_data(request_data=case["data"],replace_request_data=case["replace_request_data"])


        # 数据库校验sql替换
        if case["check_db"]:
            if "#mobile_phone#" in case["check_db"]:
                check_db = case["check_db"].replace("#mobile_phone#", getattr(HandleAttribute,"mobile_phone"))
            else:
                check_db = case["check_db"]
        else:
            check_db = None

        # 2、发起请求
        response = send_request.send_request(method=case["method"],url=case["url"],data=new_request_data)
        # 3、获取token，依赖参数

        #  4、响应参数替换
        actual_data = {'code': response['code'], 'msg': response['msg']}
        # 5、响应断言
        assert ast.literal_eval(case['expected_data'])==actual_data

        # 6、数据库校验
        MYSQL_TEST.check_db(check_db=check_db)
        # check_db.check_db(check_db=check_db)


if __name__ == '__main__':
    pytest.main(["-s","-v","test_case2.py","--html=report1.html", "--alluredir=allure1_files"])