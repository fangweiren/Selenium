## 1.访问某个网址
```python
def test_visitURL():
	visitURL = "http://www.sougou.com"
	# 通过 driver 对象的 get 方法，访问指定的网址
	driver.get(visitURL)
	assert driver.title.find(u'搜狗搜索引擎') >= 0, "assert error"
```

## 2.网页的前进和后退
```python
def test_visitRecentURL():
    firstVisitURL = "http://www.sougou.com"
    secondVisitURL = "http://www.baidu.com"
    # 首先访问 sougou 首页
    driver.get(firstVisitURL)
    # 然后访问 baidu 首页
    driver.get(secondVisitURL)
    # 返回上一次访问过的搜狗首页
    driver.back()
    # 再次回到百度首页
    driver.forward()
```

## 3.刷新当前页面
```python
def test_refreshCurrentPage():
    url = "http://www.iamnancy.top"
    driver.get(url)
    time.sleep(5)
    # 刷新当前页面
    driver.refresh()
```

## 4.浏览器窗口最大化
```python
def test_maximizeWindow():
    url = "http://www.iamnancy.top"
    driver.get(url)
    # 最大化浏览器窗口，以便占满整个电脑屏幕
    driver.maximize_window()
```

## 5.获取并设置当前窗口的位置
```python
def test_window_position():
    url = "http://www.iamnancy.top"
    driver.get(url)
    # 获取当前浏览器在屏幕上的位置，返回的是字典对象
    position = driver.get_window_position()
    print "当前浏览器所在位置的横坐标：", position['x']
    print "当前浏览器所在位置的纵坐标：", position['y']
    # 设置当前浏览器在屏幕上的位置
    driver.set_window_position(y=200, x=400)
    # 设置浏览器的位置后，再次获取浏览器的位置信息
    print driver.get_window_position()

    """
    1.获取的浏览器位置是指浏览器左上角所在的屏幕上的位置，返回的是 x,y 坐标值，即横纵坐标。
    2.get_window_position() 和 set_window_position() 方法在部分浏览器的部分版本上失效。
    """
```