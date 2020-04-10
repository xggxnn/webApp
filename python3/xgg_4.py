# -*- coding: UTF-8 -*-

# Filename : xgg_4.py
# author by : xggxnn.top

# desc:使用正则表达式提取字符串中的 URL

import re

def Find(string):
	url = re.findall('https?://(?:[-\w.]|(?:%[\da-fA-F]{2}))+',string)
	return url

string = 'Runoob 的网页地址为：https://www.runoob.com.cn,Google的网站为：https://www.google.com,百度地址：https://baidu.com'
print("Urls:",Find(string))