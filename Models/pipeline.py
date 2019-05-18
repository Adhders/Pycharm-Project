"""
      In this example we’ll write items to MongoDB using pymongo. MongoDB address
and  database name are specified in Scrapy settings; MongoDB collection is named
after item class.

"""


import pymongo

class MongoPipeline(object):

    collection_name = 'scrapy_items'

    def __init__(self, mongo_uri, mongo_db):
        self.mongo_uri = mongo_uri
        self.mongo_db = mongo_db

    @classmethod
    def from_crawler(cls, crawler):
        return cls(
            mongo_uri=crawler.settings.get('MONGO_URI'),
            mongo_db=crawler.settings.get('MONGO_DATABASE', 'items')
        ) # 'items'表示collection

    def open_spider(self, spider):
        self.client = pymongo.MongoClient(self.mongo_uri)
        self.db = self.client[self.mongo_db]

    def close_spider(self, spider):
        self.client.close()

    def process_item(self, item, spider):
        self.db[self.collection_name].insert(dict(item))
        return item
"""
将数据存储在sqlite中
"""

import sqlite3


class Sqlite3Pipeline(object):

    def __init__(self, sqlite_file, sqlite_table):
        self.sqlite_file = sqlite_file
        self.sqlite_table = sqlite_table

    @classmethod
    def from_crawler(cls, crawler):
        return cls(
            sqlite_file=crawler.settings.get('SQLITE_FILE'),  # 从 settings.py 提取
            sqlite_table=crawler.settings.get('SQLITE_TABLE')
        )

    def open_spider(self, spider):
        self.conn = sqlite3.connect(self.sqlite_file)
        self.cur = self.conn.cursor()

    def close_spider(self, spider):
        self.conn.close()

    def process_item(self, item, spider):
        insert_sql = "insert into insurance(phone, name) values({}, {})".format(item["phone"], item["name"])
        self.cur.execute(insert_sql)
        self.conn.commit()

        return item






















from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
# 替换mysqldb模块
import pymysql
pymysql.install_as_MySQLdb()
# 在Pipeline.py文件中定义用于接收并保存数据到Mysql数据库的类型
class mysqlPipeline(object):
    '''
    定义__init__函数，用于初始化数据，可用于打开文件、打开数据库连接等，必要时写
    '''
    def __init__(self):
        # 在这里与数据库建立连接
        # 创建引擎对象
        self.engine=create_engine("mysql://root:0@localhost/python_spider?charset=utf8")
        # 创建会话构建对象
        Session=sessionmaker(bind=self.engine)
        self.session=Session()

    def open_spider(self,spider):
        '''
        爬虫开启时需要调用的函数，经常用于数据初始化

        :param spider:
        :return:
        '''
        pass
    def close_spider(self,spider):
        '''
        爬虫程序关闭时自动调用的而寒暑，经常用于做一些资源回收的工作，
        如关闭和数据库的会话连接
        :param spider:
        :return:
        '''
        pass
        self.session.close()

    def process_item(self,item,spider):
        '''
        核心处理模块，该函数会接受爬虫程序已经封装好的item对象，
        通过sql语句，将数据存储在数据库中
        :param item:
        :param spider:
        :return:
        '''
        print("正在保存数据到数据库")
        sql="insert into job(job_name,company,salary) values('%s','%s','%s')"\
             %(item['job_name'],item['company'],item['salary'])
        # 执行sql语句
        self.session.execute(sql)
        self.session.commit()



import json

class JsonWriterPipeline(object):

    def open_spider(self, spider):
        self.file = open('items.jl', 'w')

    def close_spider(self, spider):
        self.file.close()

    def process_item(self, item, spider):
        line = json.dumps(dict(item)) + "\n"
        self.file.write(line)
        return item





# A filter that looks for duplicate items, and drops those items that were
# already processed. Let’s say that our items have a unique id, but our spider
# returns multiples items with the same id
from scrapy.exceptions import DropItem

class DuplicatesPipeline(object):

    def __init__(self):
        self.ids_seen = set()

    def process_item(self, item, spider):
        if item['id'] in self.ids_seen:
            raise DropItem("Duplicate item found: %s" % item)
        else:
            self.ids_seen.add(item['id'])
            return item






"""This example demonstrates how to return Deferred from process_item() method.
  It uses Splash to render screenshot of item url. Pipeline makes request to
  locally running instance of Splash. After request is downloaded and Deferred 
  callback fires, it saves item to a read and adds filename to an item."""


import scrapy
import hashlib
from urllib.parse import quote


class ScreenshotPipeline(object):
    """Pipeline that uses Splash to render screenshot of
    every Scrapy item."""

    SPLASH_URL = "http://localhost:8050/render.png?url={}"

    def process_item(self, item, spider):
        encoded_item_url = quote(item["url"])
        screenshot_url = self.SPLASH_URL.format(encoded_item_url)
        request = scrapy.Request(screenshot_url)
        dfd = spider.crawler.engine.download(request, spider)
        dfd.addBoth(self.return_item, item)
        return dfd

    def return_item(self, response, item):
        if response.status != 200:
            # Error happened, return item.
            return item

        # Save screenshot to read, filename will be hash of url.
        url = item["url"]
        url_hash = hashlib.md5(url.encode("utf8")).hexdigest()
        filename = "{}.png".format(url_hash)
        with open(filename, "wb") as f:
            f.write(response.body)

        # Store filename in item.
        item["screenshot_filename"] = filename
        return item