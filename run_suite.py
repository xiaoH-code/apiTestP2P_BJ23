import unittest,time

#将测试脚本添加到测试套件中
from script.tender import tender
from script.trust import trust
from script.tender_process import test_tender_process
from script.approve import approve
from script.login_param import login
import app
from lib.HTMLTestRunner_PY3 import HTMLTestRunner

suite = unittest.TestSuite()
suite.addTest(unittest.makeSuite(login))
suite.addTest(unittest.makeSuite(approve))
suite.addTest(unittest.makeSuite(trust))
suite.addTest(unittest.makeSuite(tender))
suite.addTest(unittest.makeSuite(test_tender_process))

#运行套件并生成测试报告
#report_file = app.BASE_DIR + '/report/report{}.html'.format(time.strftime("%Y%m%d-%H%M%S"))
report_file = app.BASE_DIR + '/report/report.html'
with open(report_file,'wb') as f:
    runner = HTMLTestRunner(f,title="P2P金融项目接口测试报告",description="test")
    runner.run(suite)