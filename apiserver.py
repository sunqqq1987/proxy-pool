#!/usr/bin/python
# -*- coding: UTF-8 -*-

import dboperation
import logging
import random
from flask import Flask, jsonify
logging.basicConfig(filename='api_server.log', level=logging.INFO, format='%(levelname)s:%(asctime)s %(message)s')
app = Flask(__name__)


# 获取所有IP
@app.route('/api/all', methods=['GET'])
def get_all():
    tasks = dboperation.select()
    return jsonify({'tasks': tasks})


# 获取权重比较高，延时比较低的IP
@app.route('/api/best', methods=['GET'])
def get_best():
    tasks = dboperation.select_best()
    return jsonify({'tasks': tasks})


# 随机获取一个权重比较高，延时比较低的IP
@app.route('/api/random', methods=['GET'])
def get_random():
    tasks = dboperation.select_best()
    return jsonify({'ip': random.choice(tasks)})
    # 获取到随机IP格式:{"ip":["4f36a4c0-990f-5a2f-8bf7-e811df1ea93c","120.26.110.59",8080,"北京","HTTP",14,147.535]}


def run():
    print("Get all ip from http://localhost:5000/api/all")
    print("Get best ip from http://localhost:5000/api/best")
    print("Get random best ip from http://localhost:5000/api/random")
    app.run()


if __name__ == '__main__':
    run()
