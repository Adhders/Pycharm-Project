import base64
import requests
from _token import access_token
import re
# from aip import AipOcr

""" 你的 APPID AK SK """
API_KEY = 'ySywA0xiNk4PKxhWrxHAcivh'
SECRET_KEY = 'uj07SIaAFh4PtQCKI6SrTf5MzA0Gze0g'


access_token =access_token()  #有效期30天
url = 'https://aip.baidubce.com/rest/2.0/ocr/v1/accurate_basic?access_token=' + access_token
f = open(r'tilt.jpg', 'rb')
img = base64.b64encode(f.read())

params = {"image": img}
print(params)
headers={'Content-Type':'application/x-www-form-urlencoded'}
response= requests.post(url,data=params,headers=headers).json()

if (response):
    print(response)
    for string in response['words_result']:
        if re.match("[A-Z]?\d+$", string[ "words" ]):
            print(string[ "words" ])
