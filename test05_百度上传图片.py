
import requests

# 百度识图上传图片的接口
url = 'https://graph.baidu.com/upload'
# 待上传的图片文件
filename = 'C:\\Users\\My\\Pictures\\5.软件测试对象、级别_proc.jpg'
# 定义请求的数据：字典类型
#  键：参数名称（抓包获取）   值：打开的待上传文件
files = {'image': open(filename, 'rb')}


r = requests.post(url, files=files)
r.encoding='utf-8'

print(r.headers)
print(r.status_code)
print(r.text)
