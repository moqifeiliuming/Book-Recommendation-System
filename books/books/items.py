# -*- coding: utf-8 -*-
# Define here the models for your scraped items
# See documentation in:
# http://doc.scrapy.org/en/latest/topics/items.html
import scrapy
class BooksItem(scrapy.Item):

    #sump=scrapy.Field() #收藏量
    #new_books=scrapy.Field() #新书
    title = scrapy.Field()  # 图书名
    pic=scrapy.Field()#图片地址
    book_star = scrapy.Field()  # 图书评分
    book_pl = scrapy.Field()  # 图书评论数
    author = scrapy.Field()  # 图书作者
    book_publish = scrapy.Field()  # 出版社
    book_date = scrapy.Field()  # 出版日期
    book_price = scrapy.Field()  # 图书价格
    #tags_id=scrapy.Field()  #类型
    #num=scrapy.Field()#浏览量
    intro=scrapy.Field()  # 图书的简介
    book_url = scrapy.Field()  # 书籍的url
   # book_img_url=scrapy.Field()  # 图书的图片

