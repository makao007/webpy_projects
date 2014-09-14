#encoding:utf8

import urllib

import sys
reload(sys)
sys.setdefaultencoding('utf-8')

import web

class index:
    def fetch (self, q, i):
        pass
    
    def decry (self, keyword):
        return urllib.unquote(keyword[::2].replace('^', '%'))
    
    def GET(self):
        keyword = web.input('name','')
        index   = web.input('index',0)
        
        return render ('/mobile/index.html', data=data)
    
