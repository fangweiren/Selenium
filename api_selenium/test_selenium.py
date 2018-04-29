#!/usr/bin/env python
# -*- coding: utf-8 -*-
from selenium import webdriver
import unittest


class VisitSogouByFirefox(unittest.TestCase):

    def setUp(self):
        self.driver = webdriver.Firefox()

    def test_operateWindowHandle(self):
        url = "http://www.baidu.com"
        self.driver.get(url)
        # 获取当前窗口句柄
        now_handle = self.driver.current_window_handle
        # 打印当前获取的窗口句柄
        print now_handle
        # 百度搜索输入框中输入“selenium”
        self.driver.find_element_by_id("kw").send_keys("w3school")
        # 单击搜索按钮
        self.driver.find_element_by_id("su").click()
        # 导入 time 包
        import time
        time.sleep(3)
        # 单击 w3school 在线教育链接
        self.driver.find_element_by_xpath('//*[@id="1"]/h3/a').click()
        time.sleep(5)
        # 获取所有窗口句柄
        all_handles = self.driver.window_handles
        print "++++", self.driver.window_handles[-1]
        # 循环遍历所有新打开的窗口句柄，也就是说不包括主窗口
        for handle in all_handles:
            if handle != now_handle:
                # 输出待选择的窗口句柄
                # print handle
                pass

    def tearDown(self):
        self.driver.quit()


if __name__ == '__main__':
    unittest.main()