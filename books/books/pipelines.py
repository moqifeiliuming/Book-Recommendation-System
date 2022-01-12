# -*- coding: utf-8 -*-
# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: http://doc.scrapy.org/en/latest/topics/item-pipeline.html

import pymysql as db

class BooksPipeline(object):
    def __init__(self):
        self.con = db.connect(user="root", passwd="zpc123", host="localhost", db="douban", charset="utf8")
        self.cur = self.con.cursor()


    def process_item(self, item, spider):
        self.cur.execute(
            "insert into user_book(id,sump,new_books,title,author,book_star,book_pl,book_publish,book_date,book_price,intro,num,pic,tags_id) values(NULL,0,FALSE ,%s,%s,%s,%s,%s,%s,%s,%s,0,%s,NULL )",
            (item['title'],item['author'],item['book_star'], item['book_pl'], item['book_publish'],item['book_date'], item['book_price'], item['intro'],item['pic']))
        self.con.commit()
        return item