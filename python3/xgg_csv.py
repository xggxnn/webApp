# -*- coding: UTF-8 -*-

# Filename : xgg_csv.py
# author by : xggxnn.top

# desc:解析.cvs文件

import csv

XLS_PATH = "https://tower.txdocs.qq.com/sheet/DUFFFcFp6ZU5rWXZJ?tab=mnnebn&coord=H4A0A0"
# XLS_PATH 文件路径 model:打开文件的方式 encoding 编码
with open(XLS_PATH,mode = 'r', encoding = 'utf-8') as f:
	reader = csv.reader(f)
	print(reader)
	# for row in reader:
	# 	if row[0] == '':
	# 		continue
	# 	print(row)
		# dic = {}
		# dic.update(phone=row[0])
		# dic.update(remark=row[1])
		# contacts.append(dic)
	# print(contacts)