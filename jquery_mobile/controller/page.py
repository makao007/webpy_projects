#encoding:utf-8
import web
from lib.utils import render
from model.admin import item as m_item

class index:
    def GET (self):
        return render ('index.html')
    
class items : 
    def GET (self):
        items = m_item.query (0,100, 'id desc', **{})
        return render ('items.html', items=items[1])
    
class item : 
    def GET (self, xid):
        assert (str(xid).isdigit())
        item  = m_item.get_by_id ({"key":"id", "value": xid})
        return render ('item.html', item=item)