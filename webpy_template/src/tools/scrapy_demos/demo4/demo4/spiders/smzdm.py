# -*- coding: utf-8 -*-
import scrapy
from scrapy.contrib.spiders import CrawlSpider, Rule
from scrapy.contrib.linkextractors import LinkExtractor
from scrapy.contrib.linkextractors.sgml import SgmlLinkExtractor

from scrapy import signals
from scrapy.xlib.pydispatch import dispatcher
from scrapy.signalmanager import SignalManager

from demo4.items import Demo4Item

"""
从开始页中提取匹配的链接，找出下一级的网页，在下一级的网页中找出数据
"""

class SmzdmSpider(CrawlSpider):
    max_page = 3
    cur_page = 0
    name = "smzdm"
    allowed_domains = ["smzdm.com"]
    start_urls = (
        'http://www.smzdm.com/',
    )

    rules = (
          Rule(SgmlLinkExtractor(allow=('/p\d+', )), callback='parse_items', follow=False),
    )
    
    def parse_items(self, response):
        '''
        if self.cur_page >= self.max_page:
            exit(0)
        else:
            self.cur_page += 1
        '''
        self.log('Hi, this is an item page! %s' % response.url)
        
        for i in response.xpath('//div[@class="leftWrap"]/div[@class="list "]'):
            title = i.xpath('div[@class="listTitle"]/h4[@class="itemName"]/a/text()').extract()
            link  = i.xpath('div[@class="listTitle"]/h4[@class="itemName"]/a/@href').extract()
            desc  = i.xpath('div[@class="listRight"]/div[@class="lrInfo"]/text()').extract()
            image = i.xpath('a/img/@src').extract()
            buy   = i.xpath('div[@class="listRight"]/div[@class="lrBot"]/div[@class="botPart"]/div[@class="buy"]/a/@href').extract()
            item  = Demo4Item()
            item['title'] = title and title[0] or ''
            item['link']  = link and link[0] or ''
            item['desc']  = desc and desc[0] or ''
            item['image'] = image and image[0] or ''
            item['buy']   = buy and buy[0] or ''
            
            yield item
