from faker import Faker
from tools.handle_db import mysql
import ast
from pprint import pprint
from tools.handle_excel import HandleExcel
from tools.handle_loging import my_logger
from tools.handle_path import case_data_dir
from tools.handle_ini import conf


class SendPhone:
    def __init__(self):
        self.fk = Faker(locale='zh-CN')


    #随机生成手机号码
    def faker_phone(self):
        phone = self.fk.phone_number()
        return phone


    #获取数据库查询结果
    def select_phone(self,phone):
        sql = "select * from member where mobile_phone = {}".format(phone)
        result = mysql.get_all_data(sql=sql)
        return result

    #获取未注册的手机号
    def get_phone(self):
        while True:
            phone = self.faker_phone()
            result = self.select_phone(phone=phone)

            if result:
                my_logger.info('手机号已注册：{}'.format(phone))
                continue
            else:
                my_logger.info('手机号未注册，可使用：{}'.format(phone))
                return phone


    # def set_phone(self,Phone):
    #     excel_data = '{"mobile_phone":"#mobile#","pwd":"Aa123456"}'
    #     rustel = ast.literal_eval(excel_data)
    #     rustel['mobile_phone'] = Phone
    #     print(rustel)
    #
    # def test_1(self):
    #     while True:
    #         phone = self.faker_phone()
    #         a =self.handledb.select_phone(phone)
    #         print(a)
    #         result, cur, conn = a
    #
    #         print('返回数据长度：', len(result))
    #         if result:
    #             continue
    #         else:
    #             cur.close()
    #             conn.close()
    #             return phone


if __name__ == '__main__':
    a=SendPhone()
    a.get_phone()