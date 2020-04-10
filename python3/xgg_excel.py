# -*- coding: UTF-8 -*-

# Filename : xgg_excel.py
# author by : xggxnn.top

# desc:解析excel

import xlrd
import csv

# xls_path xls文件路径 // 绝对路径
# saveDict 保存文件的文件夹路径 // 绝对路径
def read_xsls(xls_path,saveDict):
	data_xsls = xlrd.open_workbook(xls_path) 			# 打开次地址下的exl文件
	data_sheetsss = data_xsls.sheets()					# 获取所有sheet页签内容
	for kkk in range(0,len(data_sheetsss)):				# 遍历所有sheet
		data_sheet = data_sheetsss[kkk]
		rowNum = data_sheet.nrows 						# 行数
		colNum = data_sheet.ncols 						# 列数
		heards = []										# 表头，也就第一行
		for i in range(colNum):
			heards.append(data_sheet.cell_value(0,i))
		dicts = []										# 具体内容
		for i in range(1,rowNum):
			items = {}
			for j in range(colNum):
				items[heards[j]] = data_sheet.cell_value(i,j)
			dicts.append(items)
		csv_savepath = saveDict + data_sheet.name + ".csv"		#写入文件路径
		with open(csv_savepath,'w',newline='',encoding='utf-8') as f:
			f_csv = csv.DictWriter(f,heards)
			f_csv.writeheader()
			f_csv.writerows(dicts)
	print("\n over")

read_xsls("d://配置表 (1).xlsx","d://testcsv//")