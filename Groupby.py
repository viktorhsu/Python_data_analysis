1、简单groupby方法聚合
df1 = pd.DataFrame({"key1" : ["a", "a", None, "b", "b", "a", None],
                   "key2" : pd.Series([1, 2, 1, 2, 1, None, 1],
                                      dtype="Int64"),
                   "data1" : np.random.standard_normal(7),
                   "data2" : np.random.standard_normal(7)})

#对指定的数据，按照指定的单个分组键，求解分组平均值，分组键名会被转换成索引
df1["data1"].groupby(df1['key1']).mean()

#对指定的数据，按照指定的两个或多个分组，求解分组平均值，分组键名会被转换成索引
df1["data1"].groupby([df1['key1'], df1['key2']]).mean()



2、可以将分组键设置为非该数据集内的与数据长度相等的其他序列
#自定义分组键以及分组键的类别值，并且根据该自定义的分组键和值进行分组
states = np.array(["OH", "CA", "CA", "OH", "OH", "CA", "OH"])
years = [2005, 2005, 2006, 2005, 2006, 2005, 2006]

df1["data1"].groupby([states, years]).mean()



3、可以同时对数据内的多列值进行分组，按照单个或者多个分组键进行分组聚合

df1.groupby([df1['key1'], df1['key2']]).mean()



4、通过设置聚合函数中的numeric_only=True参数，可以使得分组聚合计算，只考虑数值型列
df1.groupby(["key2"]).mean(numeric_only=True)





