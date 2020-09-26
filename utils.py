import json
import logging

import pymysql
import requests
from bs4 import BeautifulSoup

import app


def assert_utils(self,response,status_code,status,desc):
    # 针对收到的响应进行断言
    self.assertEqual(status_code, response.status_code)
    self.assertEqual(status, response.json().get('status'))
    self.assertEqual(desc, response.json().get("description"))

def third_request_api(form_data):
    #解析form表单中的内容，并提取参数发送第三方请求
    soup = BeautifulSoup(form_data, 'html.parser')
    third_request_url = soup.form['action']
    data = {}
    for input in soup.find_all('input'):
        data.setdefault(input['name'], input['value'])
    logging.info("third request data = {}".format(data))
    # 调用响应中的url和参数来发送请求，并接收响应
    response = requests.post(third_request_url, data=data)
    logging.info("third response data={}".format(response.text))
    return response

class DButils:
    @classmethod
    def get_conn(cls):
        conn = pymysql.connect(app.DB_host,app.DB_user,app.DB_password,app.DB_database,app.DB_port,autocommit=True)
        return conn

    @classmethod
    def close_conn(cls,cursor,conn):
        if cursor:
            cursor.close()
        if conn:
            conn.close()

    @classmethod
    def execute_sql(cls,sql):
        try:
            conn = cls.get_conn()
            cursor = conn.cursor()
            cursor.execute(sql)
        except Exception as e:
            conn.rollback()
        finally:
            cls.close_conn(cursor,conn)

def read_img_verify_code_data():
    #定义数据文件的路径
    data_file = app.BASE_DIR + "/data/imgVerifyCode.json"
    #定义空的测试数据的列表
    test_case_data = []
    #打开数据文件，并读取里面的内容
    with open(data_file,encoding='utf-8') as f:
        #将JSON数据文件转化为字典格式
        verify_data = json.load(f)
        #提取定义的测试数据列表
        test_data_list = verify_data.get("test_img_verify_code")
        #依次读取出测试数据列表中的type、status，添加到测试数据列表中test_case_data
        for test_data in test_data_list:
            test_case_data.append((test_data.get("type"),test_data.get("status_code")))
    print("json data={}".format(test_case_data))
    return test_case_data

#读取注册的参数文件中的内容
def read_register_data():
    #获取注册的参数文件路径
    data_file = app.BASE_DIR + "/data/register.json"
    #定义空的列表，用来存放读取出来的测试数据
    test_case_data = []
    #打开数据文件，并读取数据文件中的内容
    with open(data_file,encoding='utf-8') as f:
        #将json格式的文件内容转化为对应的字典格式
        register_data = json.load(f)
        #提取定义的测试数据列表
        test_data_list = register_data.get("test_register")
        #依次读取测试数据列表中的内容，并将请求和响应的各项参数放入到测试数据的列表中
        for test_data in test_data_list:
            test_case_data.append((test_data.get("phone"),test_data.get("pwd"),test_data.get("verifycode"),test_data.get("phonecode"),test_data.get("dyServer"),test_data.get("invitephone"),test_data.get("status_code"),test_data.get("status"),test_data.get("description")))
    print("test_case_data = {}".format(test_case_data))
    return test_case_data

#定义统一读取所有的参数数据文件的代码
def read_param_data(filename,method_name,param_names):
    #filename: 需要读取的json数据文件的文件名 （放在data目录下）
    #method_name: json数据文件中定义的测试数据文件列表的名称。如：test_register
    #param_names: json数据文件中定义的所有参数名组成的字符串，多个参数名称之间用“,”分隔。如："type,status_code"

    #获取待读取的参数文件的路径
    data_file = app.BASE_DIR + "/data/" + filename
    #定义空的列表，用来存放读取出来的测试数据
    test_case_data = []
    #打开数据文件，依次读取出数据文件中的测试数据
    with open(data_file,encoding='utf-8') as f:
        #将JSON格式的数据内容，转化为字典格式
        dict_data = json.load(f)
        #提取出定义的数据列表内容
        test_data_list = dict_data.get(method_name)
        #依次读取测试数据列表中的数据，并将请求和响应的各项参数传递给测试数据的列表
        for test_data in test_data_list:
            #定义一组列表，存放一组test_data中的所有测试数据
            test_params = []
            for param in param_names.split(','):
                #依次读取每一个参数的值，添加到test_params中，形成一个列表
                test_params.append(test_data.get(param))
            test_case_data.append(test_params)
    print("test_case_data = {}".format(test_case_data))
    return test_case_data
