# -*- coding: utf-8 -*-
# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: http://doc.scrapy.org/en/latest/topics/item-pipeline.html
import pymysql as db
class BookusersPipeline(object):
    def __init__(self):
        self.con = db.connect(user="root", passwd="zpc123", host="localhost", db="python", charset="utf8")
        self.cur = self.con.cursor()
        ''' self.cur.execute(
            "create table IF NOT EXISTS douban_use(id int auto_increment primary key,user_id varchar (200),user_name varchar (200))")'''
        self.cur.execute(
            'create table IF NOT EXISTS douban_ratings(id int auto_increment primary key,user_id varchar (200),book_id varchar (200),user_ratings int(5))')
    def process_item(self, item, spider):
        ''' self.cur.execute(
            "insert into douban_use(id,user_id,user_name) values(NULL,%s,%s)",
            (item['user_id'], item['user_name']))'''

        self.cur.execute(
            "insert into douban_ratings(id,user_id,book_id,user_ratings) values(NULL,%s,%s,%s)",
            (item['user_id'], item['book_id'],item['user_ratings']))
        self.con.commit()
        return item