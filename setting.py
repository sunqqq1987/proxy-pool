#!/usr/bin/python
# -*- coding: UTF-8 -*-
from fake_useragent import UserAgent
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

thread_number = 10

db = 'proxylist.db'
