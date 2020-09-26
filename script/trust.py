import logging
import random
import unittest,requests,app
from api.trustAPI import trustAPI
from api.loginAPI import loginAPI
from utils import assert_utils,third_request_api
from bs4 import BeautifulSoup


class trust(unittest.TestCase):
    def setUp(self) -> None:
        #初始化API的对象
        self.trust_api = trustAPI()
        self.login_api = loginAPI()
        #初始化session对象
        self.session = requests.Session()

    def tearDown(self) -> None:
        #关闭session对象
        self.session.close()

    #开户请求
    def test01_trust_register(self):
        #1、认证成功的账号进行登录
        #准备测试数据
        phone = app.phone1
        #调用API接口中的方法来发送请求，并接收响应
        response = self.login_api.login(self.session,phone)
        logging.info("get login response = {}".format(response.json()))
        #针对收到的响应进行断言
        assert_utils(self,response,200,200,'登录成功')
        #2、发送开户请求
        # 准备测试数据
        # 调用API接口中的方法来发送请求，并接收响应
        response = self.trust_api.trust_register(self.session)
        logging.info("get trust register response = {}".format(response.json()))
        # 针对收到的响应进行断言
        self.assertEqual(200,response.status_code)
        self.assertEqual(200,response.json().get("status"))
        #3、提取开户响应中的数据，发送第三方的开户请求
        # 准备测试数据
        form_data = response.json().get("description").get("form")
        #调用封装好的第三方请求的接口
        response = third_request_api(form_data)
        # 针对收到的响应进行断言
        self.assertEqual(200,response.status_code)
        self.assertEqual("UserRegister OK",response.text)

    #充值
    def test02_recharge(self):
        #1、开户后账户进行登录
        #准备测试数据
        phone = app.phone1
        #调用API接口中的方法来发送请求，并接收响应
        response = self.login_api.login(self.session,phone)
        logging.info("get login response = {}".format(response.json()))
        #针对收到的响应进行断言
        assert_utils(self,response,200,200,'登录成功')
        #2、获取充值验证码
        #准备测试数据
        r = random.random()
        #调用API接口中的方法来发送请求，并接收响应
        response = self.trust_api.get_recharge_verify_code(self.session,str(r))
        # 针对收到的响应进行断言
        self.assertEqual(200,response.status_code)
        #3、发送充值请求
        #准备测试数据
        amount = '1000'
        #调用API接口中的方法来发送请求，并接收响应
        response = self.trust_api.recharge(self.session,amount)
        logging.info("recharge response = {}".format(response.json()))
        # 针对收到的响应进行断言
        self.assertEqual(200,response.status_code)
        self.assertEqual(200,response.json().get("status"))
        #4、获取充值响应中的数据，发送第三方接口请求
        #准备测试数据
        form_data = response.json().get("description").get("form")
        #调用封装第三方接口的方法来发送请求，并接收响应
        response = third_request_api(form_data)
        logging.info("third request response = {}".format(response.text))
        # 针对收到的响应进行断言
        self.assertEqual("NetSave OK",response.text)