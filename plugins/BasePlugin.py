#!/usr/bin/env python
#_*_ coding:utf-8 _*_
'''
@author: tanglei
@contact: tanglei_0315@163.com
@file: BasePlugin.py
@time: 2018/4/3 18:01
'''
import salt.client
import json
import os

def server_list():
    local = salt.client.LocalClient()
    server_keys = local.key

    return server_keys