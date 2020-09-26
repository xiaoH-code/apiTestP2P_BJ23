import app


class trustAPI():
    def __init__(self):
        self.trust_register_url = app.BASE_URL + '/trust/trust/register'
        self.get_recharge_verify_code_url = app.BASE_URL + '/common/public/verifycode/'
        self.recharge_url = app.BASE_URL + '/trust/trust/recharge'

    def trust_register(self,session):
        #定义参数
        #发送请求
        response = session.post(self.trust_register_url)
        #返回响应
        return response

    def get_recharge_verify_code(self,session,r):
        #定义参数
        url = self.get_recharge_verify_code_url + r
        #发送请求
        response = session.get(url)
        #返回响应
        return response

    def recharge(self,session,amount,code='8888'):
        # 定义参数
        data = {"paymentType": "chinapnrTrust",
                "formStr": "reForm",
                "amount": amount,
                "valicode": code}
        #发送请求
        response = session.post(self.recharge_url,data=data)
        #返回响应
        return response