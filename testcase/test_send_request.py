import requests
import pytest

class Testlogin():
    session = requests.session()

    def test_login(self):
        url='http://39.101.167.251:81/jinxiaocun/index.asp?action=login '
        data={
            'username':'admin','pwd':'admin','action':'login'
        }
        response=Testlogin.session.request('post',url=url,data=data)
        response.encoding='gbk'
        print(response.text)
    def test_danwei(self):
        url1 = 'http://39.101.167.251:81/jinxiaocun/system/danwei_add.asp?danwei=吨&submit=+%C8%B7+%C8%CF+&hid1=ok'
        data1 = {'danwei': '567', 'submit': '+%C8%B7+%C8%CF+', 'hid1': 'ok', }
        r3 = Testlogin.session.request('get',url=url1,data=data1)
        r3.encoding = 'GBK'

        print(r3.text)


if __name__=='__main__':
    pytest.main(['-vs'])