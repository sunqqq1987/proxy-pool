#!/usr/bin/python3
# -*- coding: UTF-8 -*-

import ipaddress
# To use ipaddress module, the version of Python must be greater than 3.3
import requests
from fake_useragent import UserAgent
headers_base = {'User-Agent': UserAgent().random}


def ip_isvalid(address):
    try: 
        ipaddress.IPv4Address(address)
        return True
    except ipaddress.AddressValueError:
        return False


def port_isvalid(port):
    try:    
        if( int(port) < 65535 and int(port) > 1):
            return True
        else:
            return False
    except ValueError:
        return False


def protocol_isvalid(protocol=""):
    try:
        if(protocol.upper()=="HTTP" or protocol.upper()=="HTTPS"):
            return True
        else:
            return False
    except AttributeError as e:
        print("Parameter must be string. "+str(e))
        return False


def getLocation(address):
    try:
        if(ip_isvalid(address)):
            par = {'ip': address}
            response = requests.get('http://ip.taobao.com/service/getIpInfo.php', params=par)
            re_json = response.json()
            region = re_json['data']['country']
            if(region=='中国'):
                return re_json['data']['region']
            return region
        else:
            return ''
    except Exception as e:
        print(str(e))
        return ''


def ipverify(address, port, protocol='HTTP'):
    proxy = {'http': protocol + "://"+str(address)+":"+str(port)}
    try:
        response = requests.get('http://ip.taobao.com/service/getIpInfo.php?ip=myip',
                                headers=headers_base, proxies=proxy, timeout=3)
        # print(response.json()['data']['ip'])
        # print(address)
        # print(address, port, response.text)
        # print(response.elapsed.microseconds/1000)
        if response.json()['data']['ip'] == address:
            # print(response)
            speed = response.elapsed.microseconds/1000
            return [True, speed]
        return [False, False]
    except:
        return [False, False]


# Used for test!
# address = "119.28.194.66"
# port = 8888
# print(ipverify(address, port)[1])
# print()



