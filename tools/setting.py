#!/usr/bin/python3
# -*- coding: UTF-8 -*-
from fake_useragent import UserAgent
import os
# set headers,use random
headers_base = {'User-Agent': UserAgent().random}
proxy_web_list = {
    "http://www.kuaidaili.com/free/inha/",
    "http://www.kuaidaili.com/free/intr/",
    "http://www.xicidaili.com/nn/",
    "http://www.xicidaili.com/wt/",
    "http://www.xicidaili.com/nt/",
    "http://www.ip3366.net/free/?stype=1&page=",
    "http://www.ip3366.net/free/?stype=2&page=",
    "http://www.ip3366.net/free/?stype=3&page=",
    "http://www.ip3366.net/free/?stype=4&page="
    "http://www.mimiip.com/gngao/",
    "http://www.mimiip.com/hw/",
    "http://www.mimiip.com/gnpu/",
    "http://www.mimiip.com/gntou/"

}

header_pc = {'User-Agent': UserAgent().random}

proxy_web_loop_number = 2

thread_number = 20

db = os.path.dirname(__file__)+os.sep+'proxylist.db'
# 数据库文件使用上面方式获取路径,使用os.getcwd()在Ubuntu上面获取的为用户主目录，获取不到脚本目录，具体原因搞不清楚
# print(db)

