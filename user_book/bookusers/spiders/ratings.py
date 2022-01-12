# -*- coding: utf-8 -*-
import scrapy
import  re
from scrapy.selector import Selector

from bookusers.items import BookusersItem
class RatingsSpider(scrapy.Spider):
    name = 'ratings'
    allowed_domains = ['douban.com']
    start_urls = ['https://book.douban.com/subject/3674537/comments']
#评论人的id以及评分以及id
    def parse(self, response):
        sel = Selector(response)
        book_lists = sel.css('#comments > ul > li')

        for book_list in book_lists:
            item = BookusersItem()
            try:
                item['username']=book_list.xpath("div[@class='comment']/h3/span[@class='comment-info']/a/text()").extract()[0].strip()
                item['password'] ='admin11'
                item['phone'] = '123454'
                item['name'] = 'wujj'
                item['address'] = 'fdafd'
                item['email'] = '134@qq.com'
                yield item
            except:
                pass
        urls=['https://book.douban.com/subject/3674537/comments/hot?p={0}'.format(i) for i in range(2,10,1)]
        for url in urls:
            yield scrapy.Request(url, callback=self.parse)