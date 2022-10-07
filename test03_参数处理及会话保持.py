
import requests
import unittest


# url1 ='http://39.101.167.251:81/jinxiaocun/index.asp'
# r1 = s.get(url1)
r=requests.Session()

url2 = 'http://39.101.167.251:81/jinxiaocun/main.asp'
data1 = {'username':'admin','pwd':'admin','action':'login',}
r2 = r.post(url=url2,data=data1)
r2.encoding='GBK'

print(r2.text)
print('------------')

url3 = 'http://39.101.167.251:81/jinxiaocun/system/danwei_add.asp'
data2= {'danwei':'ttt','submit':'+%C8%B7+%C8%CF+','hid1':'ok',}
r3 = r.get(url=url3,data=data2)
r3.encoding='GBK'

print(r3.text)