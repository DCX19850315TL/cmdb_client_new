#!/usr/bin/env python
#_*_ coding:utf-8 _*_
'''
@author: tanglei
@contact: tanglei_0315@163.com
@file: iperf_server.py
@time: 2018/4/5 18:39
'''
import iperf3

server = iperf3.Server()
server.bind_address = '192.168.1.11'
server.port = 6969
server.verbose = False
while True:
    server.run()
