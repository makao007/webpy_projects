#encoding:utf8
import os
import sys
import json
import codecs

'''
load json file to database
'''

def to_sql (data):
    sql_filename = "items.sql"
    db_info = {
       'engine': 'mysql', #engine , MySQL
       'user'  : 'root',  #username
       'pawd'  : '1234',  #password
       'name'  : 'smzdm', #database name
       'char'  : 'utf8',  #database character set
    }
    
    def to_db ():
        print os.popen ('mysql -u%s -p%s < %s' % (db_info.get('user'), db_info.get('pawd'), sql_filename)).read()
            
    
    def to_line (s):
        return s.strip().replace('\n',' ').replace('\r',' ').replace("'", "''")
    
    temp = "insert ignore into items (title, link, summary, image, buy, link_md5) values ('%s', '%s', '%s', '%s', '%s', md5('%s')) ;\n"
    with codecs.open(sql_filename,'w', "utf-8") as w:
        w.write ("use %s;\n" % db_info.get('name')) 
        w.write ("set names %s;\n" % db_info.get('char') )
        
        for item in data:
            line = temp % (to_line(item['title']), to_line(item['link']), to_line(item['desc']), \
                           to_line(item['image']), to_line(item['buy']),  to_line(item['link']) )
            w.write(line)
        w.close()
    to_db ()

def load_data (filename):
    return json.load(file(filename))

if __name__ == "__main__":
    if len(sys.argv) != 2:
        print "usage %s <filename>" % sys.argv[0]
        exit(0)
    to_sql(load_data(sys.argv[1]))