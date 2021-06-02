
"""
path1 = os.path.abspath(__file__)
# D:\ningMengClass\py39AutoTest\tools\handle_path.py
print(path1)

path2 = os.path.dirname(path1)
print(path2)

path3 = os.path.dirname(path2)
print(path3)

"""

import os
import time

# os.path.dirname(os.path.abspath(__file__))
base_dir = os.path.dirname(os.path.dirname(__file__))
print(base_dir)

#测试数据路径
case_data_dir = os.path.join(base_dir,'case_data','testCase.xlsx')

#配置文件路径
conf_dir = os.path.join(base_dir,'conf','conf.ini')

# 日志路径配置
log_file_name = time.strftime("%Y%m%d",time.localtime())
log_dir = os.path.join(base_dir,'logs','{}.log'.format(log_file_name))


# 测试报告路径
report_dir = os.path.join(base_dir,'reports')
report_name = time.strftime("%Y%m%d_%H%M%S.html",time.localtime())

