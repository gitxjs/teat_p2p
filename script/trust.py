import unittest,logging,requests

from api.loginAPI import loginAPI
from api.trustAPI import trustAPI
import utils
from bs4 import BeautifulSoup


class trust(unittest.TestCase):
    def setUp(self):
        self.login_api=loginAPI()
        self.trust_api=trustAPI()
        self.session=requests.Session()

    def tearDown(self):
        self.session.close()


    #开户请求
    def test01_trust_requests(self):
        #1。认证通过的账号登录
        response=self.login_api.login(self.session,13452298765,'123456a')
        utils.assert_utils(self,response,200,200,'登录成功')
        #2.发送海湖请求
        response=self.trust_api.trust_register(self.session)
        logging.info('trust register response ={}'.format(response.json()))
        self.assertEqual(200,response.status_code)
        self.assertEqual(200,response.json().get('status'))

        #3.发送第三方的开户请求
        form_data=response.json().get('description').get('form')
        logging.info('form response={}'.format(form_data))
        #4.解析form表单中的内容，并提取第三方请求的参数
        soup=BeautifulSoup(form_data,'html.parser')
        third_url=soup.form['action']
        data={}
        for input in soup.find_all('input'):
            data.setdefault(input['name'],input['vaule'])

        #发送第三方请求
        response=requests.post(third_url,data=data)
        self.assertEqual(200,response.status_code)
        self.assertEqual('userRegister OK',response.text)