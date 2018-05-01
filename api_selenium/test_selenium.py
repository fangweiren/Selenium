#!/usr/bin/env python
# -*- coding: utf-8 -*-
from selenium import webdriver
import unittest


class VisitSogouByFirefox(unittest.TestCase):

    def setUp(self):
        self.driver = webdriver.Firefox()

    def test_operateMultipleOptionDropList(self):
        url = r"D:\radio.html"
        # 访问自定义的 HTML 网页
        self.driver.get(url)
        # 使用 xpath 定位获取 value 属性值为'berry'的 input 元素对象，也就是"草莓"选项
        berryRadio = self.driver.find_element_by_xpath("//input[@value='berry']")
        # 单击选择"草莓"选项
        berryRadio.click()
        # 断言"草莓"单选框被成功选中
        self.assertTrue(berryRadio.is_selected(), u"草莓单选框未被选中！")
        if berryRadio.is_selected():
            # 如果"草莓"单选框被成功选中，重新选择"西瓜"选项
            watermelonRadio = self.driver.find_element_by_xpath("//input[@value='watermelon']")
            watermelonRadio.click()
            # 选择"西瓜"选项以后，断言"草莓"选项处于未被选中状态
            self.assertFalse(berryRadio.is_selected())
        # 查找所有 name 属性值为'fruit'的单选框元素对象，并存放在 radioList 列表中
        radioList = self.driver.find_element_by_xpath("//input[@name='fruit']")
        '''
        循环遍历 radioList 中的每个单选按钮，查找 value 属性值为"orange"的单选框，
        如果找到此单选框以后，发现未处于选中状态，则调用 click 方法选中该选项。
        '''
        for radio in radioList:
            if radio.get_attribute("value") == "orange":
                if not radio.is_selected():
                    radio.click()
                    self.assertEqual(radio.get_attribute("value"), "orange")

    def tearDown(self):
        self.driver.quit()


if __name__ == '__main__':
    unittest.main()