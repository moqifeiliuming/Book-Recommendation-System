# -*- coding: utf-8 -*-
import scrapy
import  re
from scrapy.selector import Selector

from bookusers.items import BookusersItem
class RatingsSpider(scrapy.Spider):
    name = 'ratings'
    allowed_domains = ['douban.com']
    start_urls = ['https://book.douban.com/subject/3674537/comments']
    '''
        # 获取页面的内容
        def parse(self, response):
            sel = Selector(response)
            book_list = sel.css('#subject_list > ul > li')
            for book in book_list:
                item = BookusersItem()
                try:
                    # strip() 方法用于移除字符串头尾指定的字符（默认为空格）
                    item['book_id'] =str(book.xpath("div[@class='pic']/a/@href").extract()[0].strip()).replace("https://book.douban.com/subject/",'').replace('/','')
                    url=book.xpath("div[@class='pic']/a/@href").extract()[0].strip()
                    url=url+'comments/hot?p=1'
                    yield scrapy.http.Request(url,meta={'item': item},callback=self.parse_ratings)
                except:
                    pass
            #
            nextPage = sel.xpath('//div[@id="subject_list"]/div[@class="paginator"]/span[@class="next"]/a/@href').extract()[
                0].strip()
            if nextPage:
                next_url = 'https://book.douban.com' + nextPage
                yield scrapy.http.Request(next_url, callback=self.parse)
                '''
#评论人的id以及评分以及id
    def parse(self, response):
        sel = Selector(response)
        book_lists = sel.css('#comments > ul > li')
        user_names=[]
        user_ids=book_lists.xpath("div[@class='comment']/h3/span[@class='comment-vote']/a/@data-cid").extract()
        pattern1 = re.compile(r'<a href="https://www.douban.com/people.*?</a>\s*(.*?)\s*<span>.*?</span>')
        pattern2 = re.compile(r'<span class="user-stars allstar(.*?) rating" ')
        stars = pattern1.findall(response.text)
        for j in range(len(stars)):
            if stars[j]:
                stars[j] = int(pattern2.search(stars[j]).group(1))/10
            else:
                stars[j] = 0
        for book_list in book_lists:
            try:
                user_names.append(book_list.xpath("div[@class='comment']/h3/span[@class='comment-info']/a/text()").extract()[0].strip())
            except:
                pass
        for i in range(0,20):
            item=BookusersItem()
            try:
                item['book_id']=str(self.start_urls[0]).replace('https://book.douban.com/subject/','').replace('/comments','').strip()
                item["user_id"]=user_ids[i]
                item["user_name"]=user_names[i]
                item["user_ratings"]=stars[i]
                yield item
            except:
                pass
        urls=['https://book.douban.com/subject/3674537/comments/hot?p={0}'.format(i) for i in range(2,10,1)]
        for url in urls:
            yield scrapy.Request(url, callback=self.parse)