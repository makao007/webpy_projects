# -*- coding: utf-8 -*-

# Scrapy settings for demo1 project
#
# For simplicity, this file contains only the most important settings by
# default. All the other settings are documented here:
#
#     http://doc.scrapy.org/en/latest/topics/settings.html
#

BOT_NAME = 'demo1'

SPIDER_MODULES = ['demo1.spiders']
NEWSPIDER_MODULE = 'demo1.spiders'

# Crawl responsibly by identifying yourself (and your website) on the user-agent
#USER_AGENT = 'demo1 (+http://www.yourdomain.com)'

ITEM_PIPELINES = {'scrapy.contrib.pipeline.images.ImagesPipeline': 1}
IMAGES_STORE = './images/'
IMAGES_EXPIRES = 90
