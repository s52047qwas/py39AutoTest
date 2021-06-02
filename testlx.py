from faker import Faker
from pprint import pprint

from tools.handle_excel import HandleExcel
from tools.handle_path import case_data_dir
from tools.handle_ini import conf
fk = Faker(locale='zh-CN')

print(fk.name())


print(fk.phone_number())

excel = HandleExcel(case_data_dir,conf.get(section='sheet',option='name'))

pprint(excel.get_case_data_dict())
