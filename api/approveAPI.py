import app


class approveAPI():
    def __init__(self):
        self.approve_url = app.BASE_URL + "/member/realname/approverealname"
        self.get_approve_url = app.BASE_URL + '/member/member/getapprove'

    def approve(self,session,name,cardId):
        #定义参数
        data = {"realname":name, "card_id":cardId}
        #发送请求
        response = session.post(self.approve_url,data=data,files={'x':'y'})
        #返回响应
        return response

    def get_approve(self,session):
        #定义参数
        #发送请求
        response = session.post(self.get_approve_url)
        #返回响应
        return response