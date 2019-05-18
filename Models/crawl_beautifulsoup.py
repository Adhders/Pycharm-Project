from urllib.request import urlopen
from bs4 import BeautifulSoup
from selenium import webdriver
import time
import xlwt

resp=urlopen('http://www.ssac.com.cn/UserArticleList.aspx?LinkID=9&ColumnID=106').read().decode('utf-8')
soup=BeautifulSoup(resp,'xml')
driver = webdriver.Firefox()
driver.get('http://www.ssac.com.cn/UserArticleList.aspx?LinkID=9&ColumnID=106')
f=xlwt.Workbook()
sheet1=f.add_sheet('test',cell_overwrite_ok=True)


def write_2(soup):
    global count
    conut=0
    for i in range(1,3):
        for question in soup.find_all('a',target='_blank'):
            url='http://www.ssac.com.cn/'+question.get('href')
            try:
                resp = urlopen(url).read().decode('utf-8')
            except:
                continue
            soup = BeautifulSoup(resp, "html.parser")
            graph=soup.find_all('div',class_='content3')
            str=['']
            for string in graph:
                str.append(string.get_text())
            text=''.join(str)
            if len(text)>2000:
                print(question.get_text())
            else:
                sheet1.write(count, 0, question.get_text())
                sheet1.write(count,1,text)
                count +=1
        next = driver.find_element_by_id('ctl00_ContentPlaceHolder1_lbtnNextPage')
        next.click()
        time.sleep(3)
        html_const = driver.page_source.encode('utf-8')
        soup = BeautifulSoup(html_const, "html.parser")

write_2(soup)
f.save('junbo.xls')