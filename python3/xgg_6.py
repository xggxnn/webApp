# -*- coding: UTF-8 -*-

# Filename : xgg_6.py
# author by : xggxnn.top

# desc:冒泡排序

import random

def bubbleSort(arr):
	n = len(arr)

	# 遍历所有数组元素
	for i in range(n):
		
		# Last i ele are already in place
		for j in range(0,n-i-1):
			
			if arr[j] > arr[j+1]:
				arr[j],arr[j+1] = arr[j+1],arr[j]

arr = []
for i in range(1,10):
	arr.append(random.randint(1,100))

print("排序前的数组：")
for i in range(len(arr)):
	print ("%d" %arr[i],end=",")

bubbleSort(arr)
print()
print("排序后的数组：")
for i in range(len(arr)):
	print ("%d" %arr[i],end=",")