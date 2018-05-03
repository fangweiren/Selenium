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

### 26.操作复选框
```python
CheckBox.html

<html>
<body>
    <form>
        <input type="checkbox" name="fruit" value="berry">草莓</input>
        <br />
        <input type="checkbox" name="fruit" value="berry">草莓</input>
        <br />
        <input type="checkbox" name="fruit" value="berry">草莓</input>
    </form>
</body>
</html>


def test_operateCheckBox(self):
    url = "d:\\CheckBox.html"
    # 访问自定义的 HTML 网页
    self.driver.get(url)
    # 使用 xpath 定位获取 value 属性值为 'berry' 的 input 元素对象，也就是“草莓”选项
    berryCheckBox = self.driver.find_element_by_xpath("//input[@value='berry']")
    # 单击选择“草莓”选项
    berryCheckBox.click()
    # 断言“草莓”复选框被成功选中
    self.assertTrue(berryCheckBox.is_selected(), u'草莓复选框未被选中！')
    if berryCheckBox.is_selected():
        # 如果“草莓”复选框被成功选中，再次单击取消选中
        berryCheckBox.click()
        # 断言“草莓”复选框处于未选中状态
        self.assertFalse(berryCheckBox.is_selected())
    # 查找所有 name 属性值为 ‘fruit’ 的复选框元素对象，并存放在 checkBoxList 列表中
    checkBoxList = self.driver.find_element_by_xpath("//input[@name='fruit']")
    # 遍历 checkBoxList 列表中的所有复选框元素，让全部复选框处于被选中状态
    for box in checkBoxList:
        if not box.is_selected():
            box.click()
```

### 27.断言页面源码中的关键字
```python
def test_assertKeyWord(self):
    url = "http://www.baidu.com"
    # 访问百度首页
    self.driver.get(url)
    self.driver.find_element_by_id("kw").send_keys(u"光荣之路自动化测试")
    self.driver.find_element_by_id("su").click()
    import time
    time.sleep(4)
    # 通过断言页面是否存在某些关键字来确定页面按照预期加载
    assert u"首页 -- 光荣之路" in self.driver.page_source, u"页面源码中不存在该关键字!"

    """
    有时会出现页面存在要断言的内容，但结果仍断言失败，这可能是由于页面还未加载完全就开始
    执行断言语句，导致要断言的内容在页面源码中找不到。
    """
```

### 28.对当前浏览器窗口截屏
```python
def test_captureScreenInCurrentWindow(self):
    url = "http://www.sogou.com"
    # 访问搜狗首页
    self.driver.get(url)
    try:
        '''
        调用 get_screenhot_as_file(filename) 方法，对浏览器当前打开页面进行截图，并
        保存为 C 盘下的 screenPicture.png 文件
        '''
        result = self.driver.get_screenhot_as_file(r"c:\screenPicture.png")
        print result
    except IOError, e:
        print e

    """
    1.调用截屏函数 get_screenhot_as_file() 截图成功后会返回 True，如果发生了 IOError 异常，
    会返回 False。函数中传递的存放图片的路径可以是绝对路径，也可以是相对路径。
    2.当自动化测试过程中，未实现预期结果，可以将页面截图保存，方便更快速地定位问题。
    """
```

### 29.拖拽页面元素
```python
用于测试的网址：http://jqueryui.com/resources/demos/draggable/scroll.html

def test_dragPageElement(self):
    url = "http://jqueryui.com/resources/demos/draggable/scroll.html"
    # 访问被测网页
    self.driver.get(url)
    # 获取页面上第一个能拖拽的页面元素
    initialPosition = self.driver.find_element_by_id("draggable")
    # 获取页面上第二个能拖拽的页面元素
    targetPosition = self.driver.find_element_by_id("draggable2")
    # 获取页面上第三个能拖拽的页面元素
    dragElement = self.driver.find_element_by_id("draggable3")
    # 导入提供拖拽元素方法的模块 ActionChains
    from selenium.webdriver import ActionChains
    import time
    '''
    创建一个新的 ActionChains，将 webdriver 实例对象 driver 作为参数值传入
    然后通过 WebDriver 实例执行用户动作
    '''
    action_chains = ActionChains(self.driver)
    # 将页面上第一个能被拖拽的元素拖拽到第二个元素位置
    action_chains.drag_and_drop(initialPosition, targetPosition).perform()
    # 将页面上第三个能拖拽的元素，向右下拖动 10 个像素，共拖动 5 次
    for i in range(5):
        action_chains.drag_and_drop_by_offset(dragElement, 10, 10).perform()
        time.sleep(2)
```

