import unittest,time
from script.login import login
import app
from lib.HTMLTestRunner_PY3 import HTMLTestRunner

#将测试脚本添加到测试套件中
suite = unittest.TestSuite()
suite.addTest(unittest.makeSuite(login))

#运行套件并生成测试报告
report_file = app.BASE_DIR + '/report/report{}.html'.format(time.strftime("%Y%m%d-%H%M%S"))
with open(report_file,'wb') as f:
    runner = HTMLTestRunner(f,title="P2P金融项目接口测试报告",description="test")
    runner.run(suite)