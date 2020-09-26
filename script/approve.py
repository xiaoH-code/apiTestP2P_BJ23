import logging
import unittest,requests

import app
from api.approveAPI import approveAPI
from api.loginAPI import loginAPI
from utils import assert_utils


class approve(unittest.TestCase):
    def setUp(self) -> None:
        #API接口对象的初始化
        self.login_api = loginAPI()
        self.approve_api = approveAPI()
        #session的初始化
        self.session = requests.Session()

    def tearDown(self) -> None:
        #关闭session
        self.session.close()

    #输入正确的认证信息，认证成功
    def test01_approve_success(self):
        #1、登录成功
        #准备测试数据
        phone = app.phone1
        #调用API接口中的方法来发送请求，并接收响应
        response = self.login_api.login(self.session,phone)
        logging.info("get login response = {}".format(response.json()))
        #针对收到的响应进行断言
        assert_utils(self,response,200,200,'登录成功')
        #2、输入姓名和身份证号，进行认证
        # 准备测试数据
        name = '张三'
        cardId = '110117199003070995'
        # 调用API接口中的方法来发送请求，并接收响应
        response = self.approve_api.approve(self.session,name,cardId)
        logging.info("approve response = {}".format(response.json()))
        # 针对收到的响应进行断言
        assert_utils(self,response,200,200,"提交成功!")

    #姓名为空时，实名认证失败
    def test02_approve_fail_name_is_null(self):
        #1、登录成功
        #准备测试数据
        phone = app.phone2
        #调用API接口中的方法来发送请求，并接收响应
        response = self.login_api.login(self.session,phone)
        logging.info("get login response = {}".format(response.json()))
        #针对收到的响应进行断言
        assert_utils(self,response,200,200,'登录成功')
        #2、输入姓名和身份证号，进行认证
        # 准备测试数据
        name = ''
        cardId = '110117199003070995'
        # 调用API接口中的方法来发送请求，并接收响应
        response = self.approve_api.approve(self.session,name,cardId)
        logging.info("approve response = {}".format(response.json()))
        # 针对收到的响应进行断言
        assert_utils(self,response,200,100,"姓名不能为空")

    #身份证号为空时，实名认证失败
    def test03_approve_fail_cardid_is_null(self):
        #1、登录成功
        #准备测试数据
        phone = app.phone2
        #调用API接口中的方法来发送请求，并接收响应
        response = self.login_api.login(self.session,phone)
        logging.info("get login response = {}".format(response.json()))
        #针对收到的响应进行断言
        assert_utils(self,response,200,200,'登录成功')
        #2、输入姓名和身份证号，进行认证
        # 准备测试数据
        name = '张三'
        cardId = ''
        # 调用API接口中的方法来发送请求，并接收响应
        response = self.approve_api.approve(self.session,name,cardId)
        logging.info("approve response = {}".format(response.json()))
        # 针对收到的响应进行断言
        assert_utils(self,response,200,100,"身份证号不能为空")

    #获取认证信息
    def test04_get_approve_success(self):
        #1、登录
        #准备测试数据
        phone = app.phone1
        #调用API接口中的方法来发送请求，并接收响应
        response = self.login_api.login(self.session,phone)
        logging.info("get login response = {}".format(response.json()))
        #针对收到的响应进行断言
        assert_utils(self,response,200,200,'登录成功')
        #2、获取认证信息
        #准备测试数据
        #调用API接口中的方法来发送请求，并接收响应
        response = self.approve_api.get_approve(self.session)
        logging.info("get approve response = {}".format(response.json()))
        #对结果进行断言
        self.assertEqual(200,response.status_code)
        self.assertEqual("110****995",response.json().get("card_id"))