import logging
import os
from logging import handlers

BASE_URL='http://user-p2p-test.itheima.net'
base_dir = os.path.dirname(os.path.abspath(__file__))
DB_URL='52.83.144.39'
DB_USERNAME='root'
DB_PASSWORD='123456'
DB_MEMBER=''
DB_FINANCE=''

#初始化日志配置
def init_log_config():
    #1.初始化日志对象:
    logger=logging.getLogger()

    #2.设置日志级别
    logger.setLevel(logging.INFO)

    #3.创建控制台日志处理器和文件日志处理器
    #3.1.负责将日志日志信息输入到pycharm下方的console（控制台）窗口中
    sh = logging.StreamHandler()
    #3.2.负责将日志信息输入到log目录下的日志文件中

    #logfile=base_dir+'log'+os.sep+'p2p{}.log'.format("%Y%m%D %H%M%S")
    logfile = base_dir + r'\log' + os.sep + 'p2p.log'
    fh=logging.handlers.TimedRotatingFileHandler(logfile,when='m',interval=5,backupCount=5,encoding='utf-8')

    #4.设置日志格式，创建格式化器
    fmt='%(asctime)s %(levelname)s [%n(ame)s] [%(filename)s(funcName)s:%(lineno)d] - %(message)s'
    formatter=logging.Formatter(fmt)

    #5.将格式化器设置到日志器中
    sh.setFormatter(formatter)
    fh.setFormatter(formatter)

    #6.将日志处理器添加到日志对象
    logger.addHandler(sh)
    logger.addHandler(fh)