### 30.模拟键盘单个按键操作
```python
def test_simulateASingleKeys(self):
    url = "http://www.sogou.com"
    # 访问搜狗首页，焦点会自动定位到搜索输入框中
    self.driver.get(url)
    # 导入模拟按键模块 Keys
    from selenium.webdriver.common.keys import Keys
    import time
    # 通过 id 获取搜索输入框的页面元素
    query = self.driver.find_element_by_id("query")
    # 通过 WebDriver 实例发送一个 F12 键
    query.send_keys(Keys.F12)
    time.sleep(3)
    # 再次通过 WebDriver 实例模拟发送一个 F12 键
    query.send_keys(Keys.F12)
    # 在搜索输入框中输入 "selenium"
    query.send_keys("selenium")
    # 通过 WebDriver 实例发送一个回车键
    # 或者使用 query.send_keys(Keys.RETURN)
    query.send_keys(Keys.ENTER)
    time.sleep(3)
```

### 31.模拟组合按键操作
略。

### 32.模拟鼠标右键
```python
目的：模拟右键菜单实现粘贴效果。

# 导入模拟组合按键需要的包(需要安装)
from selenium.webdriver import ActionChains
import win32clipboard as w
import win32con
import time

# 设置剪切板内容
def setText(aString):
    w.OpenClipboard()
    w.EmptyClipboard()
    w.SetClipboardData(win32con.CF_UNICODETEXT, aString)
    w.CloseClipboard()

# 将上面这段代码放到单元测试类外边的区域，测试用例方法如下：

def test_rightClickMouse(self):
    url = "http://www.sogou.com"
    # 访问搜狗首页
    self.driver.get(url)
    # 找到搜索输入框
    searchBox = self.driver.find_element_by_id("query")
    # 将焦点切换到搜索输入框
    searchBox.click()
    time.sleep(2)
    # 在搜索输入框上执行一个鼠标右键单击操作
    ActionChains(self.driver).context_click(searchBox).perform()
    # 将 "gloryroad" 数据设置到剪切板中，相当于执行了复制操作
    setText(u'gloryroad')
    # 发送一个粘贴命令，字符 P 指代粘贴操作
    ActionChains(self.driver).send_keys('P').perform()
    # 单击搜索按钮
    self.driver.find_element_by_id('stb').click()
    time.sleep(2)
```

### 33.模拟鼠标左键按下与释放
略。

### 34.保持鼠标悬停在某个元素上
略。

### 35.判断页面元素是否存在
```python
def isElementPresent(self, by, value):
    # 从 selenium.common.exceptions 模块导入 NoSuchElementException 异常类
    from selenium.common.exceptions import NoSuchElementException
    try:
        element = self.driver.find_element(by=by, value=value)
    except NoSuchElementException, e:
        # 打印异常信息
        print e
        # 发生了 NoSuchElementException 异常，说明页面中未找到该元素，返回 False
        return False
    else:
        # 没有发生异常，表示在页面中找到了该元素，返回 True
        return True

def test_isElementPresent(self):
    url = "http://www.sogou.com"
    # 访问搜狗首页
    self.driver.get(url)
    # 判断页面元素 id 属性值为 "query" 的页面元素是否存在
    res = self.isElementPresent("id", "query")
    if res is True:
        print u"所查找的元素存在于页面上！"
    else:
        print u"页面中未找到所需要的页面元素！"
```

