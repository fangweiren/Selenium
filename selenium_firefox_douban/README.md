# Selenium Firefox 模拟登录

### Ubuntu 用户安装或升级使用下面的命令（支持所有版本 Ubuntu 系统）
```python
sudo apt-get update
sudo apt-get install firefox
```

### 查看版本
打开firefox，点菜单栏Help->About Firefox

### Firefox 安装路径
1.打开一个火狐浏览器
2.打开一个终端，输入：ps -ef | grep firefox

### Python selenium 模块使用出错解决，Message: 'geckodriver' executable needs to be in PATH
1、下载 geckodriver 地址： https://github.com/mozilla/geckodriver/releases
2、解压后将 geckodriver 存放至 /usr/local/bin/ 路径下即可

### Selenium 使用 send_keys() 方法写中文报错
Python2.7 + Selenium 使用 utf-8 编码的中文作为参数调用 send_keys() 方法, utf8 编码不能按照我们预期的填入对应的搜索框内。怎么办呢？
可以使用解码的方式，把 utf8 编码变为 unicode
具体步骤：
driver.find_element_by_name("q").send_keys('灵魂摆渡')
修改为：driver.find_element_by_name("q").send_keys('灵魂摆渡'.decode())
或者：dirver.find_element_by_name("q").send_keys(u'灵魂摆渡')

### Python+Selenium 刷新当前页面
```python
try:  
    driver.refresh() # 刷新方法 refresh  
    print ('test pass: refresh successful')  
except Exception as e:  
    print ("Exception found", format(e))
```

### 设置禁用图片、css、flash、javascript
```python
firefox_profile = webdriver.FirefoxProfile()
# 不下载和加载图片
firefox_profile.set_preference('permissions.default.image', 2)
# 禁用 css
firefox_profile.set_preference('permissions.default.stylesheet', 2)
# 禁用 flash
firefox_profile.set_preference('dom.ipc.plugins.enabled.libflashplayer.so', 'false')
# 禁用 js
firefox_profile.set_preference('javascript.enabled', 'false')
firefox_profile.update_preferences()
driver = webdriver.Firefox(firefox_profile=firefox_profile)
```

### 三种等待方式
1.强制等待
time.sleep(5)

2.隐式等待
```python
driver = webdriver.Firefox() 
driver.implicitly_wait(30) # 隐性等待，最长等30秒 
driver.get('https://huilansame.github.io')
```
隐式等待是设置了一个最长等待时间，如果在规定时间内网页加载完成，则执行下一步，否则一直等到时间截止，然后执行下一步。注意这里有一个弊端，那就是程序会一直等待整个页面加载完成，也就是一般情况下你看到浏览器标签栏那个小圈不再转，才会执行下一步，但有时候页面想要的元素早就在加载完成了，但是因为个别js之类的东西特别慢，我仍得等到页面全部完成才能执行下一步，我想等我要的元素出来之后就下一步怎么办？有办法，这就要看selenium提供的另一种等待方式——显性等待wait了。

3.显式等待
显性等待 WebDriverWait，配合该类的 until() 和 until_not() 方法，就能够根据判断条件而进行灵活地等待了。它主要的意思就是：程序每隔xx秒看一眼，如果条件成立了，则执行下一步，否则继续等待，直到超过设置的最长时间，然后抛出TimeoutException。
```python
from selenium import webdriver
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By

driver = webdriver.Firefox()
driver.implicitly_wait(10) # 隐性等待和显性等待可以同时用，但要注意：等待的最长时间取两者之中的大者
driver.get('https://huilansame.github.io';)
locator = (By.LINK_TEXT, 'CSDN')
try:
    WebDriverWait(driver, 20, 0.5).until(EC.presence_of_element_located(locator))
    print driver.find_element_by_link_text('CSDN').get_attribute('href')
finally:
    driver.close()
```
参数解释：
```python
WebDriverWait(driver=self.driver, timeout=300, poll_frequency=0.5,  ignored_exceptions=None)
```
driver：浏览器驱动
timeout：最长超时等待时间
poll_frequency：检测的时间间隔，默认为500ms
ignore_exception：超时后抛出的异常信息，默认情况下抛 NoSuchElementException 异常
[Python selenium —— 一定要会用selenium的等待，三种等待方式解读](https://blog.csdn.net/huilan_same/article/details/52544521)

### ubuntu 16.04 服务器上配置 selenium + firefox
1.安装 Python
`sudo apt-get install python`
2.更新 apt-get
`sudo apt-get update`
3.安装 selenium
`sudo pip install selenium`
4.安装 firefox
`sudo apt-get install firefox`
5.安装 Xvfb
`sudo apt-get install xvfb`
6.安装 pyvirtualdisplay
`sudo pip install pyvirtualdisplay`
7.安装 geckodriver
下载好了上传到服务器(scp 命令)放到/usr/bin/路径下
cp geckodriver /usr/bin
8.修改权限
`sudo chmod a+w geckodriver`
[ubuntu16.04新服务器上配置selenium+firefox](https://www.cnblogs.com/lgh344902118/p/6285278.html)

### Message: Process unexpectedly closed with status 1
This error can come up when you are trying to run the browser in non-headless mode on a box that doesn't have a display (like an Ubuntu server).
当您尝试在没有显示器的盒子（如Ubuntu服务器）上以非无头模式运行浏览器时，会出现此错误。
```python
from selenium import webdriver
from selenium.webdriver import FirefoxOptions

opts = FirefoxOptions()
opts.add_argument("--headless")
browser = webdriver.Firefox(firefox_options=opts)

browser.get('http://example.com';)
```
[Webdriver Exception:Process unexpectedly closed with status: 1](https://stackoverflow.com/questions/46809135/webdriver-exceptionprocess-unexpectedly-closed-with-status-1)
