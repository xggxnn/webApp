# -*- coding: UTF-8 -*-

# Filename : xgg_1.py
# author by : xggxnn.top

# desc:计算每个月天数

import calendar

yy = int(input("请输入年份："))
for i in range(1,13):
	print("{}年\t".format(yy),"{}月\t".format(i),"有{}天\t".format(calendar.monthrange(yy,i)[1]))