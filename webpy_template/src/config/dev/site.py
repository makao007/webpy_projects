#!/usr/bin/env python
# coding: utf-8
#这里存放一些配置信息， 一般与所处的运行环境无关

import os
import logging

root = os.path.dirname(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))   #项目根路径

info = {
    'project_dir': root,
    'templates'  : os.path.join(root, 'views'),
}

#调试信息
debug = {
    'log': True,
    'log_dir': os.path.join( os.path.dirname(info['project_dir']), 'data', 'debuglog'),
    'log_file': 'webpy_log.log',
    'name': 'WebpyLogger',
    'level': logging.DEBUG,          #低于这个水平的不会写入
    'files_amount':  10,             #保留10个日志文件
    'file_size': 1024 * 1024 * 10,   #每个日志文件10MB
}
debug['path'] = os.path.join(debug['log_dir'], debug['log_file'])

#cookie session 信息
cookie = {
    'name': 'cookie_name',
    'path': '/',
    'domain' : '/',
    'timeout': 60*60*24*7,  #秒数为单位, 
    'message': 'the cookie timeout',
    'secretkey': 'fLjUfxqXtfN^2AXD23A(5-!E23ADAasoIldA0A0JasdfASD3adA',
    'dir_path' : os.path.join (os.path.dirname(info['project_dir']), 'data', 'sessions')
}

#字符集
character = {
    'content_type': "text/html; charset=utf-8",
}

db = {
    'engine': 'mysql',
    'name'  : 'smzdm',
    'user'  : 'root',
    'pawd'  : '1234',
    'port'  : 3306,
    'host'  : '127.0.0.1',   #localhost not work
    'char'  : 'utf8',
    'log'   : True,  #show log 
    'adapt' : "+pymysql"
}