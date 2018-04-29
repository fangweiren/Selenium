#!/usr/bin/env python
# -*- coding: utf-8 -*-
from selenium import webdriver
import unittest


class VisitSogouByFirefox(unittest.TestCase):

    def setUp(self):
        self.driver = webdriver.Firefox()

    def test_getWebElementAttribute(self):
        url = "http://www.sogou.com"
        # 访问 sogou 首页
        self.driver.get(url)
        # 找到搜索输入框元素
        searchBox = self.driver.find_element_by_id("query")
        # 获取搜索输入框页面元素的 name 属性值
        print searchBox.get_attribute("name")
        # 向搜索输入框中输入“测试工程师指定的输入内容”内容
        searchBox.send_keys(u"测试工程师指定的输入内容")
        # 获取页面搜索框的 value 属性值(即搜索输入框的文字内容)
        print searchBox.get_attribute("value")

    def tearDown(self):
        self.driver.quit()


if __name__ == '__main__':
    unittest.main()