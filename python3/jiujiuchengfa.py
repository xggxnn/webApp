# -*- coding: UTF-8 -*-

# Filename : jiujiuchengfa.py
# author by : xggxnn.top

# 九九乘法表
for i in range(1,10):
	for j in range(1,i+1):
		print('{0}X{1}={2}\t'.format(j,i,i*j),end='')
	print("")