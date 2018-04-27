#!/usr/bin/env python
# -*- coding: utf-8 -*-
from selenium import webdriver
# import time

driver = webdriver.Firefox()


def test_window_position():
    url = "http://www.iamnancy.top"
    driver.get(url)
    # 获取当前浏览器在屏幕上的位置，返回的是字典对象
    position = driver.get_window_position()
    print "当前浏览器所在位置的横坐标：", position['x']
    print "当前浏览器所在位置的纵坐标：", position['y']
    # 设置当前浏览器在屏幕上的位置
    driver.set_window_position(y=500, x=800)
    # 设置浏览器的位置后，再次获取浏览器的位置信息
    print driver.get_window_position()


test_window_position()