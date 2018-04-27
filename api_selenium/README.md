## 1.����ĳ����ַ
```python
def test_visitURL():
	visitURL = "http://www.sougou.com"
	# ͨ�� driver ����� get ����������ָ������ַ
	driver.get(visitURL)
	assert driver.title.find(u'�ѹ���������') >= 0, "assert error"
```

## 2.��ҳ��ǰ���ͺ���
```python
def test_visitRecentURL():
    firstVisitURL = "http://www.sougou.com"
    secondVisitURL = "http://www.baidu.com"
    # ���ȷ��� sougou ��ҳ
    driver.get(firstVisitURL)
    # Ȼ����� baidu ��ҳ
    driver.get(secondVisitURL)
    # ������һ�η��ʹ����ѹ���ҳ
    driver.back()
    # �ٴλص��ٶ���ҳ
    driver.forward()
```

## 3.ˢ�µ�ǰҳ��
```python
def test_refreshCurrentPage():
    url = "http://www.iamnancy.top"
    driver.get(url)
    time.sleep(5)
    # ˢ�µ�ǰҳ��
    driver.refresh()
```

## 4.������������
```python
def test_maximizeWindow():
    url = "http://www.iamnancy.top"
    driver.get(url)
    # �����������ڣ��Ա�ռ������������Ļ
    driver.maximize_window()
```

## 5.��ȡ�����õ�ǰ���ڵ�λ��
```python
def test_window_position():
    url = "http://www.iamnancy.top"
    driver.get(url)
    # ��ȡ��ǰ���������Ļ�ϵ�λ�ã����ص����ֵ����
    position = driver.get_window_position()
    print "��ǰ���������λ�õĺ����꣺", position['x']
    print "��ǰ���������λ�õ������꣺", position['y']
    # ���õ�ǰ���������Ļ�ϵ�λ��
    driver.set_window_position(y=200, x=400)
    # �����������λ�ú��ٴλ�ȡ�������λ����Ϣ
    print driver.get_window_position()

    """
    1.��ȡ�������λ����ָ��������Ͻ����ڵ���Ļ�ϵ�λ�ã����ص��� x,y ����ֵ�����������ꡣ
    2.get_window_position() �� set_window_position() �����ڲ���������Ĳ��ְ汾��ʧЧ��
    """
```