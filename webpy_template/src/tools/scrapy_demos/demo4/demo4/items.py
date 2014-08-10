# -*- coding: utf-8 -*-

# Define here the models for your scraped items
#
# See documentation in:
# http://doc.scrapy.org/en/latest/topics/items.html

import scrapy


class Demo4Item(scrapy.Item):
    # define the fields for your item here like:
    # name = scrapy.Field()
    title = scrapy.Field()
    link  = scrapy.Field()
    image = scrapy.Field()
    desc  = scrapy.Field()
    buy   = scrapy.Field()
    image2= scrapy.Field()
    

    
