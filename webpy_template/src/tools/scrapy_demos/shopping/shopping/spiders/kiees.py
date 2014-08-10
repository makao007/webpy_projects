# -*- coding: utf-8 -*-
import scrapy


class KieesSpider(scrapy.Spider):
    name = "kiees"
    allowed_domains = ["www.kiees.com/"]
    start_urls = (
        'http://www.www.kiees.com//',
    )

    def parse(self, response):
        pass
