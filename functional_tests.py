#!usr/loacl/bin/python 3
# -*- coding: utf-8 -*-
from selenium import webdriver
browser=webdriver.Firefox()
browser.get('http://127.0.0.1/')
assert 'Django' in browser.title #还没有创建本地的web

#测试如何使用github桌面程序，提交代码
