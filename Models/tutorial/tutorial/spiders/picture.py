import scrapy, json
from scrapy import cmdline
from tutorial.items import PicItem  # 导入item

class PicSpider(scrapy.Spider):
    name = "pic_spider"
    def __init__(self,keyword=None,num=1):
        self.num=num
        self.keyword=keyword
        super(PicSpider,self).__init__(self)

        self.allowed_domains = [ "https://image.baidu.com/search/index" ]
        self.start_urls = ["https://image.baidu.com/search/index"]

    def start_requests(self):

        url = 'https://image.baidu.com/search/index'
        pages = self.num;
        keyword = self.keyword

        for i in range(30, 30 * int(pages) + 30, 30):
            params = {
                'tn': 'resultjson_com',
                'ipn': 'rj',
                'ct': str(201326592),
                'is': '',
                'fp': 'result',
                'queryWord': keyword,
                'cl': '2',
                'lm': '-1',
                'ie': 'utf-8',
                'oe': 'utf-8',
                'adpicid': '',
                'st': "",
                'z': '',
                'ic': "",
                "hd": "",
                "latest": "",
                "copyright": "",
                'word': keyword,
                's': '',
                'se': '',
                'tab': '',
                'width': '',
                'height': '',
                'face': "",
                'istype': '2',
                'qc': '',
                'nc': '1',
                'fr': '',
                "expermode": "",
                "force": "",
                'pn': str(i),
                'rn': '30',
                'gsm': '1e',
                '1555038081953': ''
            }

            yield scrapy.FormRequest(url=url, method='GET', formdata=params, callback=self.parse)

    def parse(self,response):


            # message=requests.get(self.start_urls[0], params=params).json().get('data')
            ret = json.loads(response.body)['data']
            for str in ret:
                if str["thumbURL"]!= None:
                    yield PicItem(image_urls=[str["thumbURL"]])



if __name__=="__main__":
    cmdline.execute([ "scrapy", "crawl", "pic_spider" ,"-a","keyword=数学公式","-a","num=10"]).strip()