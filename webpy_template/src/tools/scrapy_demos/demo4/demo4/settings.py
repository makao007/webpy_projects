# -*- coding: utf-8 -*-

# Scrapy settings for demo4 project
#
# For simplicity, this file contains only the most important settings by
# default. All the other settings are documented here:
#
#     http://doc.scrapy.org/en/latest/topics/settings.html
#

BOT_NAME = 'demo4'

SPIDER_MODULES = ['demo4.spiders']
NEWSPIDER_MODULE = 'demo4.spiders'

# Crawl responsibly by identifying yourself (and your website) on the user-agent
#USER_AGENT = 'demo4 (+http://www.yourdomain.com)'

ITEM_PIPELINES = {'scrapy.contrib.pipeline.images.ImagesPipeline': 1}