
"""

分层设计
tools：工具
test_case：unittest+ddt
conf：host、数据库
test_data：excel表
reports：测试报告
logs：日志文件
框架入口：main.py

整体流程
1、读取excel表测试用例
2、封装requests请求
3、编写测试用例
4、执行测试用例
5、收集测试报告
6、持续集成


第一天(day26)：
1、分层设计思想
2、搭建分层设计框架模型
3、excel用例数据os路径处理

第二天(day27)：
1、配置conf文件的路径
2、配置文件添加excel的sheet_name
3、封装requests请求
   3.1、根据项目鉴权方式，无需鉴权的接口(注册、登陆、项目列表)
   3.2、需要鉴权：传入token，拿到token就添加到请求头中，再去发起请求
   3.3、不需要鉴权：不传token，token设置一个默认值，请求头就不做处理，再去发起请求
   3.4、收集日志
4、unittest+ddt 编写测试用例
   4.1、创建测试类(继承unittest.TestCase，类名称建议Test开头)
   4.2、创建测试函数(必须test开头)
        1、发起request请求
        2、断言























































"""