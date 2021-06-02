# -*- coding: utf-8 -*-
# @Time    : 27/5/2021 下午 9:41
# @Author  : 海励
# @File    : main.py


import os
import unittest
from BeautifulReport import BeautifulReport

from tools.handle_path import report_dir,report_name
from unittestreport import TestRunner

# BeautifulReport 生成测试报告
dir_path = os.path.dirname(__file__)
suite = unittest.defaultTestLoader.discover(start_dir=dir_path,pattern='test_register.py')

br = BeautifulReport(suites=suite)

br.report(description='py39期DDT学习',report_dir=report_dir,filename=report_name)

#unittestreport 生成测试报告
# dir_path = os.path.dirname(__file__)
#
# suite = unittest.defaultTestLoader.discover(start_dir=dir_path,pattern='case_ddt.py')
# runner = TestRunner(
#                  suite=suite,
#                  filename="py39_report_88.html",
#                  title='py39测试报告',
#                  tester='py39海励',
#                  desc="py39项目测试生成的报告",
#                  templates=1
# )
# runner.run()


