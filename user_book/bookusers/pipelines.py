# -*- coding: utf-8 -*-
# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: http://doc.scrapy.org/en/latest/topics/item-pipeline.html
import pymysql as db
class BookusersPipeline(object):
    def __init__(self):
        self.con = db.connect(user="root", passwd="zpc123", host="localhost", db="douban", charset="utf8")
        self.cur = self.con.cursor()

    def process_item(self, item, spider):
        self.cur.execute(
            "insert into user_user(id,username,password,phone,name,address,email) values(NULL,%s,%s,%s,%s,%s,%s)",
            (item['username'],item['password'],item['phone'],item['name'],item['address'],item['email']))
        self.con.commit()
        return item