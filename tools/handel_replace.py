from tools.handle_phone import SendPhone
from tools.handle_attribute import HandleAttribute
from tools.handle_ini import conf
from tools.handle_db import mysql

import ast

class HandleReplace:

    def __init__(self):
        self.handle_phone = SendPhone()


    #设置类属性（全局变量）
    def __set_attribute(self,key,val):
        setattr(HandleAttribute,key,val)

    #通过脚本过去手机号（其他参数）
    def __get_phone_script(self,key):
        phone = self.handle_phone.get_phone()
        self.__set_attribute(key=key,val=phone)

    #从配置文件读取
    def __get_data_conf(self,key):
        data = conf.get(section=key,option=key)
        self.__set_attribute(key=key,val=data)

    #从数据库读取
    def __get_data_db(self,key,sql):
        data = mysql.get_all_data(sql=sql)
        self.__set_attribute(key=key,val=data[0][key])

    #从类属性
    def __get_data_by_attribute(self):
        pass


    def __replace_data(self,data,key_list):
        if isinstance(data,str):
            data=data
        else:
            data = str(data)

        for key in key_list:
            data = data.replace(f"#{key}#",getattr(HandleAttribute,key))

        return data


    #参数替换，对外访问，返回替换后的请求参数
    def replace_request_data(self,request_data,replace_request_data):
        """
        :param request_data: tyep = dict,str 接口请求参数
        :param replace_request_data: type=str
        :return:
        """

        if request_data and replace_request_data:
            replace_request_data = ast.literal_eval(replace_request_data)
            replace_key_list = [key for key in replace_request_data.keys()]
            for key,val in replace_request_data.items():
                if val[0].lower() =='conf':
                    self.__get_data_conf(key=key)

                elif val[0].lower() =="script":
                    if key=='mobile_phone':
                        self.__get_phone_script(key=key)
                    else:
                        print('当前只支持生成手机号')

                elif val[0].lower()=='attribute':
                    print('类属性已存在')

                elif val[0].lower()=='db':
                    if len(val)==2:
                        self.__get_data_db(key=key,sql=val[1])
                    else:
                        print('参数错误')

                else:
                    print('不支持的场景，检查标记位置')


                new_request_data_by_str = self.__replace_data(data=request_data,key_list=replace_key_list)
                return ast.literal_eval(new_request_data_by_str)

        elif request_data and not replace_request_data:
            print('xxx')
            return ast.literal_eval(request_data)

        else:
            print('buchiz')
            return request_data


