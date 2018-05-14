#!/usr/bin/python3
# -*- coding: UTF-8 -*-
# 修改自https://github.com/SymeonChen/spider-proxy-pool
# 增加数据库检测成功\失败次数统计,网页api返回成功率比较高的代理
# 减少了代理爬取网站,发现有些网站规则变了,中间报错,逐渐增加

from multiprocessing.dummy import Pool as ThreadPool
# import dboperation
from tools import setting, proxyspider

# import apiserver

thread_number = setting.thread_number  # 线程数量
proxy_list = setting.proxy_web_list  # 网站列表

# for i in range(1):  # 循环筛选ip
# 爬取新的代理增加到数据库
pool = ThreadPool(thread_number)
pool.map(proxyspider.getProxy, proxy_list)  # 爬代理列表内网站
proxyspider.getcnProxy()  # 爬cn-proxy
# 验证ip可用性,使用淘宝地址检测
# results = dboperation.selectAllAddress()
# pool.map(dboperation.checkAllAddress, results)

pool.close()
pool.join()
# 运行网页api
# apiserver.run()














































