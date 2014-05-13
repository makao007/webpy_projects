#!/usr/bin/python  
#coding=utf-8  
  
import gzip
import urllib  
import urllib2  
import StringIO
import cookielib  

def header_dict ():
    chrome_header = '''
        Accept:text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,*/*;q=0.8
        Accept-Encoding:gzip,deflate,sdch
        Accept-Language:en-US,en;q=0.8,zh-CN;q=0.6
        Cache-Control:max-age=0
        Connection:keep-alive
        User-Agent:Mozilla/5.0 (Windows NT 6.3; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/30.0.1599.101 Safari/537.36
        Origin:http://pan.baidu.com
        RA-Sid:3A3E198A-20131112-130401-98590a-5b86cb
        RA-Ver:1.0.0
        X-Requested-With:XMLHttpRequest
        Referer:http://www.cnbeta.com/'''
    header = {}
    for line in chrome_header.strip().split('\n'):
        header[line.strip().split(':',1)[0]] = line.split(':',1)[1]
    return header

def fetch (url, data=None, cookies=None, get_cookie=False):
    url = url.replace(r'\/','/')
    timeout  = 10
    request = urllib2.Request(url)
    for k,v in header_dict().iteritems():
        if k=='X-Requested-With' :
            if 'jsoncallback=' not in url.lower():
                continue
        request.add_header(k,v)
    if cookies is not None:
        request.add_header('Cookie', cookies)
    try:
        if data:
            data = urllib.urlencode(data)
            response = urllib2.urlopen(request, data, timeout)
        else:
            response = urllib2.urlopen(request, timeout=timeout)
        pass
    except IOError :
        print 'Error when download %s' % url
        return ''
    except ValueError:
        print 'Value Error', url
        return ''

    if response.info().get('content-encoding','') == 'gzip' or response.info().get('Content-Encoding', '') == 'gzip':
        content = gzip.GzipFile(fileobj=StringIO.StringIO(response.read())).read()
    else:
        content = response.read()

    if get_cookie:
        return content, response.headers["Set-cookie"]
    else:
        return content