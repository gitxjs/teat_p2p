import unittest
import app
import time
from lib.HTMLTestRunner import HTMLTestRunner

from testcase.login import login

suite=unittest.TestSuite()
suite.addTest(unittest.makeSuite(login))

report_file=app.BASE_URL+'/report/report{}.html'.format(time.strftime('%Y%m%d'))

with open(report_file,'wb') as f:
    runner=HTMLTestRunner(f,title='报告')
    runner.run()