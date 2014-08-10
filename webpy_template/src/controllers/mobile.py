#!/usr/bin/env python
# coding: utf-8

import os

from models.db import db_session, Shop, User

from scripts import utils
from scripts.utils import render


class index:
    def GET(self, index=0):
        index  = int(index)
        length = 10
        data = {}
        data['records'] = db_session.query (Shop).order_by(-Shop.id).all()[index*length: (1+index)*length]
        data['index']   = index
        data['length']  = length
        return render ('/mobile/items.html', data = data)
    
class sync_items:
    def sync (self):
        os.system("sh tools/scrapy_demos/demo4/script/crawl.sh")
    
    def GET(self):
        self.sync ()
        return "update finished"

