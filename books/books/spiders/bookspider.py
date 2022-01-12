# -*- coding: utf-8 -*-
from urllib import parse

import scrapy
from scrapy.selector import Selector
from books.items import BooksItem
import os
import requests


class BookspiderSpider(scrapy.Spider):
    name = "bookspider"
    allowed_domains = ["book.douban.com"]
    start_urls = ['https://book.douban.com/tag/历史']

    # 获取页面的内容
    def parse(self, response):
        sel = Selector(response)
        book_list = sel.css('#subject_list > ul > li')
        for book in book_list:
            item = BooksItem()
            try:
                # strip() 方法用于移除字符串头尾指定的字符（默认为空格）
                book_ids = book.xpath("div[@class='pic']/a/@href").extract_first().strip().replace(
                    "https://book.douban.com/subject/", '').replace('/', '')
                #              item['book_url']=book.xpath("div[@class='pic']/a/@href").extract()[0].strip()
                title = book.xpath('div[@class="info"]/h2/a/text()').extract()[0].strip()
                item['title'] = title
                item['book_star'] = book.xpath("div[@class='info']/div[2]/span[@class='rating_nums']/text()").extract()[
                    0].strip()
                item['pic'] = 's'+book_ids+'.jpg'
                item['book_pl'] = int(str(book.xpath("div[@class='info']/div[2]/span[@class='pl']/text()").extract()[0].strip()).replace("[","").replace(']','').replace("(","").replace("人评价)",""))
                books_img_url = book.xpath("div[@class='pic']/a[@class='nbg']/img/@src").extract()[0].strip()
                books=book.xpath("div[@class='info']/p/text()").extract()
                bookSting=''
                for book1 in books:
                    boo1=str(book1).replace('\n','').replace(' ','').strip()
                    bookSting=bookSting+boo1
                item['intro'] =bookSting
                pub = book.xpath('div[@class="info"]/div[@class="pub"]/text()').extract()[0].strip().split('/')
                item['book_price'] = pub.pop()
                item['book_date'] = pub.pop()
                item['book_publish'] = pub.pop()
                item['author'] = '/'.join(pub)
                if os.path.exists('book_cover'):
                    pass
                else:
                    os.mkdir('book_cover')
                with open('book_cover/' + 's' + book_ids + '.jpg', 'wb') as fd:
                    picture = requests.get(books_img_url).content
                    fd.write(picture)
                    fd.close()
                yield item
            except:
                pass
        #
        nextPage = sel.xpath('//div[@id="subject_list"]/div[@class="paginator"]/span[@class="next"]/a/@href').extract()[0].strip()

        if nextPage:
            next_url = 'https://book.douban.com' +nextPage
            yield scrapy.http.Request(next_url, callback=self.parse)
