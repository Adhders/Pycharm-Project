import base64
import requests
import re
# import urllib
# import urllib.request as urllib2
from aip import AipOcr

""" 你的 APPID AK SK """
APP_ID = '16143595'
API_KEY = 'ySywA0xiNk4PKxhWrxHAcivh'
SECRET_KEY = 'uj07SIaAFh4PtQCKI6SrTf5MzA0Gze0g'

# client = AipOcr(APP_ID, API_KEY, SECRET_KEY)

access_token ="24.e058c2807035a63492540520310dc28b.2592000.1559133375.282335-16143595"  #有效期30天
url = 'https://aip.baidubce.com/rest/2.0/ocr/v1/accurate_basic?access_token=' + access_token
# 二进制方式打开图文件
f = open(r'15118.jpg', 'rb')
# 参数image：图像base64编码
img = base64.b64encode(f.read())
params = {"image": img}
# data= urllib.parse.urlencode(params).encode("utf-8")
headers={'Content-Type':'application/x-www-form-urlencoded'}
response= requests.post(url,data=params,headers=headers).json()

if (response):
    for string in response['words_result']:
        if re.match("[A-Z]?\d+$", string[ "words" ]):
            print(string[ "words" ])
