import logging,os
from logging import handlers

BASE_DIR = os.path.dirname(os.path.abspath(__file__))
BASE_URL = "http://user-p2p-test.itheima.net"
phone1 = '13011231111'
phone2 = '13011231112'
phone3 = '13011231113'
phone4 = '13011231114'
phone5 = '13011231115'
tender_id = 866
DB_host = '52.83.144.39'
DB_user = 'root'
DB_password = 'Itcast_p2p_20191228'
DB_port = 3306
DB_database = 'czbk_member'

#初始化日志配置
def init_log_config():
    #1、初始化日志对象
    logger = logging.getLogger()
    #2、设置日志级别
    logger.setLevel(logging.INFO)
    #3、创建控制台日志处理器和文件日志处理器
    sh = logging.StreamHandler()
    log_file = BASE_DIR + os.sep + "log" + os.sep + "p2p.log"
    fh = logging.handlers.TimedRotatingFileHandler(log_file,when='M',interval=5,backupCount=5,encoding='utf-8')
    #4、设置日志格式，创建格式化器
    fmt = '%(asctime)s %(levelname)s [%(name)s] [%(filename)s(%(funcName)s:%(lineno)d)] - %(message)s'
    formatter = logging.Formatter(fmt)
    #5、将格式化器设置到日志器中
    sh.setFormatter(formatter)
    fh.setFormatter(formatter)
    #6、将日志处理器添加到日志对象
    logger.addHandler(sh)
    logger.addHandler(fh)