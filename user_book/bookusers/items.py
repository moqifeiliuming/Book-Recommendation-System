# -*- coding: utf-8 -*-

# Define here the models for your scraped items
#
# See documentation in:
# https://doc.scrapy.org/en/latest/topics/items.html

import scrapy


class BookusersItem(scrapy.Item):
    # define the fields for your item here like:
    # name = scrapy.Field()
    username=scrapy.Field()  #用户名字
    password=scrapy.Field()
    phone=scrapy.Field()
    name=scrapy.Field()
    address=scrapy.Field()
    email=scrapy.Field()
