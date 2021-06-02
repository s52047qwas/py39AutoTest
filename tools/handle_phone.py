from faker import Faker
from tools.handle_db import HandleDB
import ast
from pprint import pprint
from tools.handle_excel import HandleExcel
from tools.handle_loging import my_logger
from tools.handle_path import case_data_dir
from tools.handle_ini import conf


class SendPhone:
    def __init__(self):
        self.fk = Faker(locale='zh-CN')
        self.handledb = HandleDB()


    #随机生成手机号码
    def faker_phone(self):
        phone = self.fk.phone_number()
        print('生成的手机号：',phone)
        return phone

    ##检查号码是否存在
    def check_phone(self):
        while True:
            phone = self.faker_phone()
            result = self.handledb.select_phone(phone)
            if result:
                continue
            else:
                return phone


    def set_phone(self,Phone):
        excel_data = '{"mobile_phone":#mobile#,"pwd":"Aa123456"}'
        rustel = ast.literal_eval(excel_data)
        rustel['mobile_phone'] = Phone
        print(rustel)

    def test_1(self):
        name = HandleExcel(file_path=case_data_dir,sheet_name=conf.get(section='sheet',option='name')).get_case_data_dict()
        for i in name:
            pprint(i['data'])

if __name__ == '__main__':
    a=SendPhone()
    a.test_1()