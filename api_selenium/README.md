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

### 16.获取页面元素的 CSS 属性值
```python
def test_getWebElementCssValue(self):
    url = "http://www.baidu.com"
    # 访问 baidu 首页
    self.driver.get(url)
    # 找到搜索输入框元素
    searchBox = self.driver.find_element_by_id("kw")
    # 使用页面元素对象的 value_of_css_property() 方法获取元素的 CSS 属性值
    print u"搜索输入框的高度是：", searchBox.value_of_css_property("height")
    print u"搜索输入框的宽度是：", searchBox.value_of_css_property("width")
    font = searchBox.value_of_css_property("font-family")
    print u"搜索输入框的字体是：", font
    # 断言搜索输入框的字体是否是 arial 字体
    self.assertEqual(font, "arial")
```

### 17.清空输入框中的内容
### 18.在输入框中输入指定内容
```python
def test_clearInputBoxText(self):
    url = "http://www.baidu.com"
    # 访问 baidu 首页
    self.driver.get(url)
    # 获取输入框页面对象
    input = self.driver.find_element_by_id("kw")
    input.send_keys(u"光荣之路自动化测试")
    import time
    time.sleep(3)
    # 清除输入框中默认内容
    input.clear()
    # 等待 3 秒，主要看清空输入框内容后的效果
    time.sleep(3)
```

### 19.单击按钮
```python
def test_clickButton(self):
    url = "http://www.baidu.com"
    # 访问 baidu 首页
    self.driver.get(url)
    # 获取按钮页面对象
    button = self.driver.find_element_by_id("button")
    # 模拟鼠标左键单击操作
    button.click()
    import time
    time.sleep(3)
```

### 20.双击某个元素
```python
def test_doubleClick(self):
    url = "d:\\test.html"
    # 访问自定义的 HTML 网页
    self.driver.get(url)
    # 获取页面输入元素
    inputBox = self.driver.find_element_by_id("inputBox")
    # 导入支持双击操作的模块
    from selenium.webdriver import ActionChains
    # 开始模拟鼠标双击操作
    action_chains = ActionChains(self.driver)
    action_chains.double_click(inputBox).perform()
    import time
    time.sleep(3)

    """
    selenium.webdriver.ActionChains 包是 WebDriver 针对 Python 语言提供的专门用于
    模拟鼠标操作事件的包，比如双击、悬浮、拖拽等。
    """
```

### 21.遍历所有选项并打印选项显示的文本和选项值
```python
select.html

<html>
<body>
    <select name='fruit' size=1>
        <option id='peach' value='taozi'>桃子</option>
        <option id='watermelon' value='xigua'>西瓜</option>
        <option id='orange' value='juzi'>橘子</option>
        <option id='kiwifruit' value='mihoutao'>猕猴桃</option>
        <option id='maybush' value='shanzha'>山楂</option>
        <option id='litchi' value='lizhi'>荔枝</option>
    </select>
</body>
</html>


def test_printSelectText(self):
    url = "d:\\select.html"
    # 访问自定义的 HTML 网页
    self.driver.get(url)
    # 使用 name 属性找到页面上 name 属性为“fruit”的下拉列表元素
    select = self.driver.find_element_by_name("fruit")
    all_options = select.find_elements_by_tag_name("option")
    for option in all_options:
        print "选项显示的文本：", option.text
        print "选项值：", option.get_attribute("value")
        option.click()
        import time
        time.sleep(3)
```

### 21.2 选项下拉列表元素的三种方法
```python
def test_operateDropList(self):
    url = "d:\\select.html"
    # 访问自定义的 HTML 网页
    self.driver.get(url)
    # 导入 Select 模块
    from selenium.webdriver.support.ui import Select
    # 使用 xpath 定位方式获取 select 页面元素对象
    select_emement = Select(self.driver.find_element_by_xpath("//select"))
    # 打印默认选中项的文本
    print select_emement.first_selected_option.text
    # 获取所有选择项的页面元素对象
    all_options = select_emement.options
    # 打印选项总个数
    print len(all_options)
    '''
    is_enabled():判断元素是否可操作
    is_selected():判断元素是否被选中
    '''
    if all_options[1].is_enabled() and not all_options[1].is_selected():
        # 方法一：通过序号选择第二个元素，序号从 0 开始
        select_emement.select_by_index(1)
        # 打印已选中项的文本
        print select_emement.all_selected_options[0].text
        # assertEqual()方法断言当前选中的选项文本是否是“西瓜”
        self.assertEqual(select_emement.all_selected_options[0].text, u'西瓜')
    import time
    time.sleep(2)

    # 方法二：通过选项的显示文本选择文本为“猕猴桃”选项
    select_emement.select_by_visible_text("猕猴桃")
    # 断言已选中项的文本是否是“猕猴桃”
    self.assertEqual(select_emement.all_selected_options[0].text, u'猕猴桃')
    time.sleep(2)

    # 方法三：通过选项的 value 属性值选择 value="shanzha" 选项
    select_emement.select_by_value("shanzha")
    print select_emement.all_selected_options[0].text
    self.assertEqual(select_emement.all_selected_options[0].text, u'山楂')
```

