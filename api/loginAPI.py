import app
import requests


class loginAPI():
    def __init__(self):
        self.getImageCode_url = app.BASE_URL + '/common/public/verifycodel/'
        self.getSmsCode_url=app.BASE_URL+'/member/punlic/sendsms'
        self.login_url=app.BASE_URL+'/member/public/login'

    def getImageCode(self, session, r):
        url = self.getImageCode_url + r
        #发送请求
        response = session.get(url)
        return response

    def getSmsCode(self,session,phone,imgVerifyCode):
        #准备参数
        data={'phone':phone,'imgVerifyCode':imgVerifyCode,'type':'reg'}
        #发送请求
        response=session.post(self.getSmsCode_url,data=data)
        #返回响应
        return response
    def login(self,session,phone,pwd):
        data={'keywords':phone,'password':pwd}
        response=session.post(self.login_url,data=data)
        return response


