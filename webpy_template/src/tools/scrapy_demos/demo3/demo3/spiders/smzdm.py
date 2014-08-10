# -*- coding: utf-8 -*-
import scrapy
from scrapy.contrib.spiders import CrawlSpider, Rule
from scrapy.contrib.linkextractors import LinkExtractor
from scrapy.contrib.linkextractors.sgml import SgmlLinkExtractor

from scrapy import signals
from scrapy.xlib.pydispatch import dispatcher
from scrapy.signalmanager import SignalManager

"""
从开始页中提取匹配的链接，找出下一级的网页，在下一级的网页中找出数据
当爬虫结束时，调用 closed_handler方法
"""

class SmzdmSpider(CrawlSpider):
    name = "smzdm"
    allowed_domains = ["smzdm.com"]
    start_urls = (
        'http://www.smzdm.com/',
    )

    rules = (
          Rule(SgmlLinkExtractor(allow=('/tag/[^/]+', )), callback='parse_item'),
    )
    
    def __init__(self,*args, **kwargs):
        super(SmzdmSpider, self).__init__(*args, **kwargs)
        SignalManager(dispatcher.Any).connect(self.closed_handler, signal=signals.spider_closed)
        #dispatcher.connect(self.spider_closed, signals.spider_closed)
        
    
    def parse_item(self, response):
        self.log('Hi, this is an item page! %s' % response.url)
        #print response.xpath('//h3[@class="itemName"]/a/text()').extract()
      
    def closed_handler(self, spider):
      # second param is instance of spder about to be closed.
        print "task finish, going to exis"