### 22.断言单选列表选项值
```python
def test_checkSelectText(self):
    url = "d:\\select.html"   # 同 21 select.html
    # 访问自定义的 HTML 网页
    self.driver.get(url)
    # 导入 Select 模块
    from selenium.webdriver.support.ui import Select
    # 使用 xpath 定位方式获取 select 页面元素对象
    select_emement = Select(self.driver.find_element_by_xpath("//select"))
    # 获取所有选择项的页面元素对象
    actual_options = select_emement.options
    # 声明一个 list 对象，存储下拉列表中所期望出现的文字内容
    expect_optionsList = [u'桃子', u'西瓜', u'橘子', u'猕猴桃', u'山楂', u'荔枝']
    # 使用 Python 内置 map() 函数获取页面中下拉列表展示的选项内容组成的列表对象
    actual_optionsList = map(lambda option: option.text, actual_options)
    # 断言期望列表对象和实际列表对象是否完全一致
    self.assertListEqual(expect_optionsList, actual_optionsList)
```

### 23.操作多选的选择列表
```python
select.html

<html>
<body>
    <select name='fruit' size=6 multiple=true>
        <option id='peach' value='taozi'>桃子</option>
        <option id='watermelon' value='xigua'>西瓜</option>
        <option id='orange' value='juzi'>橘子</option>
        <option id='kiwifruit' value='mihoutao'>猕猴桃</option>
        <option id='maybush' value='shanzha'>山楂</option>
        <option id='litchi' value='lizhi'>荔枝</option>
    </select>
</body>
</html>


def test_operateMultipleOptionDropList(self):
    url = "d:\\select.html"   # 同 21 select.html
    # 访问自定义的 HTML 网页
    self.driver.get(url)
    # 导入 Select 模块
    from selenium.webdriver.support.ui import Select
    import time
    # 使用 xpath 定位方式获取 select 页面元素对象
    select_emement = Select(self.driver.find_element_by_xpath("//select"))
    # 通过序号选择第一个元素
    select_emement.select_by_index(0)
    # 通过选项的文本选择“山楂”选项
    select_emement.select_by_visible_text("山楂")
    # 通过选项的 value 属性值选择 value='mihoutao' 的选项
    select_emement.select_by_value("mihoutao")
    # 打印所有的选中项文本
    for option in select_emement.all_selected_options:
        print option.text
    # 取消所有已选中项
    select_emement.deselect_all()
    time.sleep(2)
    print '-----------再次选中 3 个选项-----------'
    select_emement.select_by_index(1)
    select_emement.select_by_visible_text("荔枝")
    select_emement.select_by_value("juzi")
    # 通过选项文本取消已选中的文本为“荔枝”选项
    select_emement.deselect_by_visible_text("荔枝")
    # 通过序号取消已选中的序号为 1 的选项
    select_emement.deselect_by_index(1)
    # 通过选项的 value 属性值取消已选中的 value="juzi" 选项
    select_emement.deselect_by_value("juzi")
```

### 24.操作可以输入的下拉列表(输入的同时模拟按键)
```python
data.html

<html>
<body>
    <div style="position:relative;">
        <input list="pasta" id="select">
        <datalist id="pasta">
            <option>Bavette</option>
            <option>Rigatoni</option>
            <option>Fiorentine</option>
            <option>Gnocchi</option>
            <option>Tagliatelle</option>
            <option>Penne lisce</option>
            <option>Pici</option>
            <option>Pappardelle</option>
            <option>Spaghetti</option>
            <option>Cannelloni</option>
            <option>Cancl</option>
        </datalist>
    </div>
</body>
</html>

def test_operateMultipleOptionDropList(self):
    url = r"D:\data.html"
    # 访问自定义的 HTML 网页
    self.driver.get(url)
    from selenium.webdriver.common.keys import Keys
    self.driver.find_element_by_id("select").clear()
    import time
    time.sleep(1)
    # 按下的同时按下箭头键
    self.driver.find_element_by_id("select").send_keys("c", Keys.ARROW_DOWN)
    self.driver.find_element_by_id("select").send_keys(Keys.ARROW_DOWN)
    self.driver.find_element_by_id("select").send_keys(Keys.ENTER)
    time.sleep(3)
    """
    运行这段测试代码可以看到输入字符“c”的同时看到筛选出的数据项中第一项被选中。
    """
```

### 25.操作单选框
```python
radio.html

<html>
<body>
    <form>
        <input type="radio" name="fruit" value="berry">草莓</input>
        <br />
        <input type="radio" name="fruit" value="watermelon">西瓜</input>
        <br />
        <input type="radio" name="fruit" value="orange">橘子</input>
    </form>
</body>
</html>

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
```