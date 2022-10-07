
import requests

# 打开进销存首页 - GET 方式
url1 = 'http://39.101.167.251:81/jinxiaocun/index.asp'
r1 = requests.get(url1)
r1.encoding = 'GBK'

# 完成登录操作 - POST 方式
url2 = 'http://39.101.167.251:81/jinxiaocun/main.asp'
data2 = {'username': 'admin', 'pwd': 'admin', 'action': 'login'}
r2 = requests.post(url=url2, data=data2)
r2.encoding = 'gbk'

# 实验：新增单位 - 失败
# 失败原因：该请求没有附带前面响应回的SessionID
# 解决办法：在每次提交请求前，附加SessionID
url3 = 'http://39.101.167.251:81/jinxiaocun/system/danwei_add.asp'
params3 = {'danwei': 'dun', 'submit': '%C8%B7%C8%CF', 'hid1': 'ok'}
r3 = requests.get(url=url3, params=params3)
r3.encoding = 'gbk'

print(r3.text)