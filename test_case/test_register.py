
# from ddt import ddt,data,unpack
import unittest
import ast
import traceback
from unittestreport import ddt,list_data

from tools.handle_excel import HandleExcel
from tools.handle_path import case_data_dir
from tools.handle_ini import conf
from tools.handle_request import SendRequest

#获取测试用例
case_list = HandleExcel(file_path=case_data_dir,sheet_name=conf.get('sheet','name')).get_case_data_dict()
print('这里是从excel获取的测试用例')
print(case_list)
#实例化业务逻辑

@ddt
class TestDemo(unittest.TestCase):

    @classmethod
    def setUpClass(cls) -> None:
        cls.send_request = SendRequest()

    #初始化函数，后置清理函数都可以不写，因为我们没有前置条件，也没有后置清理
    @list_data(case_list)
    def test_register(self,case):
        response = self.send_request.send_request(method=case["method"],url=case["url"],data=ast.literal_eval(case["data"]))
        # 获取响应结果
        actual_data = {'code': response['code'], 'msg': response['msg']}
        #断言
        self.assertEqual(first=ast.literal_eval(case['expected_data']),second=actual_data)
if __name__ == '__main__':
    unittest.main()