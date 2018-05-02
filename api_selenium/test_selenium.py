#!/usr/bin/env python
# -*- coding: utf-8 -*-
from selenium import webdriver
import unittest


class VisitSogouByFirefox(unittest.TestCase):

    def setUp(self):
        self.driver = webdriver.Firefox()

    def test_implictWait(self):
        # 导入异常类
        from selenium.common.exceptions import NoSuchElementException, TimeoutException
        # 导入堆栈类
        import traceback
        url = "http://www.sogou.com"
        # 访问搜狗首页
        self.driver.get(url)
        # 通过 driver 对象 implicitly_wait() 方法来设置隐式等待时间，最长等待 10 秒
        self.driver.implicitly_wait(10)
        try:
            # 查找 sogou 首页的搜索输入框页面元素
            searchBox = self.driver.find_element_by_id("query")
            # 在搜索输入框中输入 "光荣之路自动化测试"
            searchBox.send_keys(u"光荣之路自动化测试")
            # 查找 sogou 首页搜索按钮页面元素
            click = self.driver.find_element_by_id("stb")
            # 单击搜索按钮
            click.click()
        except (NoSuchElementException, TimeoutException), e:
            traceback.print_exc()

    def tearDown(self):
        self.driver.quit()


if __name__ == '__main__':
    unittest.main()