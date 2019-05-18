import scrapy
from selenium import webdriver
from scrapy import cmdline
import time
import json
import codecs

class Zhihu_Spider(scrapy.Spider):
    name = 'zhihu'
    allowed_domains = [ 'www.zhihu.com' ]
    start_urls = [ 'http://www.zhihu.com/' ]

    # 模拟请求的headers，非常重要，不设置也可能知乎不让你访问请求
    headers = {
        "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:61.0) Gecko/20100101 Firefox/61.0",
        "HOST": "www.zhihu.com"
    }

    # 第一步：使用selenium登录知乎并获取登录后的cookies，cookies没失效时，只要初次请求执行一次
    def loginZhihu(self):
        # 登录网址
        loginurl = 'https://www.zhihu.com/signin'
        # 加载webdriver驱动，用于获取登录页面标签属性
        driver = webdriver.Firefox()
        driver.get(loginurl)
        driver.find_element_by_name('username').clear()  # 获取用户名框
        driver.find_element_by_name('username').send_keys('13661451627')  # 填充用户名
        driver.find_element_by_name('password').clear()  # 获取密码框
        driver.find_element_by_name('password').send_keys('lijunbo1991')  # 填充密码
        time.sleep(2)
        # input("检查网页是否有验证码要输入，有就在网页输入验证码，输入完后在编辑器中回车；如果无验证码，则直接回车")
        # 非常关键，有时候知乎会在输入密码后弹出验证码，这一步可将代码执行暂时停滞
        # driver.find_element_by_css_selector("button[class='Button SignFlow-submitButton Button--primary Button--blue']").click()    # 点击登录按钮
        # time.sleep(10)  # 同样休眠10s等待页面
        # input("请扫描页面二维码，并确认登录后，点击回车：")  # 点击二维码手机扫描登录
        # 通过上述的方式实现登录后，其实我们的cookies在浏览器中已经有了，我们要做的就是获取
        cookies = driver.get_cookies()  # Selenium为我们提供了get_cookies来获取登录cookies
        driver.close()  # 获取cookies便可以关闭浏览器
        # 然后的关键就是保存cookies，之后请求从文件中读取cookies就可以省去每次都要登录一次的
        # 当然可以把cookies返回回去，但是之后的每次请求都要先执行一次login没有发挥cookies的作用
        jsonCookies = json.dumps(cookies)  # 通过json将cookies写入文件
        with open('zhihuCookies.json', 'w') as f:
            f.write(jsonCookies)
        print(cookies)

    def question(self, response):
        with open('zhihu_find.html', 'w', encoding='utf-8') as f:
            f.write(response.text)  # 写入文件，保存成.html文件

    def start_requests(self):
        zhihu_findUrl = 'https://www.zhihu.com/explore'
        #self.loginZhihu()  # 首次使用，先执行login，保存cookies之后便可以注释，
        # 从文件中获取保存的cookies
        with codecs.open('zhihuCookies.json', 'r', encoding='utf-8') as f:
            listcookies = json.loads(f.read())  # 获取cookies
        # 把获取的cookies处理成dict类型
        cookies_dict = dict()
        for cookie in listcookies:
            # 在保存成dict时，我们其实只要cookies中的name和value，而domain等其他都可以不要
            cookies_dict[ cookie[ 'name' ] ] = cookie[ 'value' ]
        print(cookies_dict)
        # Scrapy发起其他页面请求时，带上cookies=cookies_dict即可，同时记得带上header值，
        yield scrapy.Request(url=zhihu_findUrl, cookies=cookies_dict, callback=self.question, headers=self.headers)

if __name__=='__main__':
    cmdline.execute("scrapy runspider zhihu_spider.py".split()) #该指令可以单独运行scrapy，不予要创建scrapy项目