### 36.隐式等待
```python
隐式等待表示在自动化实施过程中，为查找页面元素或者执行命令设置一个最长等待时间，如果在规定时间内页面元素被找到或者命令
被执行完成，则执行下一步，否则继续等待直到设置的最长等待时间截止。

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

    """
    隐式等待的好处是不用像强制等待(time.sleep(n))方法一样死等固定时间 n 秒，可以在一定程度上提升测试用例的执行效率。
    不过这种方法也存在一个弊端，那就是程序会一直等待整个页面加载完成，也就是说浏览器窗口标签栏中不再出现转动的小圆圈，
    才会继续执行下一步，比如某些时候想要的页面元素早就加载完成了，但由于个别 JS 等资源加载稍慢，此时程序仍然会等待页
    面全部加载完成才会继续执行下一步，这无形中加长了测试用例的执行时间。
    """
```

### 37.显式等待
```python
显式等待工作原理：
    程序会每隔一段时间(该时间一般都很短，默认0.5秒，也可以自定义)执行一下自定义的判定条件，如果条件成立，就执行下一步，
    否则继续等待，直到超过设定的最长等待时间，然后抛出 TimeoutException 异常。

示例代码略。
```

### 39.使用 Title 属性识别和操作新弹出的浏览器窗口
```python
test.html

<html>
    <head>
        <title>你喜欢的水果</title>
        <meta http-equiv="Content-Type" content="text/html"; charset="utf-8" />
    </head>
<body>
    <p id="p1">你爱吃的水果么？</p>
    <br><br>
    <a href="http://www.sogou.com" target="_blank">sogou 搜索</a>
</body>
</html>


def test_identifyPopUpWindowByTitle(self):
    # 导入多个异常类型
    from selenium.common.exceptions import NoSuchWindowException, TimeoutException
    # 导入期望场景类
    from selenium.webdriver.support import expected_conditions as EC
    # 导入 By 类
    from selenium.webdriver.common.by import By
    # 导入 WebDriverWait 类
    from selenium.webdriver.support.ui import WebDriverWait
    # 导入堆栈类
    import traceback
    # 导入时间模块
    import time
    url = "d:\\test.html"
    # 访问自定义测试网页
    self.driver.get(url)
    # 显式等待找到页面上链接文字为 "sogou 搜索" 的链接元素，找到后单击它
    WebDriverWait(self.driver, 10, 0.2).until(EC.element_to_be_clickable((By.LINK_TEXT, 'sogou 搜索'))).click()
    # 获取当前所有打开的浏览器窗口句柄
    all_handles = self.driver.window_handles
    # 打印当前浏览器窗口句柄
    print self.driver.current_window_handle
    # 打印打开的浏览器窗口的个数
    print len(all_handles)
    # 等待 2 秒，以便更好的查看效果
    time.sleep(2)
    # 如果存储浏览器窗口句柄的容器不为空，再遍历 all_handles 中所有的浏览器句柄
    if len(all_handles) > 0:
        try:
            for windowHandle in all_handles:
                # 切换窗口
                self.driver.switch_to.window(windowHandle)
                print self.driver.title
                # 判断当前浏览器窗口的 title 属性是否等于 "搜狗搜索引擎 - 上网从搜狗开始"
                if self.driver.title == u"搜狗搜索引擎 - 上网从搜狗开始":
                    # 显式等待页面搜索输入框加载完成，然后输入 "sogou 首页的浏览器窗口被找到"
                    WebDriverWait(self.driver, 10, 0.2).until(lambda x: x.find_element_by_id("query")).\
                        send_keys(u"sogou 首页的浏览器窗口被找到")
                    time.sleep(2)
        except NoSuchWindowException, e:
            # 捕获 NoSuchWindowException 异常
            print traceback.print_exc()
        except TimeoutException, e:
            # 捕获 TimeoutException 异常
            print traceback.print_exc()
    # 将浏览器窗口切换回默认窗口
    self.driver.switch_to.window(all_handles[0])
    print self.driver.title
    # 断言当前浏览器窗口的 title 属性是 "你喜欢的水果"
    self.assertEqual(self.driver.title, u"你喜欢的水果")
```

