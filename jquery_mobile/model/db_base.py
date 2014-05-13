#!/usr/bin/env python
# coding: utf-8

import web
import time
import datetime

database = web.database(dbn='mysql', user='root', pw='1234', db='shopping')

class DB_BASE (object):
    db = database
    TBNAME = ''
    
    def __init__(self, table):
        table = table.strip()
        self.TBNAME = table
        
    def add(self, **kwargs):
        return database.insert(self.TBNAME, **kwargs)
        
    def update (self, cond, **kwargs):
        myvar = {cond.get('key'): cond.get('value')}
        
        where = cond.get('key') + '=' + '$' + cond.get('key')
        result = database.update(self.TBNAME, where=where, vars=myvar, **kwargs)
        return result 
    
    def get_by_id(self, cond):
        myvar = {cond.get('key'): cond.get('value')}
        
        where = cond.get('key') + '=' + '$' + cond.get('key')
        result = database.select(self.TBNAME, where=where, vars=myvar)
        if result:
            return result[0]
        else:
            return {}
        
    def get_list (self, order=''):
        if order:
            return database.select (self.TBNAME, order=order)
        return database.select (self.TBNAME)
    
    def make_where (self,pagenum=0, pagesize=50, order_by='', **param):
        
        if type(pagenum) != type(1) or type(pagesize)!=type(1):
            return 0,[]
        
        #limit for safe, just contain the character and space
        # 'a' + 防止当order_by为空时出错 
        if not ('a'+order_by.replace(' ','').replace(',','').replace('_','').replace('-','')).isalpha():
            print 'query DB unsafe, order=',order_by
            return 0,[]
        
        for k in param.keys():
            if not ('a'+k[2:]).isalnum():
                print 'query DB unsafe, condision key=',k
                return 0,[]
         
        offset = max(pagenum - 1, 0) * pagesize
        myvar = {'offset' : offset,
                 'pagesize' : pagesize}
        
        where = " where 1=1 "
        for k,v in param.iteritems():
            if k.startswith('%'):
                where += ' and ' + str(k[1:]) + ' like $' + str(k[1:])
                myvar[k[1:]] = v
                
            elif k.startswith("**"):  #in操作    
                where += ' and ' + str(k[2:]) + ' in $' + str(k[2:])
                myvar[k[2:]] = v
                 
            elif k.startswith("!*"):  #not in 操作
                where += ' and ' + str(k[2:]) + ' not in $' + str(k[2:])
                myvar[k[2:]] = v
                
            elif k.startswith("!="):  #not =
                where += ' and ' + str(k[2:]) + '!=' + str(k[2:])
                myvar[k[2:]] = v
            
            elif k.startswith("<="):  #<= 小于等于
                key_name = str(k[2:])
                where += ' and ' + key_name + '<=$' + key_name + '21'
                myvar[key_name+'21'] = v
            elif k.startswith(">="):  #>= 大于等于
                key_name = str(k[2:])
                where += ' and ' + key_name + '>=$' + key_name + '22'
                myvar[key_name + '22'] = v
                
            elif k.startswith("<"):
                key_name = str(k[1:])
                where += ' and ' + key_name + '<$' + key_name + '11'
                myvar[key_name+'11'] = v
            elif k.startswith(">"):
                key_name = str(k[1:])
                where += ' and ' + str(k[1:]) + '>$' + str(k[1:])+ '12'
                myvar[key_name+'12'] = v
                
            else:
                where += ' and ' + str(k) + '=$' + str(k)
                myvar[k] = v
        
        
        return where, myvar
    
    def query(self, pagenum=0, pagesize=50, order_by='', **param):  
        sql_debug = False
        
        where, myvar = self.make_where(pagenum, pagesize, order_by, **param)
        
        sql = 'select count(*) as amount from ' + self.TBNAME + where
        if sql_debug:
            print sql
            print myvar
        
        count = database.query (sql, vars=myvar)[0].get("amount")
        
        sql = 'select * from ' + self.TBNAME + where
        
        if order_by:
            sql += ' order by ' + order_by + ' '
        sql = sql + ' limit $offset, $pagesize'

        if sql_debug:
            print sql
            print myvar
        result = database.query(sql, vars=myvar)
        return count,list(result)
    
    def exists (self,**param ):
        #是否存在
        where, myvar = self.make_where(1, 1, '', **param)
        
        sql = 'select count(*) as amount from ' + self.TBNAME + where
        count = database.query (sql, vars=myvar)[0].get("amount")
        if count > 0:
            #存在
            return True
        return False  #不存在
    
    def delete (self, keyname, ids=[]):
        for i in ids:
            if not str(i).isdigit():
                return False
            where = keyname + '=' + str(i)
            database.delete(self.TBNAME, where=where)
        return True
    
    def delete_by_id (self, key, value):
        where = key + "=$" + key
        myvar = { key: value }
        return database.delete (self.TBNAME, where=where, vars=myvar)
    
    def origin_sql (self, sql, myvar):
        return database.query (sql, vars=myvar)
        


