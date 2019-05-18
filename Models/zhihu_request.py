import requests
import json
Cookie="_zap=4011a69a-e98c-49a3-a706-e4a01eab782d; __DAYU_PP=rqqINJyFjJAuU3eAiV6624314f99165a; d_c0=AKBkwu66ug2PTqU8kS5ZoQ2X2j644fznS1M=|1528649551';_xsrf=4ynzKAM8PVpbTTm14bmJoxtscdpOOpPz; q_c1=6d3e6f9baf954fdbb038234576a56ea7|1534687686000|1517138937000; l_cap_id='ZTFhMmVkMjA4MTc5NDk3ZGE0MWRkMDlhYTVjYmY1NzU=|1535788301|313bcf8727b39629e45e3db7b6d93c6bc8d81544'; r_cap_id='MTI3YTA1NTBkNDc5NGI5ZjhkOTEyZmEyNGUyNmE4MTM=|1535788301|3137592922687a872e159ace3e79601245261a3c'; cap_id='ZTI3OWU2Nzg1MmYzNGIxNGI4YjI0ODIxYmMxN2ExODE=|1535788301|aedb11ed0aa529fae63359706ca6881b34ff7435'; capsion_ticket='2|1:0|10:1535789753|14:capsion_ticket|44:MjJhMDgxZDY3ZWQzNDZlM2I3ZTg1MDI5YWE4NGYxZDg=|2161601b3240a8a9b9fd206a9d9a0b85cd110aff0bd70f0cc06c3ce1c1c3d4e7'; z_c0='2|1:0|10:1535789771|4:z_c0|92:Mi4xRVUxMUFBQUFBQUFBb0dUQzdycTZEU1lBQUFCZ0FsVk55NWgzWEFBRlVsRkpnM1pFbHVkUkJkeXN2MEtWOGhLRWpn|f832fc14df6a7670b77ae8106555b9bb66277020a6c3e87f44302cc7e6b56ed7'; __utma=51854390.1282910891.1535815155.1535815155.1535815155.1; __utmz=51854390.1535815155.1.1.utmcsr=(direct)|utmccn=(direct)|utmcmd=(none); __utmv=51854390.100-1|2=registration_date=20140822=1^3=entry_date=20140822=1; tgw_l7_route=8605c5a961285724a313ad9c1bbbc186"
with open('zhihuCookies.json', 'r', encoding='utf-8') as f:
    listcookies = json.loads(f.read())  # 获取cookies
cookies_dict = dict()
for cookie in listcookies:
    cookies_dict[ cookie[ 'name' ] ] = cookie[ 'value' ]

headers = {
        "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:61.0) Gecko/20100101 Firefox/61.0",
        "HOST": "www.zhihu.com"
    }
s=requests.session()
url = 'https://www.zhihu.com//explore'
res = requests.get(url,headers=headers,data=Cookie)#或者data=cookies_dict
print(res.cookies['_xsrf'])#当url的地址与host的地址相同时，要用res.request._cookies进行获取
with open('zhihu_explore.html', 'w', encoding='utf-8') as f:
    f.write(res.text)

