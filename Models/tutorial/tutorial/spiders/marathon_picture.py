import scrapy
from scrapy import cmdline
from scrapy.exceptions import CloseSpider
from scrapy.linkextractors import LinkExtractor
from scrapy.spiders import CrawlSpider, Rule
from tutorial.items import PicItem



class MarathonSpider(CrawlSpider):
    name = "marathon"
    allowed_domains = ["http://iranshao.com"]
    start_urls = ['http://iranshao.com/albums/73209']

    def start_requests(self):
        url = 'http://iranshao.com/albums/73209?page={num}'
        for i in range(10,25):
            yield scrapy.Request(url.format(num=i), callback=self.parse)


    def parse(self, response):

        for url in response.xpath('//img[@alt="2016 深圳南山半程马拉松"]/@src').extract():
            # print(url[:-8])
            yield PicItem(image_urls=[url[:-8]])



if __name__=='__main__':
    cmdline.execute("scrapy crawl marathon".split())
