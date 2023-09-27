1、通过pd.unique()方法可以查看某列数据中含有的所有不同值
cate_data = pd.Series(['apple', 'apple', 'orange', 'apple']*2)
pd.unique(cate_data)



2、通过pd.value_counts()方法，可以统计一列数据中，各不同值出现的次数。（即默认会对一列中的元素去重计数）
pd.value_counts(cate_data)



3、通过take()方法，可以使得序列或者dataframe按照已有的整数序列中数字的顺序进行排列和扩展

#创建一个特定顺序和长度的整数序列
values_take = pd.Series([0, 1, 0, 0]*2)

#创建一个分类数据序列
cate_take = pd.Series('apple', 'Samsung')

#通过take()方法，将原分类序列，按照整数序列进行排序和扩展
cate_take.take(values_take)
