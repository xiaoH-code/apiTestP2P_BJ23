import app

class loginAPI():
    def __init__(self):
        #定义接口请求的URL
        self.get_Img_code_url = app.BASE_URL + "/common/public/verifycode1/"
        self.get_sms_code_url = app.BASE_URL + '/member/public/sendSms'
        self.register_url = app.BASE_URL + '/member/public/reg'
        self.login_url = app.BASE_URL + '/member/public/login'

    def get_Img_code(self,session,r):
        #发送接口请求
        url = self.get_Img_code_url + r
        response = session.get(url)
        #返回响应
        return response

    def get_sms_code(self,session,phone,imgCode='8888'):
        #定义参数
        data = {'phone':phone,'imgVerifyCode':imgCode,'type':'reg'}
        #发送请求
        response = session.post(self.get_sms_code_url,data=data)
        #返回响应
        return response

    def register(self,session,phone,pwd='test123',imgCode='8888',phoneCode='666666',dyServer='on',invitePhone=''):
        #定义参数
        data = {"phone": phone,
                "password": pwd,
                "verifycode": imgCode,
                "phone_code": phoneCode,
                "dy_server": dyServer,
                "invite_phone": invitePhone}
        #发送请求
        response = session.post(self.register_url,data=data)
        #返回响应
        return response

    def login(self,session,phone, pwd='test123'):
        #定义参数
        data = {"keywords": phone, "password": pwd}
        #发送请求
        response = session.post(self.login_url,data=data)
        #返回响应
        return response