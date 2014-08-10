#!/usr/bin/env python
# coding: utf-8

urls = (
    '/?',       'controllers.mobile.index',  #首页
    '/p/(\d+)', 'controllers.mobile.index',  #首页，翻页
    '/update',  'controllers.mobile.sync_items',   #爬虫，更新信息
)