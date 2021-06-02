
import os
import unittest
from BeautifulReport import BeautifulReport

from tools.handle_path import report_dir,report_name


# BeautifulReport 生成测试报告
dir_path = os.path.dirname(__file__)
suite = unittest.defaultTestLoader.discover(start_dir=dir_path,pattern='test_register.py')

br = BeautifulReport(suites=suite)

br.report(description='py39期DDT学习',report_dir=report_dir,filename=report_name)



