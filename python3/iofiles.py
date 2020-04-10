# -*- coding: UTF-8 -*-

# Filename : iofiles.py
# author by : xggxnn.top

# 写文件
with open("test.txt","wt") as out_file:
	out_file.write("写入内容\n换行")

# Read a file
with open("test.txt","rt") as in_file:
	txt = in_file.read()

print(txt)

# for i in range(1,10):
# 	astrss = "xgg_{0}.py".format(i)
# 	with open(astrss,"wt") as out_file:
# 		out_file.write("# -*- coding: UTF-8 -*-\n\n")
# 		out_file.write("# Filename : {0}\n".format(astrss))
# 		out_file.write("# author by : xggxnn.top\n\n")
# 		out_file.write("# desc:")


# Python 字符串判断
# Python 字符串大小写转换
# Python 计算每个月天数
# Python 获取昨天日期
# Python list 常用操作
# Python 约瑟夫生者死者小游戏
# Python 五人分鱼
# Python 实现秒表功能
# Python 计算 n 个自然数的立方和
# Python 计算数组元素之和
# Python 数组翻转指定个数的元素
# Python 将列表中的头尾两个元素对调
# Python 将列表中的指定位置的两个元素对调
# Python 翻转列表
# Python 判断元素是否在列表中存在
# Python 清空列表
# Python 复制列表
# Python 计算元素在列表中出现的次数
# Python 计算列表元素之和
# Python 计算列表元素之积
# Python 查找列表中最小元素
# Python 查找列表中最大元素
# Python 移除字符串中的指定位置字符
# Python 判断字符串是否存在子字符串
# Python 判断字符串长度
# Python 使用正则表达式提取字符串中的 URL
# Python 将字符串作为代码执行
# Python 字符串翻转
# Python 对字符串切片及翻转
# Python 按键(key)或值(value)对字典进行排序
# Python 计算字典值之和
# Python 移除字典点键值(key/value)对
# Python 合并字典
# Python 将字符串的时间转换为时间戳
# Python 获取几天前的时间
# Python 将时间戳转换为指定格式日期
# Python 打印自己设计的字体
# Python 二分查找
# Python 线性查找
# Python 插入排序
# Python 快速排序
# Python 选择排序
# Python 冒泡排序
# Python 归并排序
# Python 堆排序
# Python 计数排序
# Python 希尔排序
# Python 拓扑排序