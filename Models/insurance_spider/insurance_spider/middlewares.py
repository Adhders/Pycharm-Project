# -*- coding: utf-8 -*-

# Define here the models for your spider middleware
#
# See documentation in:
# https://doc.scrapy.org/en/latest/topics/spider-middleware.html

import time
from scrapy import signals
from scrapy.http import HtmlResponse
from selenium import webdriver

class InsuranceSpiderSpiderMiddleware(object):
    # Not all methods need to be defined. If a method is not defined,
    # scrapy acts as if the spider middleware does not modify the
    # passed objects.

    @classmethod
    def from_crawler(cls, crawler):
        # This method is used by Scrapy to create your spiders.
        s = cls()
        crawler.signals.connect(s.spider_opened, signal=signals.spider_opened)
        return s

    def process_spider_input(self, response, spider):
        # Called for each response that goes through the spider
        # middleware and into the spider.

        # Should return None or raise an exception.
        return None

    def process_spider_output(self, response, result, spider):
        # Called with the results returned from the Spider, after
        # it has processed the response.

        # Must return an iterable of Request, dict or Item objects.
        for i in result:
            yield i

    def process_spider_exception(self, response, exception, spider):
        # Called when a spider or process_spider_input() method
        # (from other spider middleware) raises an exception.

        # Should return either None or an iterable of Response, dict
        # or Item objects.
        pass

    def process_start_requests(self, start_requests, spider):
        # Called with the start requests of the spider, and works
        # similarly to the process_spider_output() method, except
        # that it doesn’t have a response associated.

        # Must return only requests (not items).
        for r in start_requests:
            yield r

    def spider_opened(self, spider):
        spider.logger.info('Spider opened: %s' % spider.name)


class InsuranceSpiderDownloaderMiddleware(object):
    # Not all methods need to be defined. If a method is not defined,
    # scrapy acts as if the downloader middleware does not modify the
    # passed objects.

    @classmethod
    def from_crawler(cls, crawler):
        # This method is used by Scrapy to create your spiders.
        s = cls()
        crawler.signals.connect(s.spider_opened, signal=signals.spider_opened)
        return s

    def process_request(self, request, spider):
        # Called for each request that goes through the downloader
        # middleware.

        # Must either:
        # - return None: continue processing this request
        # - or return a Response object
        # - or return a Request object
        # - or raise IgnoreRequest: process_exception() methods of
        #   installed downloader middleware will be called
        return None

    def process_response(self, request, response, spider):
        # Called with the response returned from the downloader.

        # Must either;
        # - return a Response object
        # - return a Request object
        # - or raise IgnoreRequest
        return response

    def process_exception(self, request, exception, spider):
        # Called when a download handler or a process_request()
        # (from other downloader middleware) raises an exception.

        # Must either:
        # - return None: continue processing this exception
        # - return a Response object: stops process_exception() chain
        # - return a Request object: stops process_exception() chain
        pass

    def spider_opened(self, spider):
        spider.logger.info('Spider opened: %s' % spider.name)






import random
class RandomUserAgent(object):

    def __init__(self,agents):
        self.agents=agents

    @classmethod
    def from_crawler(cls,crawler):
        return cls(crawler.settings.getlist('USER_AGENTS'))
    def process_request(self,request,spider):
        request.headers.setdefault('User-Agent',random.choice(self.agents))




class PhantomJSMiddleware(object):
    @classmethod
    def process_request(cls, request, spider):

        # if  'count' in request.meta:
        #     driver=webdriver.Firefox()
        #     driver.get(request.url)
        #
        #     js="""var theForm = document.forms['Form'];
        #           if (!theForm) {
        #               theForm = document.Form;
        #           }
        #           function __doPostBack(eventTarget, eventArgument) {
        #               if (!theForm.onsubmit || (theForm.onsubmit() != false)) {
        #                   theForm.__EVENTTARGET.value = eventTarget;
        #                   theForm.__EVENTARGUMENT.value = eventArgument;
        #                   theForm.submit();
        #               }
        #           }
        #        """
        #     js_num="""__doPostBack('ess$ctr{0}$OrganizationList$lbnToPage','3')"""
        #     driver.execute_script(js)
        #     # count=request.meta['count']
        #
        #     driver.execute_script(js_num.format(request.meta['page']))
        #     time.sleep(2)
        #     content = driver.page_source.encode('utf-8')
        #     # count -=1
        #     request.meta['count'] =1
        #     return HtmlResponse(request.url, encoding='utf-8', body=content, request=request)
        return request

