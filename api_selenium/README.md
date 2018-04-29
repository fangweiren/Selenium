### 1.访问某个网址
```python
def test_visitURL(self):
    visitURL = "http://www.sougou.com"
    # 通过 driver 对象的 get 方法，访问指定的网址
    self.driver.get(visitURL)
    assert self.driver.title.find(u'搜狗搜索引擎') >= 0, "assert error"
```

### 2.网页的前进和后退
```python
def test_visitRecentURL(self):
    firstVisitURL = "http://www.sougou.com"
    secondVisitURL = "http://www.baidu.com"
    # 首先访问 sougou 首页
    self.driver.get(firstVisitURL)
    # 然后访问 baidu 首页
    self.driver.get(secondVisitURL)
    # 返回上一次访问过的搜狗首页
    self.driver.back()
    # 再次回到百度首页
    self.driver.forward()
```

### 3.刷新当前页面
```python
def test_refreshCurrentPage(self):
    url = "http://www.iamnancy.top"
    self.driver.get(url)
    time.sleep(5)
    # 刷新当前页面
    self.driver.refresh()
```

### 4.浏览器窗口最大化
```python
def test_maximizeWindow(self):
    url = "http://www.iamnancy.top"
    self.driver.get(url)
    # 最大化浏览器窗口，以便占满整个电脑屏幕
    self.driver.maximize_window()
```

### 5.获取并设置当前窗口的位置
```python
def test_window_position(self):
    url = "http://www.iamnancy.top"
    self.driver.get(url)
    # 获取当前浏览器在屏幕上的位置，返回的是字典对象
    position = self.driver.get_window_position()
    print "当前浏览器所在位置的横坐标：", position['x']
    print "当前浏览器所在位置的纵坐标：", position['y']
    # 设置当前浏览器在屏幕上的位置
    self.driver.set_window_position(y=200, x=400)
    # 设置浏览器的位置后，再次获取浏览器的位置信息
    print self.driver.get_window_position()

    """
    1.获取的浏览器位置是指浏览器左上角所在的屏幕上的位置，返回的是 x,y 坐标值，即横纵坐标。
    2.get_window_position() 和 set_window_position() 方法在部分浏览器的部分版本上失效。
    """
```

### 6.获取并设置当前窗口的大小
```python
def test_window_size(self):
    url = "http://www.iamnancy.top"
    self.driver.get(url)
    # 获取浏览器窗口的大小，返回字典类型
    sizeDict = self.driver.get_window_size()
    print "当前浏览器窗口的宽：", sizeDict['width']
    print "当前浏览器窗口的高：", sizeDict['height']
    # 设置浏览器窗口的大小
    self.driver.set_window_size(width=500, height=400, windowHandle='current')
    # 设置浏览器窗口大小以后，再次获取浏览器窗口大小信息
    print self.driver.get_window_size(windowHandle='current')
```

### 7.获取页面的 Title 属性值
```python
def test_getTitle(self):
    url = "http://www.baidu.com"
    self.driver.get(url)
    # 调用 driver 的 title 属性获取页面的 title 属性值
    title = self.driver.title
    print "当前网页的 title 属性值为：", title
    # 断言页面的 title 属性值是否是“百度一下，你就知道”
    self.assertEqual(title, u"百度一下，你就知道", "页面 title 属性值错误")
```

### 8.获取页面的 HTML 源代码
```python
def test_getPageSource(self):
    url = "http://www.iamnancy.top"
    self.driver.get(url)
    # 调用 driver 的 page_source 属性获取页面源码
    pageSource = self.driver.page_source
    # 打印页面源码
    print pageSource
    # 断言页面源码中是否包含“新闻”两个关键字，以此判断页面内容是否正确
    self.assertTrue(u"订阅" in pageSource, "页面源码中未找到'订阅'关键字")
```

### 9.获取当前页面的 URL 地址
```python
def test_getCurrentPageUrl(self):
    url = "http://www.iamnancy.top"
    self.driver.get(url)
    # 获取当前页面的 URL
    currentPageUrl = self.driver.current_url
    # 打印当前 URL
    print currentPageUrl
    # 断言当前网页的网址是否为 http://www.iamnancy.top/
    self.assertEqual(currentPageUrl, "http://www.iamnancy.top/", "当前网页网址非预期")
```

### 10.获取与切换浏览器窗口句柄
```python
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

    """
    driver.window_handles 以列表对象形式返回所有打开窗口的句柄，包括主窗口，
    可以通过 driver.window_handles[-1] 来获取当前打开窗口的句柄。
    """
```

### 11.获取页面元素的基本信息
```python
def test_getBasicInfo(self):
    url = "http://www.baidu.com"
    # 访问百度首页
    self.driver.get(url)
    # 查找百度首页上的“新闻”链接元素
    newsElement = self.driver.find_element_by_xpath("//a[text()='新闻']")
    # 获取查找到的“新闻”链接元素的基本信息
    print u'元素的标签名：', newsElement.tag_name
    print u'元素的 size：', newsElement.size
```

### 12.获取页面元素的文本内容
```python
def test_getWebElementText(self):
    url = "http://www.baidu.com"
    # 访问百度首页
    self.driver.get(url)
    import time
    time.sleep(5)
    # 通过 xpath 定位方式找到 id 属性值为 “ul” 的 div 元素下的第一个链接元素
    aElement = self.driver.find_element_by_xpath("//*[@class='mnav'][1]")
    a_text = aElement.text
    print a_text
    self.assertEqual(a_text, u'糯米')
```

### 13.判断页面元素是否可见
```python
def test_getWebElementIsDisplayed(self):
    url = "d:\\test.html"
    # 访问自定义的 HTML 网页
    self.driver.get(url)
    # 通过 id="div2" 找到第二个 div 元素
    div2 = self.driver.find_element_by_id("div2")
    # 判断第二个 div 元素是否在页面上可见
    print div2.is_displayed()
    # 单击第一个切换 div 按钮，将第二个 div 显示在页面上
    self.driver.find_element_by_id("button1").click()
    # 再次判断第二个 div 元素是否可见
    print div2.is_displayed()
    # 通过 id="div4" 找到第四个 div 元素
    div4 = self.driver.find_element_by_id("div4")
    # 判断第四个 div 元素是否在页面上可见
    print div4.is_displayed()
    # 单击第二个切换 div 按钮，将第四个 div 显示在页面上
    self.driver.find_element_by_id("button2").click()
    # 再次判断第四个 div 元素是否可见
    print div4.is_displayed()
```

### 14.判断页面元素是否可操作
```python
def test_getWebElementEnabled(self):
    url = "d:\\test.html"
    # 访问自定义的 HTML 网页
    self.driver.get(url)
    # 通过 id 找到第一个 input 元素
    input1 = self.driver.find_element_by_id("input1")
    # 判断第一个 input 元素是否可操作
    print input1.is_enabled()
    # 通过 id 找到第二个 input 元素
    input2 = self.driver.find_element_by_id("input2")
    # 判断第二个 input 元素是否可操作
    print input2.is_enabled()
    # 通过 id 找到第三个 input 元素
    input3 = self.driver.find_element_by_id("input3")
    # 判断第三个 input 元素是否可操作
    print input3.is_enabled()
```

### 15.获取页面元素的属性
```python
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
```