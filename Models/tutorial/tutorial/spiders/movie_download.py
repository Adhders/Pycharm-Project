import scrapy
from scrapy import cmdline
from scrapy.loader.processors import MapCompose, Join
from tutorial.items import videoItem
from scrapy.linkextractors import LinkExtractor
from scrapy.spiders import CrawlSpider, Rule
from os import path
import os


class videospiderSpider(CrawlSpider):
    name = 'VideoSpider'
    allowed_domains = [ 'eastday.com' ]
    start_urls = [ 'http://video.eastday.com/' ]

    rules = (
        Rule(LinkExtractor(allow=r'video.eastday.com/a/\d+.html'), #提取所有视频的链接地址
             callback='parse_item', follow=True),
    )

    def parse_item(self, response):

        item = videoItem()
        try:
            #从视频页提取元素
            item[ "video_url" ] = response.xpath('//input[@id="mp4Source"]/@value').extract()[ 0 ]
            item[ "video_title" ] = response.xpath('//meta[@name="description"]/@content').extract()[ 0 ]
            # print(item)
            item[ "video_url" ] = 'http:' + item[ 'video_url' ]
            yield scrapy.Request(url=item[ 'video_url' ], meta=item, callback=self.parse_video)
        except:
            pass

    def parse_video(self, response):

        i = response.meta
        file_name = Join()([ i[ 'video_title' ], '.mp4' ])
        base_dir = path.join(path.curdir, 'Video')
        print(base_dir)
        video_local_path = path.join(base_dir, file_name.replace('?', ''))

        i[ 'video_local_path' ] = video_local_path

        if not os.path.exists(base_dir):
            os.mkdir(base_dir)

        with open(video_local_path, "wb") as f:
            f.write(response.body)

        yield i

if __name__=="__main__":
    cmdline.execute(["scrapy", "crawl","VideoSpider"]).strip()
