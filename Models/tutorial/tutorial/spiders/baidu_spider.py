import re
from scrapy import cmdline
from scrapy.exceptions import CloseSpider
from scrapy.linkextractors import LinkExtractor
from scrapy.http import Request
from scrapy.spiders import CrawlSpider, Rule
from tutorial.items import DmozItem

global count
count=0

# http://image.baidu.com/search/index?tn=baiduimage&ps=1&ct=201326592&lm=-1&cl=2&nc=1&ie=utf-8&word=%E5%9B%BE%E7%89%87


class DmozSpider(CrawlSpider):
    name = "baidu"
    allowed_domains = ["baike.baidu.com"]
    start_urls = ['https://baike.baidu.com/item/%E9%87%91%E8%9E%8D%E4%BD%93%E7%B3%BB/2389250']
    rules=(Rule(LinkExtractor(allow_domains="baike.baidu.com",restrict_xpaths=
        '//a[contains(@href,"item")]',unique=True),follow=True,callback='parse_item'),)
    #CrawlSpider 不能自定义parse函数
    def parse_item(self, response):
        item = DmozItem()
        text=response.xpath('//title/text()')
        texts=re.split("（|_",text.extract_first())[0]
        item['question']=texts
        string = []
        for i,text in enumerate(response.xpath('//meta[@name="description"]/@content')):
            string.append(text.extract())
        global count
        count = count + 1
        if count > 100:
            raise CloseSpider()  #也可以通过定义时间，和pagecount来closespider
        item['answer']=''.join(string)
        yield item  #注意该yield不可以省略

        #print(text.xpath('.//text()').extract_first()) #只有text()属性才有extract_first()方法
        # link=LinkExtractor(allow_domains="baike.baidu.com",restrict_xpaths='//a[contains(@href,"item")]',unique=True)
        # links=link.extract_links(response)
        # for link in links:
        #     url=link.url
        #     yield Request(url,callback=self.parse_item,meta=item,dont_filter=False)

        for url in response.xpath('//a[contains(@href,"item")]/@href'):
            url=response.urljoin(url.extract())  #urljoin可以获得绝地路径
            yield Request(url,callback=self.parse_item,meta=item,dont_filter=False)

if __name__=='__main__':
    cmdline.execute("scrapy crawl baidu -o items.csv".split())

