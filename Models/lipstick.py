import requests
import pandas as pd
import os
import time
import json
from snownlp import SnowNLP

#定义一个解析单页评论内容的函数
def parse_page(url,headers,cookies):
    result = pd.DataFrame()
    html = requests.get(url,headers = headers,cookies = cookies)
    bs = json.loads(html.text[25:-2])
    #循环解析，结果放在result中
    for i in bs['rateList']:
        content = i['rateContent']
        time = i['rateDate']
        sku = i['auctionSku']
        name = i['displayUserNick']

        df = pd.DataFrame({'买家昵称':[name],'评论时间':[time],'内容':[content],'SKU':[sku]})
        result = pd.concat([result,df])
    return result


#构造网页，需要输入基准的网址和商品总评价数量
def format_url(base_url,num):
    urls = []
    #如果小于99页，则按照实际页数来循环构造
    if (num / 20) < 99:
        for i in range(1,int(num / 20) + 1):
            url = base_url[:-1] + str(i)
            urls.append(url)
    #如果评论数量大于99页能容纳的，则按照99页来爬取
    else:
        for i in range(1,100):
            url = base_url[:-1] + str(i)
            urls.append(url)
    #最终返回urls
    return urls


#输入基准网页，以及有多少条评论
def main(url,num):
    #定义一个存所有内容的变量
    final_result = pd.DataFrame()
    count = 1
    #构造网页，循环爬取并存储结果
    for u in format_url(url,num):
        result = parse_page(u,headers = headers,cookies = cookies)
        final_result = pd.concat([final_result,result])
        print('正在疯狂爬取，已经爬取第 %d 页' % count)
        #设置一个爱心的等待时间，文明爬取
        count += 1
        time.sleep(5.2)
    print('为完成干杯！')
    return final_result


#情感筛选，只留下大于等于0.6分值的结果
def filter_emotion(df,min_ = 0.6):
    scores = []
    #判断情感分值
    for text in df['内容']:
        ob = SnowNLP(text)
        score = ob.sentiments
        scores.append(score)

    df_scores = pd.DataFrame({'情感分值':scores})
    df.index = df_scores.index
    result = pd.concat([df,df_scores],axis = 1)

    #剔除掉没有评论的用户
    result = result.loc[result['内容'].str.find('此用户没有填写评论') == -1,:]

    #留下大于0.6的分值
    result = result.loc[result['情感分值'] >= min_,:]
    return result


if __name__ == "__main__":

    #找到基准网址，在网页JS文件中找到填写就OK
    url = 'https://rate.tmall.com/list_detail_rate.htm?itemId=585140124323&spuId=1136244482&sellerId=3102239719&order=3&currentPage=1'

    #伪装headers按照实际情况填写
    headers = {'User-Agnet':'Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/63.0.3239.132 Safari/537.36',
               'Accept':'text/html,application/xhtml+xml,application/xml;q=0.9,*/*;q=0.8',
               'Accept-Language': 'zh-CN,zh;q=0.8,en;q=0.6'}

    #伪装cookies，最近反爬比较严，最好填入登录的值，并且文明爬取，设置合理的间隔时间
    cookies = {'cookie':''}

    #最终执行，这个产品目前只有265条评价，大家根据实际情况酌情填写
    df = main(url,num = 265)

    #用情感分值来进行清洗
    df = filter_emotion(df,min_ = 0.6)

    #最后可以把结果存为excel文件的形式
    #df.to_excel('XXXX.xlsx')