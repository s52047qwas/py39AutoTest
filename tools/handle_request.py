
import requests

from tools.handle_loging import my_logger

class SendRequest:
    def __init__(self):
        self.headers = {"X-Lemonban-Media-Type": "lemonban.v2", "Content-Type": "application/json"}

    def __handle_headers(self,token=None):
        if token:
            self.headers["Authorization"] = "Bearer {}".format(token)
        else:
            pass

    def send_request(self,method,url,data,token=None):
        """
        :param method: 请求方法
        :param url: 请求地址
        :param data: 请求参数
        :param token: 鉴权token
        :return: 返回接口响应结果
        """

        try:
            my_logger.info(msg='请求方式:\n{}'.format(method))
            my_logger.info(msg='请求地址:\n{}'.format(url))
            my_logger.info(msg='请求参数：\n{}'.format(data))
            new_method = method.upper()
            self.__handle_headers(token=token)
            if new_method == 'GET':
                response = requests.get(url=url,params=data,headers = self.headers)
                my_logger.info(msg='GET请求返回:\n{}'.format(response.json()))
            elif new_method == 'POST':
                response = requests.post(url=url, json=data, headers=self.headers)
                my_logger.info(msg='POST请求返回:\n{}'.format(response.json()))
            else:
                my_logger.info(msg='{}请求类型暂不支持,后续再加'.format(method))
            return response.json()
        except Exception as e:
            my_logger.error(msg='========请求发送结束，请求报错了========')
            my_logger.exception(e)
            raise




