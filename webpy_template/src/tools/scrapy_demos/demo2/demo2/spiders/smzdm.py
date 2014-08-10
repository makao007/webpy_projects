# -*- coding: utf-8 -*-
import os
import codecs
import scrapy

"""
匹配单个网页的数据
"""

db_info = {
   'engine': 'mysql', #engine , MySQL
   'user'  : 'root',  #username
   'pawd'  : '1234',  #password
   'name'  : 'smzdm', #database name
   'char'  : 'utf8',  #database character set
}


class SmzdmSpider(scrapy.Spider):
    name = "smzdm"
    allowed_domains = ["www.smzdm.com"]
    start_urls = (
        'http://www.smzdm.com/',
    )



    def parse(self, response):
        sql_filename = 'shop_item.sql'
        sql_filename = os.path.abspath(sql_filename)
        
        def to_utf8 (s):
            temp = s and s[0]
            temp = temp.strip().replace('\n',' ').replace('\r',' ').replace("'", "''")
            return temp
        
        with codecs.open(sql_filename,'w', "utf-8") as w:
            w.write ("use smzdm;\n")
            w.write ("set names %s;\n" % db_info.get('char') )
            line = """ insert ignore into item (title, summary, link, image, link_md5, fetch_time) values ('%s', '%s', '%s', '%s', md5('%s'), now()) ;\n"""
            for i in response.xpath('//div[@class="leftWrap"]/div[@class="list "]'):
                link  = i.xpath('div[@class="listTitle"]/h4[@class="itemName"]/a/@href').extract()
                title = i.xpath('div[@class="listTitle"]/h4[@class="itemName"]/a/text()').extract()
                desc  = i.xpath('div[@class="listRight"]/div[@class="lrInfo"]/text()').extract()
                image = i.xpath('a/img/@src').extract()
                link  = to_utf8(link)
                title = to_utf8(title)
                desc  = to_utf8(desc)
                image = to_utf8(image)
                
                w.write (line % (title, desc, link, image, link))
            w.close()
            
            print os.popen ('mysql -u%s -p%s < %s' % (db_info.get('user'), db_info.get('pawd'), sql_filename)).read()
            