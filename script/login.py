import unittest
import requests
from api.loginAPI import loginAPI
import random
import utils


class login(unittest.TestCase):
    def setUp(self):
        self.login_api=loginAPI()
        self.session=requests.Session()

    def tearDown(self):
        self.session.close()
    #参数为随机小数时获取图片验证码成功
    def test01_get_img_code_float(self):
        #定义参数
        r=random.randint(0,1)
        #调用接口类中的接口
        response=self.login_api.getImageCode(self.session,str(r))
        #接受接口的返回结果，进行断言
        self.assertEqual(200,response.status_code)
    #随机整数时，获取图片验证码成功
    def test02_get_img_code(self):
        r=random.randint(100000,9999999)
        response=self.login_api.getImageCode(self.session,str(r))
        self.assertEqual(200,response.status_code)
     #参数为空时，获取图片验证码失败
    def test03_get_img_code_param_isnull(self):
        response=self.login_api.getImageCode(self.session,"")
        self.assertEqual(404,response.status_code)
    # 参数为随机字母时，获取图片验证码失败
    def test04_get_img_code_char(self):
        r=random.sample('asdhbfsjfvdvfvbdj',6)
        #返回的是一个list，要转换成字符串
        ran=r"".join(r)
        print(ran)
        response=self.login_api.getImageCode(self.session,ran)
        self.assertEqual(400,response.status_code)

    #登录成功
    def test05_login_success(self):
        #准备参数
        phone1 = 13452298765
        pwd='123456a'
        #调用接口类中的发送登录的接口
        response=self.login_api.login(self.session,phone1,pwd)
        #对结果进行断言
        utils.assert_utils(self,response,200,200,'登录成功')

