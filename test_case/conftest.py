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