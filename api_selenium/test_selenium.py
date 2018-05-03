#!/usr/bin/env python
# -*- coding: utf-8 -*-
from selenium import webdriver
import unittest


class VisitSogouByFirefox(unittest.TestCase):

    def setUp(self):
        self.driver = webdriver.Firefox()

    def test_visitURL(self):
        visitURL = "http://www.sougou.com"
        # 通过 driver 对象的 get 方法，访问指定的网址
        self.driver.get(visitURL)
        assert self.driver.title.find(u'搜狗搜索引擎') >= 0, "assert error"

    def tearDown(self):
        self.driver.quit()


if __name__ == '__main__':
    unittest.main()