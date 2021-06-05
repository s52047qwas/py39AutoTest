import requests
import json
import pprint

# "Authorization": "Bearer token_value"
class ApiTest:
    def __init__(self):
        self.headers_1 = {"X-Lemonban-Media-Type": "lemonban.v1", "Content-Type": "application/json"}
        self.headers_2 = {"X-Lemonban-Media-Type": "lemonban.v2", "Content-Type": "application/json"}
        self.headers_3 = {"X-Lemonban-Media-Type": "lemonban.v3", "Content-Type": "application/json"}
        self.headers_4= {"X-Lemonban-Media-Type":"lemonban.v2","Content-Type":"application/json","Authorization":"Bearer token_value"}
        self.user_login()

    # 注册
    def user_register(self):
        url= 'http://api.lemonban.com/futureloan/member/register'
        data={'mobile_phone':'13000000001',
              'pwd': ''
              }
        res = requests.post(url=url,json=data,headers=self.headers_2)
        print('注册返回：',res.json())

    # 登陆
    def user_login(self):
        url = 'http://api.lemonban.com/futureloan/member/login'
        data={'mobile_phone':'18820992515','pwd':'Aa123456'}
        res = requests.post(url=url,json=data,headers=self.headers_2)
        self.headers_2["Authorization"] = "Bearer {}".format(res.json()['data']['token_info']['token'])
        print('登陆接口返回：',res.json())
        member_id = res.json()['data']['id']
        setattr(ApiTest,'member_id',member_id)

    # 充值
    def recharge_amount(self):
        url = 'http://api.lemonban.com/futureloan/member/recharge'
        data = {'member_id':ApiTest.member_id,'amount':100}
        res = requests.post(url=url,json=data,headers = self.headers_2)
        print('充值接口返回：',res.json())

    # 提现
    def withdraw (self):
        url = 'http://api.lemonban.com/futureloan/member/withdraw'
        data = {'member_id':ApiTest.member_id,'amount':100}
        res = requests.post(url=url,json=data,headers = self.headers_2)
        print('提现接口返回：',res.json())

    # 更新昵称 PATCH
    def change_name(self):
        url = 'http://api.lemonban.com/futureloan/member/update'
        data = {'member_id': ApiTest.member_id, 'reg_name': 'python真香'}
        #res = requests.patch(url=url,data=json.dumps(data),headers = self.headers_2)
        res = requests.patch(url=url,json=data,headers = self.headers_2)
        print('更新昵称返回：',res.json())

    #获取用户信息
    def user_info(self):
        url = 'http://api.lemonban.com/futureloan/member/{member_id}/info'.format(member_id=ApiTest.member_id)
        res = requests.get(url=url,headers = self.headers_2)
        print(res.json())


    # 新增项目(标的)
    def loan_add(self):
        url = 'http://api.lemonban.com/futureloan/loan/add'
        data = {
            'member_id':ApiTest.member_id,
            'title':'随便借点钱花花',
            'amount':1000,
            'loan_rate':10.0,
            'loan_term':10,
            'loan_date_type':1,
            'bidding_days':10
        }
        res = requests.post(url=url,json=data,headers=self.headers_2)
        print('新增标的返回：',res.json())
        setattr(ApiTest,'loan_id',res.json()['data']['id'])

    # 审核项目【管理员账号】
    def loan_check(self):
        self.loan_add()
        url = 'http://api.lemonban.com/futureloan/loan/audit'
        data = {
            'loan_id':ApiTest.loan_id,
            'approved_or_not':True
        }
        res = requests.patch(url=url,json=data,headers = self.headers_2)
        print('审核项目返回：',res.json())

    #投资
    def loan_invest (self):
        self.loan_check()
        url = 'http://api.lemonban.com/futureloan/member/invest'
        data = {
            'loan_id':ApiTest.loan_id,
            'member_id':ApiTest.member_id,
            'amount':100
        }
        res = requests.post(url=url,json=data,headers = self.headers_2)
        print('投资返回：',res.json())

    # 获取项目列表
    def get_loans(self):
        url = 'http://api.lemonban.com/futureloan/loans'
        res = requests.get(url=url,headers =  self.headers_2)
        pprint.pprint(res.json())


if __name__ == '__main__':
    a=ApiTest()
    a.get_loans()


