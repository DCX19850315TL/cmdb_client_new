#!/usr/bin/env python
#_*_ coding:utf-8 _*_
'''
@author: tanglei
@contact: tanglei_0315@163.com
@file: BasePlugin.py
@time: 2018/4/3 18:01
'''
import os
import salt.client
#通过salt获取服务器列表

def server():
    local = salt.client.LocalClient()
    cmd = local.cmd('*','cmd.run',['whoami'])
    return cmd

server()


