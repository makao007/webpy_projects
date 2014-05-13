#encoding:utf-8
import re
import datetime

from fetch import fetch

'''
<div class="postbox">
          <div class="entry lazyload">
         <a class="a_img" href="http://www.kiees.com/2014/04/29/321505.html" title="发现：男士偏光镜太阳镜  拍下9.9元包邮" target="_blank"><img rel="3" width="150" height="150" class="image-frame" src="http://img02.taobaocdn.com/bao/uploaded/i2/T1bP9CFOXXXXXXXXXX_!!2-item_pic.png_250x250.jpg" alt="男士偏光镜太阳镜  拍下9.9元包邮"></a>
            <h2><a href="http://www.kiees.com/2014/04/29/321505.html" target="_blank">男士偏光镜太阳镜 <span style="color:#bb0200;"> 拍下9.9元包邮</span></a></h2>
             <div class="detail">是2014最为时髦的款式.无论是音乐节现场的明星还是街头的型人，都用它为造型增添一点“拉风”的感觉，热力十足的暖色系、酷感满满的冷色系各有人爱。之前更多的在实用的户外品牌看到的镜面以及彩色镜面纷纷出现在时尚人士脸上，夸张、有新鲜感，且用来跟任何服装相配都有...</div>
            <p class="postmetadata">
            </p><div class="pinglun"><div class="pinglun_left">6分钟前 - 苏坡推荐 - 人气：<span class="red">9</span> - <a href="#" onclick="extdetail(this,321505);return false">展开全文∨</a></div>
            <div class="pinglun_right">
              <span class="navilink"> 
                <a class="imlink_more" target="_blank" href="http://www.kiees.com/2014/04/29/321505.html">详细图文</a> 
                <a class="tracklink imlink_gobuy" rel="nofollow" target="_blank" href="http://redirect.simba.taobao.com/rd?w=unionnojs&amp;f=http%3A%2F%2Fre.taobao.com%2Feauction%3Fe%3D%252BmXQ1%252B%252FAlWQjmraEDZVrLszURhF9EVC5WAcyj9ixhNeLltG5xFicOSZqewpHPyZzW0k6etFv%252BpkksMoNhfgJzGcmjgsAdSjvbdmZ2Sw7KViB3ujUJI0OeA%253D%253D%26ptype%3D100010&amp;k=e2e107a2b72ca1b1&amp;c=un&amp;b=alimm_0&amp;p=mm_44418348_4134203_17088525">去购买&gt;&gt;</a></span>
            </div></div><p></p>
         </div>
          <div style="clear:both"></div>
       </div>
       
<div class="postbox">
          <div class="entry lazyload">
         <a class="a_img" href="http://www.kiees.com/2014/05/13/327027.html" target="_blank"><img rel="31" width="150" height="150" class="image-frame" src="http://img03.taobaocdn.com/imgextra/i3/759183869/T2RFfZXPNaXXXXXXXX_!!759183869.jpg_160x160.jpg" alt="超长待机大字大声大按键老人手机 拍下43元包邮"></a>
            <h2><a href="http://www.kiees.com/2014/05/13/327027.html" target="_blank">超长待机大字大声大按键老人手机 <span style="color:#bb0200;">拍下43元包邮</span></a></h2>
             <div class="detail">大声音大字体大屏老人专用手机 ，大屏幕、大字体、大按键、大铃音，此外SOS一键求救、手电筒等功能也统统支持！超薄机身，小巧玲珑，握持感不错，屏幕显示清晰，待机时间给力，爸妈用正合适。

...</div>
            <p class="postmetadata">
            </p><div class="pinglun"><div class="pinglun_left">1 小时前 - 蜡笔没小新推荐 - 人气：<span class="red">70</span> - <a href="#" onclick="extdetail(this,327027);return false">展开全文∨</a></div>
            <div class="pinglun_right">
              <span class="navilink"> 
                <a class="imlink_more" target="_blank" href="http://www.kiees.com/2014/05/13/327027.html">详细图文</a> 
                <a class="tracklink imlink_gobuy" rel="nofollow" target="_blank" href="http://redirect.simba.taobao.com/rd?w=unionnojs&amp;f=http%3A%2F%2Fre.taobao.com%2Feauction%3Fe%3D8hUA8Bsx5uQjmraEDZVrLhKkcw%252FZTvscF2FCrFXB2oSLltG5xFicOSZqewpHPyZzIe9bj16or1wVlWZt09piMYf9R3WVGkDYom4YddkSJ7yB3ujUJI0OeA%253D%253D%26ptype%3D100010&amp;k=e2e107a2b72ca1b1&amp;c=un&amp;b=alimm_0&amp;p=mm_44011862_4942091_15918246">去购买&gt;&gt;</a></span>
            </div></div><p></p>
         </div>
          <div style="clear:both"></div>
       </div>
'''
 
def extract (content):
    info  = []

    items = re.findall (r'''<a class="a_img" href="([^"]+)" target="_blank"><img rel="\d+" width="150" height="150" class="image-frame" src="([^"]+)" alt="([^"]+)".*?</h2>\s+<div class="detail">(.*?)</div>''', content, re.I|re.S|re.M)
    print len(items)
 
    for item in items:
        tmp = {}
        tmp['url']   = item[0].strip().replace('\n','')
        tmp['title'] = item[2].strip().replace('\n','')
        tmp['image'] = item[1].strip().replace('\n','')
        tmp['summary'] = item[3].strip().replace('\n','')
        info.append (tmp)
    print 'find %d records' % len(items)
    return info
        
    
def insert (info):
    def insert_to_mysql ():
        import MySQLdb    
        conn   = MySQLdb.connect(host="127.0.0.1",user="root",passwd="1234",db="shopping",charset="utf8")  
        cursor = conn.cursor()    
        
        for item in info:
        
            sql    = "select * from item where url = %s "
            param  = (item['url'],)
            n      = cursor.execute (sql, param)
            if n > 0:
                continue 
            sql    = "insert into item (title, image, summary, content, url, show_time, fetch_time, update_time) values (%s,%s,%s,%s,%s,%s,%s,%s) "
            param  = ( item['title'], item['image'], item['summary'], item.get('content',''), item['url'], item.get('show_time',''), datetime.datetime.now(), datetime.datetime.now() )
            n      = cursor.execute (sql, param)
        conn.commit()
        cursor.close()
        conn.close()
        
    insert_to_mysql()

        

def go (url='http://www.kiees.com/'):
    page = fetch (url)
    info = extract (page)
    insert (info)
    
if __name__ == "__main__":
    go ()
    print 'Done'
    