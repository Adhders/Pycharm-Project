# -*- coding: utf-8 -*-

# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: https://doc.scrapy.org/en/latest/topics/item-pipeline.html
class MissingValue(object):
    def proces_item(self,item,spider):
        for key in item.fields.keys():
            if  item[key]==['']:
                print('------%s-------'%key)
                item[key]=['None']
        return item


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
            mongo_db=crawler.settings.get('MONGO_DATABASE')
        )

    def open_spider(self, spider):
        self.client = pymongo.MongoClient(self.mongo_uri)
        self.db = self.client[self.mongo_db]

    def close_spider(self, spider):
        self.client.close()

    def process_item(self, item, spider):
        self.db[self.collection_name].insert(dict(item))
        return item



import sqlite3


class Sqlite3Pipeline(object):

    def __init__(self, sqlite_file ,sqlite_table):
        self.sqlite_file = sqlite_file
        self.sqlite_table = sqlite_table

    @classmethod
    def from_crawler(cls, crawler):
        return cls(
            sqlite_file=crawler.settings.get('SQLITE_FILE'),  # 从 settings.py 提取
            sqlite_table=crawler.settings.get('SQLITE_TABLE','INDEX')
        )

    def open_spider(self, spider):
        self.conn = sqlite3.connect(self.sqlite_file)
        self.cur = self.conn.cursor()

    def close_spider(self, spider):
        self.conn.close()

    def process_item(self, item, spider):
        self.cur.execute('CREATE TABLE IF NOT EXISTS %s (%s)' %(self.sqlite_table,','.join(item.fields.keys())))
        insert_sql = "insert into {0} ({1}) values ({2})".format(self.sqlite_table,
                                                                 ','.join(item.fields.keys()),
                                                                 ','.join([ '?' ] * len(item.fields.keys())))


        self.cur.execute(insert_sql,[u''.join(item[x]) for x in item.fields.keys()])

        self.conn.commit()

        return item
