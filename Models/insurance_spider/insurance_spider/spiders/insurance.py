import scrapy
import re
import requests
import copy
from scrapy import cmdline
from scrapy.loader import ItemLoader
from scrapy.http import Request
from scrapy.linkextractors import LinkExtractor
from scrapy.spiders import CrawlSpider, Rule
from items import InsuranceSpiderItem
class InsuranceSpider(CrawlSpider):
    name = "insurance"
    allowed_domains = ["bxjg.circ.gov.cn"]
    start_urls = ['http://bxjg.circ.gov.cn/tabid/5254/Default.aspx']
    proc_request=lambda r: r if r.url=='http://bxjg.circ.gov.cn/tabid/5254/Default.aspx' else None
    rules = (
             # Rule(LinkExtractor(allow_domains=allowed_domains, unique=False), cb_kwargs={"page": 16712, 'page_num': 1},
             #      follow=False, process_request=proc_request, callback='call'),
             Rule(LinkExtractor(allow_domains=allowed_domains, unique=False), cb_kwargs={"page": 16713, 'page_num': 5},
                  follow=False, process_request=proc_request, callback='call'),
             # Rule(LinkExtractor(allow_domains=allowed_domains, unique=False), cb_kwargs={"page": 16714, 'page_num': 5},
             #      follow=False, process_request=proc_request, callback='call'),
             # Rule(LinkExtractor(allow_domains=allowed_domains, unique=False), cb_kwargs={"page": 16715, 'page_num': 1},
             #      follow=False, process_request=proc_request, callback='call'),
             # Rule(LinkExtractor(allow_domains=allowed_domains, unique=False), cb_kwargs={"page": 16716, 'page_num': 2},
             #      follow=False, process_request=proc_request, callback='call'),
             # Rule(LinkExtractor(allow_domains=allowed_domains, unique=False), cb_kwargs={"page": 16720, 'page_num': 10},
             #      follow=False, process_request=proc_request, callback='call'),
             # Rule(LinkExtractor(allow_domains=allowed_domains, unique=False), cb_kwargs={"page": 26624, 'page_num': 1},
             #      follow=False, process_request=proc_request, callback='call'),

             )



    def call(self,response,**cb_kwargs):
        page=cb_kwargs['page'] if cb_kwargs else response.meta['page']
        page_num=cb_kwargs['page_num'] if cb_kwargs else response.meta['count']
        for url in response.xpath("//table[contains(@id,'ess_ctr{0}_OrganizationList_rptCompany')]//a[@onclick]".format(page)).re(r"'(.*)\',null"):
            url = response.urljoin(url)
            request=scrapy.Request(url,callback=self.parse_item)
            yield request

        if page_num!=1 :
            # yield Request(response.url,meta={'count':page_num,'page':copy.copy(page)},
            #               callback=self.call,dont_filter=True)#dont_filter要设为True,因为动态网页url不
            print('*************************')

            url=u'http://bxjg.circ.gov.cn/tabid/5254/Default.aspx'
            header={
                "Host": "bxjg.circ.gov.cn",
                "Referer" : "http://bxjg.circ.gov.cn/tabid/5254/Default.aspx",
            }

            return  scrapy.FormRequest.from_response(response,headers=header,callback=self.call,meta={'count':1,'page':copy.copy(page)}
                   ,method='POST',formdata={"__EVENTTARGET":'ess$ctr16713$OrganizationList$lbnNextPage'},dont_filter = True)



    def parse_item(self, response):
        l = ItemLoader(item=InsuranceSpiderItem(), response=response)
        l.add_xpath('name',("//span[contains(@id,'lblComName')]/text()"),re=r'(\S+)')# 可以添加多个xpath到括号里
        l.add_xpath('class_', "//span[re:test(@id,'.*lblComType')]/text()",re=r'(\S+)') #xpath 的texst 函数比contains更灵活
        l.add_css('time', 'tr:nth-child(3) .tdRight1 ::text',re=r'(\S+)') #注意::与前面的字段必须有间隔
        l.add_css('address','tr:nth-child(4) .tdRight1 ::text',re=r'(\S+)')
        l.add_css('phone', 'tr:nth-child(5) .tdRight1 ::text',re=r'(\S+)')
        l.add_css('represent','tr:nth-child(6) .tdRight1 ::text',re=r'(\S+)')
        l.add_css('capital','tr:nth-child(7) .tdRight1 ::text',re=r'(\S+)')
        # add_css(field_name, css, *processors, **kwargs)  processors处理iterator变量，可以跟正则表达式匹配
        l.add_css('register_area','tr:nth-child(8) .tdRight1 ::text',re=r'(\S+)')
        l.add_css('state','#trState span ::text',re=r'(\S+)')
        return l.load_item()


if __name__=='__main__':

    cmdline.execute("scrapy crawl insurance -o items.csv".split())






