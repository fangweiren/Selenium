## 1.����ĳ����ַ
```python
def test_visitURL():
	visitURL = "http://www.sougou.com"
	# ͨ�� driver ����� get ����������ָ������ַ
	driver.get(visitURL)
	assert driver.title.find(u'�ѹ���������') >= 0, "assert error"
```

## 2.��ҳ��ǰ���ͺ���

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