# -*- coding: UTF-8 -*-

# Filename : xgg_2.py
# author by : xggxnn.top

# desc:获取日期

import datetime
# 一天
def getOneDay():
	return datetime.timedelta(days=1)
# 今天
def getToDay():
	return datetime.date.today()
# 昨天
def getYesterday():
	yesterday = getToDay() - getOneDay()
	return yesterday
# 明天
def getTomorrowDay():
	tomorrow = getToDay() + getOneDay()
	return tomorrow

# 输出
print("昨天：{}，今天：{}，明天：{}".format(getYesterday(),getToDay(),getTomorrowDay()))
