
import requests

# 供学习用的接口：返回请求内容
url = 'http://httpbin.org/post'
# 待上传的图片文件
filename = 'C:\\Users\\My\\Pictures\\5.软件测试对象、级别_proc.jpg'
# 定义请求的数据：字典类型
files = {'file': open(filename, 'rb')}

r = requests.post(url, files=files)



print(r.text)
print(r.status_code)
print(r.headers)