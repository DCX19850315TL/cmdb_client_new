#!/usr/bin/env python
#_*_ coding:utf-8 _*_
'''
@author: tanglei
@contact: tanglei_0315@163.com
@file: BasePlugin.py
@time: 2018/4/3 18:01
'''
import os
import commands
import salt.client
#通过salt获取服务器列表
def server_list(cmd):
    list = commands.getoutput(cmd)
    print type(list)

#b = a.update('salt-key -L --output=json')
#server_list('salt-key -L --output=json')

server_list('salt-key -L --output=json')

'''
a = {'a':1,'b':2}
print a['a']
print type(a)
'''