### 40.通过页面的关键内容识别和操作新浏览器窗口
```python
用于测试网页的 HTML 代码：同上一节一致。

def test_identifyPopUpWindowByPageSource(self):
    # 导入多个异常类型
    from selenium.common.exceptions import NoSuchWindowException, TimeoutException
    # 导入期望场景类
    from selenium.webdriver.support import expected_conditions as EC
    # 导入 By 类
    from selenium.webdriver.common.by import By
    # 导入 WebDriverWait 类
    from selenium.webdriver.support.ui import WebDriverWait
    # 导入堆栈类
    import traceback
    # 导入时间模块
    import time
    url = "d:\\test.html"
    # 访问自定义测试网页
    self.driver.get(url)
    # 显式等待找到页面上链接文字为 "sogou 搜索" 的链接元素，找到后单击它
    WebDriverWait(self.driver, 10, 0.2).until(EC.element_to_be_clickable((By.LINK_TEXT, 'sogou 搜索'))).click()
    # 获取当前所有打开的浏览器窗口句柄
    all_handles = self.driver.window_handles
    # 打印当前浏览器窗口句柄
    print self.driver.current_window_handle
    # 打印打开的浏览器窗口的个数
    print len(all_handles)
    # 等待 2 秒，以便更好的查看效果
    time.sleep(2)
    # 如果存储浏览器窗口句柄的容器不为空，再遍历 all_handles 中所有的浏览器句柄
    if len(all_handles) > 0:
        try:
            for windowHandle in all_handles:
                # 切换窗口
                self.driver.switch_to.window(windowHandle)
                # 获取当前浏览器窗口的页面源代码
                pageSource = self.driver.page_source
                if u"搜狗搜索" in pageSource:
                    # 显式等待页面搜索输入框加载完成，然后输入 "sogou 首页的浏览器窗口被找到"
                    WebDriverWait(self.driver, 10, 0.2).until(lambda x: x.find_element_by_id("query")).\
                        send_keys(u"sogou 首页的浏览器窗口被找到")
                    time.sleep(2)
        except NoSuchWindowException, e:
            # 如果没有找到浏览器的句柄，会抛出 NoSuchWindowException 异常，
            # 打印异常的堆栈信息
            print traceback.print_exc()
        except TimeoutException, e:
            # 显式等待超过规定时间后抛出 TimeoutException 异常
            print traceback.print_exc()
    # 将浏览器窗口切换回默认窗口
    self.driver.switch_to.window(all_handles[0])
    # 断言当前浏览器窗口页面源代码是否包含 "你爱吃的水果么？" 关键内容
    self.assertTrue(u"你爱吃的水果么？" in self.driver.page_source)
```

### 44.操作 JavaScript 的 Alert 弹窗
```python
目标：能够模拟鼠标单击弹出的 Alert 窗口上的 "确定" 按钮。

<html>
    <head>
        <title>你喜欢的水果</title>
        <meta http-equiv="Content-Type" content="text/html"; charset="utf-8" />
    </head>
<body>
    <input id="button" type="button" onclick="alert('这是一个 alert 弹出框');"value="单击此按钮，弹出 alert 弹窗" />
    </input>
</body>
</html>


def test_HandleAlert(self):
    from selenium.common.exceptions import NoAlertPresentException
    import time

    url = "d:\\alert.html"
    self.driver.get(url)
    # 通过 id 属性值查找页面上的按钮元素
    button = self.driver.find_element_by_id("button")
    # 单击按钮元素，则会弹出一个 Alert 消息框，上面显示 "这是一个 alert 弹出框" 和 "确定" 按钮
    button.click()
    try:
        # 使用 switch_to.alert() 方法获取 alert 对象
        alert = self.driver.switch_to.alert()
        time.sleep(2)
        # 使用 alert.text 属性获取 alert 框中的内容，并断言文字内容是否是 "这是一个 alert 弹出框"
        self.assertEqual(alert.text, u"这是一个 alert 弹出框")
        # 调用 alert 对象的 accept() 方法，模拟鼠标单击 alert 弹窗上的 "确定" 按钮，以便关闭 alert 框
        alert.accept()
    except NoAlertPresentException, e:
        # 如果 Alert 框未弹出显示在页面上，则会抛出 NoAlertPresentException 异常
        self.fail("尝试操作的 alert 框未被找到")
        print e
```

