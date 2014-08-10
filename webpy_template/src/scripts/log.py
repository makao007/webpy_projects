#!/usr/bin/env python
# coding: utf-8

import logging  
from logging.handlers import RotatingFileHandler
                              
try:                                                                                             
    from config.site import debug
except ImportError:
    import os,sys
    sys.path.append (os.path.dirname(os.path.dirname(os.path.abspath(__file__)))) 
    import config
    debug =  config.site.debug

# 创建一个logger  
logger = logging.getLogger()  
logger.setLevel(debug.get('level'))    #低于这个水平的不会写入到日志
  

#创建一个handler, 当文件超过最大的限制时，自动写到下一个文件，有最大的备份
ff = RotatingFileHandler (debug.get('path'), maxBytes=debug.get('file_size'), backupCount=debug.get('files_amount'))
ff.setLevel(logging.DEBUG) 
  
# 再创建一个handler，用于输出到控制台  
ch = logging.StreamHandler()  
ch.setLevel(logging.DEBUG)  
  
# 定义handler的输出格式  
formatter = logging.Formatter('%(asctime)s -%(name)s -%(levelname)s %(filename)s[line:%(lineno)s] __ %(message)s')  
ch.setFormatter(formatter) 
ff.setFormatter(formatter) 
  
# 给logger添加handler  
logger.addHandler(ch) 
logger.addHandler(ff) 


if __name__ == "__main__":
    # 记录一条日志  
    logger.info ('this is a test for writing info log')
    logger.debug('this is a test for writing debug log')  
    logger.warning('this is a test for writing warning log')
    logger.error('this is a test for writing error log')  
    logger.critical('this is a test for writing critical log')
