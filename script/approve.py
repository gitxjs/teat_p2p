import unittest
import requests
import utils


from api.approveAPI import approveAPI
from api.loginAPI import loginAPI


class approve(unittest.TestCase):
    realname='张三'
    cardid='812868931932928132487'
    def setUp(self):
        self.login_api=loginAPI()
        self.approve_api=approveAPI()
        self.session=requests.Session()
        pass
    def tearDown(self):
        self.session.close()

    #认证成功
    def test01(self):
        #1登录
        response=self.login_api.login(self.session,13452298765,'123456a')
        utils.assert_utils(self,response,200,200,'登录成功')
        #2发送认证请求
        response=self.approve_api.approve(self.session,self.realname,self.cardid)
        utils.assert_utils(self,response,200,200,'提交成功!')