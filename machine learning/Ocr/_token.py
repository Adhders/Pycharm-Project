import requests
#参考https://ai.baidu.com/forum/topic/show/867951 ,获取API_Key 与 SK
#参考http://ai.baidu.com/docs#/Auth/top

API_Key='ySywA0xiNk4PKxhWrxHAcivh'
SK="uj07SIaAFh4PtQCKI6SrTf5MzA0Gze0g"

url = 'https://aip.baidubce.com/oauth/2.0/token?grant_type=client_credentials&client_id={0}&client_secret={1}'.format(API_Key,SK)

headers={"Content-Type": "application/json;charset=UTF-8"}
response= requests.post(url,headers=headers).json()
def access_token():
    return response["access_token"]
