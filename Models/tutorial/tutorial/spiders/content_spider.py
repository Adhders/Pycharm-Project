import scrapy

from scrapy.http import Request
from selenium import webdriver
from tutorial.items import DmozItem
from scrapy.utils.project import get_project_settings
from scrapy.crawler import CrawlerProcess

class DmozSpider(scrapy.Spider):
    name = "dmoz"
    allowed_domains = ["bxjg.circ.gov.cn"]

    def start_requests(self):
        url = 'http://bxjg.circ.gov.cn/web/site47/tab438{num}/'
        for i in range(6, 9):
            yield scrapy.Request(url.format(num=i), callback=self.parse)
    # DLL load failed: The operating system cannot run %1
    def parse(self, response):

        for i, text in enumerate(response.css('#ess_ContentPane a')):
            item=DmozItem()
            #url=text.css('a::attr(href)').extract_first()
            url=text.xpath('.//@href').extract_first()  #注意嵌套css'.'不可以省去
            if url:
                url='http://bxjg.circ.gov.cn/'+url
                item[ 'question' ] = text.xpath('@title').extract_first()
                yield Request(url,callback=self.parse2,meta={'item':item},dont_filter=True)

    def parse2(self, response):
        string=['']
        for text in response.xpath('//p//text()'): #注意p后面是'//'
            string.append(text.extract())
        item = response.meta[ 'item' ]
        item['answer']=''.join(string)
        yield item

if __name__=='__main__':
    process=CrawlerProcess(get_project_settings())
    process.crawl('dmoz')
    process.start()