### 45.操作 JavaScript 的 confirm 弹窗
```python
目标：能够模拟鼠标单击 JavaScript 弹出的 confirm 框中的 "确定" 和 "取消" 按钮。

<html>
    <head>
        <title>你喜欢的水果</title>
        <meta http-equiv="Content-Type" content="text/html"; charset="utf-8" />
    </head>
<body>
    <input id="button" type="button" onclick="confirm('这是一个 alert 弹出框');" value="单击此按钮，弹出 confirm 弹窗" />
    </input>
</body>
</html>


def test_Handleconfirm(self):
    from selenium.common.exceptions import NoAlertPresentException
    import time

    url = "d:\\confirm.html"
    self.driver.get(url)
    # 通过 id 属性值查找页面上的按钮元素
    button = self.driver.find_element_by_id("button")
    # 单击按钮元素，则会弹出一个 confirm 消息框，上面显示 "这是一个 confirm 弹出框" 以及 "确定""取消" 按钮
    button.click()
    try:
        # 较高版本的 selenium 推荐使用 driver.switch_to.alert 方法代替 driver.switch_to_alert 方法来获取 alert 对象
        alert = self.driver.switch_to.alert()
        time.sleep(2)
        # 使用 alert.text 属性获取 confirm 框中的内容，并断言文字内容是否是 "这是一个 confirm 弹出框"
        self.assertEqual(alert.text, u"这是一个 confirm 弹出框")
        # 调用 alert 对象的 accept() 方法，模拟鼠标单击 confirm 弹窗上的 "确定" 按钮，以便关闭 confirm 框
        alert.accept()
        # 取消下面一行代码的注释，就会模拟单击 confirm 框上的 "取消" 按钮
        # alert.dismiss()
    except NoAlertPresentException, e:
        # 如果 confirm 框未弹出显示在页面上，则会抛出 NoAlertPresentException 异常
        self.fail("尝试操作的 confirm 框未被找到")
        print e
```

### 46.操作 JavaScript 的 prompt 弹窗
```python
目标：能够在 JavaScript 的 prompt 弹窗中输入自定义的内容，并单击 "确定" 和 "取消" 按钮。

<html>
    <head>
        <title>你喜欢的水果</title>
        <meta http-equiv="Content-Type" content="text/html"; charset="utf-8" />
    </head>
<body>
    <input id="button" type="button" onclick="prompt('这是一个 prompt 弹出框');" value="单击此按钮，弹出 prompt 弹出框" />
    </input>
</body>
</html>


def test_HandlePrompt(self):
    url = "d:\\prompt.html"
    self.driver.get(url)
    # 使用 id 定位方式，找到被测试网页上唯一按钮元素
    element = self.driver.find_element_by_id("button")
    element.click()
    import time
    time.sleep(1)
    # 单击按钮元素，弹出一个 prompt 提示框，上面将显示 "这是一个 prompt 弹出框"、输入框、"确定" 按钮、"取消" 按钮
    # 使用 driver.switch_to.alert 方法获取 Alert 对象
    alert = self.driver.switch_to.alert
    # 使用 alert.text 属性获取 prompt 框上面的文字，并断言文字内容是否和 "这是一个 prompt 弹出框" 一致
    self.assertEqual(u"这是一个 prompt 弹出框", alert.text)
    time.sleep(1)
    # 调用 alert.send_keys() 方法，在 prompt 窗体的输入框中输入 "光荣之路：要想改变命运，必须每天学习 2 小时！"
    alert.send_keys(u"光荣之路：要想改变命运，必须每天学习 2 小时！")
    time.sleep(1)
    # 使用 alert 对象的 accept() 方法，单击 prompt 弹窗上的 "确定" 按钮，关闭 prompt 框
    alert.accept()
    # 使用 alert 对象的 dismiss() 方法，单击 prompt 弹窗上的 "取消" 按钮，关闭 prompt 框
    # alert.dismiss()
```

