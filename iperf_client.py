#!/usr/bin/env python
#_*_ coding:utf-8 _*_
'''
@author: tanglei
@contact: tanglei_0315@163.com
@file: iperf_client.py
@time: 2018/4/5 18:39
'''
import iperf3

client = iperf3.Client()
client.duration = 1
client.bind_address = '192.168.137.2'
client.server_hostname = '192.168.137.2'