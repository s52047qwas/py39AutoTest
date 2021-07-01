import pytest


datas = [
    {"api":"login","url":"http://api.lemonban.com/futureloan/member/login"},
    {"api":"register","url":"http://api.lemonban.com/futureloan/member/register"},
    {"api":"recharge","url":"http://api.lemonban.com/futureloan/member/recharge"},
    {"api":"withdraw","url":"http://api.lemonban.com/futureloan/member/withdraw"},
    {"api":"updateuser","url":"http://api.lemonban.com/futureloan/member/updateuser"}
]

@pytest.fixture(scope='class')
def she():
    print('=====这是前置函数=======')
    yield 'test1','test2'
    print('=========这是后置函数==========')

@pytest.mark.usefixtures('she')
@pytest.mark.parametrize("case",datas)
def test_read_datas(case,she):
    print(she[0])
    print(case["api"], print(case["url"]))
    print("======================================")
    assert 1==1



# @pytest.mark.parametrize("api,url",datas)
# def test_read_datas(api,url):
#     print(api, url)
#     print("======================================")
# @pytest.mark.parametrize("case",datas)
# def test_read_datas(case):
#     print(case["api"], print(case["url"]))
#     print("======================================")
#
#
#
# @pytest.mark.parametrize("api,url",datas)
# def test_read_datas(api,url):
#     print(api, url)
#     print("======================================")


if __name__ == '__main__':
    pytest.main(["-s","-v","test_case2.py","--html=report1.html", "--alluredir=./pytest_test/allure1_files"])
    print('sss')