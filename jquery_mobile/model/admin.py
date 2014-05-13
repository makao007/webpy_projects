#!/usr/bin/env python
# coding: utf-8

from db_base import DB_BASE

class Item (DB_BASE):
    def __init__(self,table):
        DB_BASE.__init__(self,table)
    
    def new (self, data):
        if not self.get_by_id ({"key":"url", "value": data['url']}):
            return self.add (**data)
        return None

item = Item('item')


