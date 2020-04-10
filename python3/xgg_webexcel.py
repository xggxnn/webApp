#!/usr/bin/env python3
# -*- coding: UTF-8 -*-

# Filename : xgg_webexcel.py
# author by : xggxnn.top

# desc:抓取网页并写入excel

from urllib import request
from html.parser import HTMLParser
from html.entities import name2codepoint

header = {
	'Refere':'https://www.mzitu.com',
	'User-Agent':'Mozilla/6.0 (iPhone; CPU iPhone OS 8_0 like Mac OS X) AppleWebKit/536.26 (KHTML, like Gecko) Version/8.0 Mobile/10A5376e Safari/8536.25'
}


# with request.urlopen("https://www.python.org/events/python-events/") as f:
# 	data = f.read()
# 	print('Status:',f.status,f.reason)
# 	for k,v in f.getheaders():
# 		print('%s:%s'%(k,v))
# 	# print('\n\nData:',data.decode('utf-8'))

# class MyHTMLParser(HTMLParser):

#     def handle_starttag(self, tag, attrs):
#         print('<%s>' % tag)

#     def handle_endtag(self, tag):
#         print('</%s>' % tag)

#     def handle_startendtag(self, tag, attrs):
#         print('<%s/>' % tag)

#     def handle_data(self, data):
#         print(data)

#     def handle_comment(self, data):
#         print('<!--', data, '-->')

#     def handle_entityref(self, name):
#         print('&%s;' % name)

#     def handle_charref(self, name):
#         print('&#%s;' % name)

# print("---------------------------------")
# parser = MyHTMLParser()
# parser.feed('''<html>
# <head></head>
# <body>
# <!-- test html parser -->
#     <p>Some <a href=\"#\">html</a> HTML&nbsp;tutorial...<br>END</p>
# </body></html>''')


# import urllib.request
# url = "https://tower.txdocs.qq.com/sheet/DUFFFcFp6ZU5rWXZJ?tab=mnnebn&coord=H4A0A0"
# html = urllib.request.urlopen(url)
# print(html.read().decode("utf-8"))