
import requests

# 模拟向指定的接口地址发送请求（Get请求）
# r：请求后服务器的响应
r = requests.get('https://www.baidu.com/')

# 打印服务器返回的HTTP响应状态码：200
print(r.status_code)

# 打印响应头中的“content-type”: text/html
print(r.headers['content-type'])


# 打印request默认的响应解码方式: ISO-8859-1
print(r.encoding)

# 改变默认的解码方式为：UTF-8
r.encoding = 'UTF-8'

# 打印响应体
print(r.text)

