# -*- coding: utf-8 -*-

# Define here the models for your scraped items
#
# See documentation in:
# https://doc.scrapy.org/en/latest/topics/items.html

import scrapy


class InsuranceSpiderItem(scrapy.Item):
    # define the fields for your item here like:
    name=scrapy.Field()
    class_=scrapy.Field()
    time=scrapy.Field()
    address=scrapy.Field()
    phone=scrapy.Field()
    represent=scrapy.Field()
    capital=scrapy.Field()
    register_area=scrapy.Field()
    state=scrapy.Field()
    pass