### 47.操作浏览器的 Cookie
```python
目标：能够遍历输出 Cookie 信息中所有的 key 和 value ；能够删除指定的 Cookie 对象；能够删除所有的 Cookie 对象。

def test_Cookie(self):
    url = "http://www.sogou.com"
    self.driver.get(url)
    # 得到当前页面下所有的 Cookies，并输出它们所在域、name、value、有效期和路径
    cookies = self.driver.get_cookies()
    for cookie in cookies:
        print "%s -> %s -> %s -> %s -> %s" % (cookie['domain'], cookie['name'], cookie['value'],
                                              cookie['expiry'], cookie['path'])

    # 根据 Cookie 的 name 值获取该条 Cookie 信息，获取 name 值为 "SUV" 的 Cookie 信息
    ck = self.driver.get_cookie("SUV")
    print "%s -> %s -> %s -> %s -> %s" % (ck['domain'], ck['name'], ck['value'], ck['expiry'], ck['path'])

    # 删除 cookie 有两种方法
    # 第一种：通过 Cookie 的 name 属性，删除 name 值为 "ABTEST"的 Cookie 信息
    print self.driver.delete_cookie("ABTEST")

    # 第二种：一次性删除全部的 Cookie 信息
    self.driver.delete_all_cookies()
    # 删除全部 Cookie 后，再次查看 Cookie，确认是否已被全部删除
    cookies = self.driver.get_cookies()
    print cookies

    # 添加自定义的 Cookie 信息
    self.driver.add_cookie({"name": "gloryroadTrain", "value": "1479697159269020"})
    # 查看添加的 Cookie 信息
    cookie = self.driver.get_cookie("gloryroadTrain")
    print cookie
```

### 48.指定页面加载时间
```python
在实施自动化测试过程中，经常会遇到加载某一个页面需要等待很长时间，其实页面基本元素都已经加载完成，可以进行后续操作，
而 Selenium WebDriver 在执行 get 方法时会一直等待页面完全加载完毕以后才会执行后续操作，这无形中增加了自动化测试的时间，
针对此种情况，就需要指定一下页面加载超时时间，到达等待时间点不再继续等待加载，而是继续执行后续操作。

# encoding=utf-8
from selenium import webdriver
from selenium.common.exceptions import TimeoutException
from selenium.webdriver.common.keys import Keys
import time
import unittest


class setPageLoadTime(unittest.TestCase):

    def setUp(self):
        # 启动 Firefox 浏览器
        self.driver = webdriver.Firefox()

    def test_PageLoadTime(self):
        # 设定页面加载限制时间为 4 秒
        self.driver.set_page_load_timeout(4)
        self.driver.maximize_window()
        try:
            global startTime
            startTime = time.time()
            self.driver.get("http://mail.126.com")
        except TimeoutException:
            print u"页面加载超过设定时间，超时"
            # 当页面加载时间超过设定时间，通过执行 Javascript 来停止加载，然后继续执行后续动作
            self.driver.execute_script("window.stop()")
        end = time.time() - startTime
        print end
        # 切换进 frame 控件
        self.driver.switch_to.frame("x - URS - iframe")
        # 获取用户名输入框
        userName = self.driver.find_element_by_xpath('//input[@name="email"]')
        # 输入用户名
        userName.send_keys("xxx")
        # 获取密码输入框
        pwd = self.driver.find_element_by_xpath('//input[@name="password"]')
        # 输入密码
        pwd.send_keys("xxx")
        # 发送一个 Enter 键
        pwd.send_keys(Keys.RETURN)

    def tearDown(self):
        self.driver.quit()

if __name__ == "__main__":
    unittest.main()
```