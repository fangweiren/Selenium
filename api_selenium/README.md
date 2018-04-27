## 1.访问某个网址
```python
def test_visitURL():
	visitURL = "http://www.sougou.com"
	# 通过 driver 对象的 get 方法，访问指定的网址
	driver.get(visitURL)
	assert driver.title.find(u'搜狗搜索引擎') >= 0, "assert error"
```

## 2.网页的前进和后退

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