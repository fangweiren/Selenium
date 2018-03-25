#!/usr/bin/env python
# -*- coding: utf-8 -*-

from selenium import webdriver

import time

url = 'https://www.douban.com/'

firefox_profile = webdriver.FirefoxProfile()
# 不下载和加载图片
firefox_profile.set_preference('permissions.default.image', 2)
driver = webdriver.Firefox(firefox_profile=firefox_profile)
driver.get(url)
time.sleep(3)
driver.find_element_by_xpath('//*[@id="form_email"]').send_keys('username') # 填入相应的账号
time.sleep(1)
driver.find_element_by_xpath('//*[@id="form_password"]').send_keys('password') # 填入相应的密码
time.sleep(1)
driver.find_element_by_xpath('//*[@id="lzform"]/fieldset/div[4]/label').click() # 勾选 记住我
time.sleep(1)
driver.find_element_by_xpath('//*[@id="lzform"]/fieldset/div[3]/input').click() # 点击 登录豆瓣

time.sleep(20)
driver.quit()
 