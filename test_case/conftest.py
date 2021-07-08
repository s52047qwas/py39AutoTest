import os
import sys
rootpath=str('/var/jenkins_home/workspace/py_auto39')
syspath=sys.path
sys.path=[]
sys.path.append(rootpath)#将工程根目录加入到python搜索路径中
sys.path.extend([rootpath+i for i in os.listdir(rootpath) if i[0]!="."])#将工程目录下的一级目录添加到python搜索路径中
sys.path.extend(syspath)
import pytest
from tools.handle_request import SendRequest
from tools.handle_phone import HandlePhone
from tools.handle_db import mysql
from tools.handle_check_db_data import CheckDb
from tools.handel_replace import HandleReplace
from tools.handle_attribute import HandleAttribute


@pytest.fixture(scope='class')
def init1():
    send_request = SendRequest()
    handle_phone = HandlePhone()
    MYSQL_TEST = CheckDb()
    handle_replace = HandleReplace()
    yield send_request,handle_phone,MYSQL_TEST,handle_replace
    mysql.close()