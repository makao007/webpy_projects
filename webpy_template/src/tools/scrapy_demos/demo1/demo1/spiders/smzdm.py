# -*- coding: utf-8 -*-
import scrapy

from demo1.items import Demo1Item

class SmzdmSpider(scrapy.Spider):
    name = "smzdm"
    allowed_domains = ["smzdm.com"]
    start_urls = (
        'http://www.smzdm.com/',
    )

    def parse (self, response):
        
        for i in response.xpath('//div[@class="leftWrap"]/div[@class="list "]'):
            title = i.xpath('div[@class="listTitle"]/h4[@class="itemName"]/a/text()').extract()
            link  = i.xpath('div[@class="listTitle"]/h4[@class="itemName"]/a/@href').extract()
            desc  = i.xpath('div[@class="listRight"]/div[@class="lrInfo"]/text()').extract()
            image = i.xpath('a/img/@src').extract()
            buy   = i.xpath('div[@class="listRight"]/div[@class="lrBot"]/div[@class="botPart"]/div[@class="buy"]/a/@href').extract()
            item  = Demo1Item()
            item['title'] = title and title[0] or ''
            item['link']  = link and link[0] or ''
            item['desc']  = desc and desc[0] or ''
            item['buy']   = buy and buy[0] or ''
            item['image_urls'] = image
            
            yield item
