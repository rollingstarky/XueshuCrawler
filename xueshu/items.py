# -*- coding: utf-8 -*-

# Define here the models for your scraped items
#
# See documentation in:
# http://doc.scrapy.org/en/latest/topics/items.html

import scrapy

#定义Item
class XueshuItem(scrapy.Item):
    # define the fields for your item here like:
    # name = scrapy.Field()
    title=scrapy.Field()
    link=scrapy.Field()
    author=scrapy.Field()
    publish=scrapy.Field()
    year=scrapy.Field()
    cite=scrapy.Field()
    abstract=scrapy.Field()
    subject=scrapy.Field()
