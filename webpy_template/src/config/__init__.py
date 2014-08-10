#!/usr/bin/env python
# coding: utf-8
import os

mode = "dev"   #开发环境
#mode = "test"  #测试环境
#mode = "prod"  #生产环境

if mode == "dev":
    from .dev import *
elif mode == "test":
    from .test import *
elif mode == "prod":
    from .prod import *
else:
    raise "load configuration files fail, unknown mode (%s) " % (mode)
