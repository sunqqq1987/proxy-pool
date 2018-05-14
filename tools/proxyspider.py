#!/usr/bin/python3
# -*- coding: UTF-8 -*-

import time
import requests
import logging
from bs4 import BeautifulSoup

from tools import iptools as iptools, dboperation, setting
from fake_useragent import UserAgent

headers_base = {'User-Agent': UserAgent().random}
proxy_web_page_num = setting.proxy_web_loop_number
logging.basicConfig(filename='spider.log', level=logging.INFO, format='%(levelname)s:%(asctime)s %(message)s')


def getProxy(website, page_num=proxy_web_page_num):
    try:
        for n in range(1, page_num):
            ip_website = website+str(n)
            print("Scanning website: "+ip_website)
            response = requests.get(ip_website, headers=headers_base)
            soup = BeautifulSoup(response.text, 'lxml')
            result = soup.find_all('td')
            for i, e in enumerate(result, 0):
                temp = e.text
                # print(temp)
                if iptools.ip_isvalid(temp):
                    address = temp
                elif iptools.port_isvalid(temp):
                    port = temp
                    # print(port)
                elif iptools.protocol_isvalid(temp):
                    protocol = temp
                    # proxy_ip = protocol.lower() + '://' + address + ':' + port
                    dboperation.insert(address=address, port=port, location="", protocol=protocol)
            time.sleep(3)
    except Exception as e:
        print(e)
        logging.warning(e)
        pass


def getcnProxy(times=1):  # 刷新次数
    try:
        for n in range(times):
            ip_website = 'http://cn-proxy.com/'  # 此网站需要翻墙才能用
            # TODO 代理需要修改
            proxy = {'http': "http://127.0.0.1:25378"}  # 使用本机SS代理，如果切换环境需要修改
            print("Scanning website: "+ip_website)
            response = requests.get(ip_website, headers=headers_base, proxies=proxy)
            soup = BeautifulSoup(response.text, 'lxml')
            result = soup.find_all('td')
            for i, e in enumerate(result, 0):
                temp = e.text
                if iptools.ip_isvalid(temp):
                    address = temp
                elif iptools.port_isvalid(temp):
                    port = temp
                    dboperation.insert(address=address, port=port, location="", protocol='HTTP')
            time.sleep(3)
        for n in range(times):
            ip_website = 'http://cn-proxy.com/archives/218'  # 此网站需要翻墙才能用
            # TODO 代理需要修改
            proxy = {'http': "http://127.0.0.1:25378"}  # 使用本机SS代理，如果切换环境需要修改
            print("Scanning website: "+ip_website)
            response = requests.get(ip_website, headers=headers_base, proxies=proxy)
            soup = BeautifulSoup(response.text, 'lxml')
            result = soup.find_all('td')
            for i, e in enumerate(result, 0):
                temp = e.text
                # print(temp)
                if iptools.ip_isvalid(temp):
                    address = temp
                elif iptools.port_isvalid(temp):
                    port = temp
                    dboperation.insert(address=address, port=port, location="", protocol='HTTP')
            time.sleep(3)
    except:
        pass


# Used for test!
# getProxy('http://www.xicidaili.com/n2/')