# -*-coding:utf-8-*-

import pandas as pd

X = pd.read_table(r'/Users/liu/practice/abc_play/play/hos.csv', usecols=(0, 1, 2), sep=',', header=None)
# Y = pd.read_table(r'F:\Python资料\第五阶段\资料\dating.txt',usecols=(3,),sep='\t')
# Z = pd.read_csv(r'C:\Users\Administrator\Desktop\t_lianjia.csv',usecols=(0,),sep='\s+',header=None)   # 如果文件没有标题行，也可将header参数设置为None
# print(X)
print(X.T)    # 转置（行变成列，列变成行）

# print(X.head(5))    # 查看前5行
# print(X.tail(5))    # 查看后5行
# print(X[15:20])       # 做切片，只能以行做切片，不能以列做切片

# print(X.columns)    # 查看列名
# X.columns = ['x1','x2','x3']      # 修改列名
# print(X.tail(5))
# print(X.values)   # 显示所有数据

# print(X.describe())   # 显示对数据的统计（数量，最大值，最小值，平均值等信息）
# print('----------------------')
# print(X.max())    # 返回每列的最大值
# print(X.min())    # 返回每列的最小值
# print(X.mean())   # 返回每列的平均值
# print(X.std())    # 返回每列的方差

# print(X.sort_index(axis=1))   # 按照轴对索引进行排序
# print(X.sort_values(by=['salary','taobao']))  # 按照值对列进行排序，多个列排序，按照列表的顺序排序

# print(X['salary'])   # 以key，value的形式访问一列数据
# print(X.salary)      # 以属性的形式访问一列数据
#
# 通过标签来选择查看数据
# print(X.loc[3:5,'taobao':'tv'])   # 支持对行列同时做切片，支持以列名的形式
# print(X.loc[3,'tv'])      # 以行列坐标的形式、取出一个值(行标为3，列名为tv的值)
# print(X.at[3,'tv'])     # 快速取值，同上
# print(X.loc[1,1])     # 错误的使用方式，列只支持列名的索引

# 通过下标来查看数据
# print(X.iloc[1:3,1:])   # 通过下标来做切片
# print(X.iloc[4,1])      # 以下标的形式取值
# print(X.iat[4,2])      # 快速通过下标取值
# print(X.iloc[2:5,:])     # 取出某些连续行
# print(X.iloc[[2,8,3,9],:])    # 取出某些非连续行

# 过滤数据
# print(X[X.salary>40000][X.salary<60000])    # 根据布尔条件过滤值
# print(X[60000>X.salary>40000])    #  会报错，不支持连续比较

# 删除重复数据
# X.drop_duplicates(['salary'],keep='last',inplace=True)
# print(len(X))
# keep决定保存先出现的数据，还是保存后出现的数据
# inplace 决定是否作用于原来的DataFrame

# DataFrame使用
# data = []
# data.append([1,2])
# data.append([3,4,5])
# print(pd.DataFrame(data).fillna(0))    # 缺失值默认填充NaN，可以通过fillna修改填充的值
