from faker import Faker
from tools.handle_db import mysql
import ast
from pprint import pprint
from tools.handle_excel import HandleExcel
from tools.handle_loging import my_logger
from tools.handle_path import case_data_dir
from tools.handle_ini import conf


from faker import Faker
from tools.handle_db import mysql

class HandlePhone:
    def __init__(self):
        self.fk = Faker(locale='zh-cn')

    # 如果系统对手机号前缀有要求的，要做前缀校验
    def __faker_phone(self):
        phone = self.fk.phone_number()
        print('生成的手机号：',phone)
        return phone

    # 获取数据库查询结果 [{}，{}，{}]
    def __select_phone(self,phone):
        sql = "select * from member where mobile_phone = '{}'".format(phone)
        result = mysql.get_db_all_data(sql=sql)
        return result

    # 获取未注册的手机号
    def get_phone(self):
        while True:
            phone = self.__faker_phone() # 随机生成手机号
            result = self.__select_phone(phone) # 拿到数据库执行结果
            if len(result) >0:
                continue
            else:
                return phone

if __name__ == '__main__':
    cl = HandlePhone()
    result = cl.get_phone()
    print(result)