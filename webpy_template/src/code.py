#!/usr/bin/env python
# coding: utf-8

import web

import config
from url import urls

web.config.debug = config.site.debug.get('log')

webapp = web.application(urls, globals())
if web.config.get("_session") is None:
    session = web.session.Session(webapp, web.session.DiskStore(config.site.cookie.get('dir_path')))
    web.config._session = session
else:
    session = web.config._session
    

def my_loadhook():
    web.header('Content-type', config.site.character.get('content_type'))
webapp.add_processor(web.loadhook(my_loadhook))

def session_hook():
    web.ctx.session = session
webapp.add_processor(web.loadhook(session_hook))

web.config.session_parameters['timeout']         = config.site.cookie.get('timeout') 
web.config.session_parameters['cookie_name']     = config.site.cookie.get('name') 
web.config.session_parameters['cookie_path']     = config.site.cookie.get('path') 
web.config.session_parameters['cookie_domain']   = config.site.cookie.get('domain')
web.config.session_parameters['secret_key']      = config.site.cookie.get('secretkey') 
web.config.session_parameters['expired_message'] = config.site.cookie.get('message')

application = webapp.wsgifunc()

if __name__ == '__main__':
    webapp.run()
