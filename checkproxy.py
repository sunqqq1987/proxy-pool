#!/usr/bin/python3
# -*- coding: UTF-8 -*-
# 修改自https://github.com/SymeonChen/spider-proxy-pool
# 增加数据库检测成功\失败次数统计,网页api返回成功率比较高的代理
# 减少了代理爬取网站,发现有些网站规则变了,中间报错,逐渐增加

from multiprocessing.dummy import Pool as ThreadPool
from tools import dboperation, setting

thread_number = setting.thread_number  # 线程数量
proxy_list = setting.proxy_web_list  # 网站列表

pool = ThreadPool(thread_number)

results = dboperation.selectAllAddress()
pool.map(dboperation.checkAllAddress, results)

pool.close()
pool.join()















































