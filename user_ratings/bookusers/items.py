# -*- coding: utf-8 -*-

# Define here the models for your scraped items
#
# See documentation in:
# https://doc.scrapy.org/en/latest/topics/items.html

import scrapy


class BookusersItem(scrapy.Item):
    # define the fields for your item here like:
    # name = scrapy.Field()
    book_id = scrapy.Field()  # 书籍的ID
    user_id=scrapy.Field()    #用户id
    user_name=scrapy.Field()  #用户名字
    user_ratings =scrapy.Field() #用户的评分
