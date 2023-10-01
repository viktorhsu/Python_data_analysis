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

#通过groupby()方法中的dropna=False参数，可以不去除数据中的空值
df1["data1"].groupby([df1['key1'], df1['key2']], dropna=False).mean()

#通过size()聚合方法，可以统计每组数据的行数，包括空行。即所有列均为空值，才为空行。
df1["data1"].groupby([df1['key1'], df1['key2']], dropna=False).size()

#通过count()聚合方法，可以统计每组数据的行数，不包括空行
df1["data1"].groupby([df1['key1'], df1['key2']], dropna=False).count()




2、可以将分组键设置为非该数据集内的与数据长度相等的其他序列
#自定义分组键以及分组键的类别值，并且根据该自定义的分组键和值进行分组
states = np.array(["OH", "CA", "CA", "OH", "OH", "CA", "OH"])
years = [2005, 2005, 2006, 2005, 2006, 2005, 2006]

df1["data1"].groupby([states, years]).mean()



3、可以同时对数据内的多列值进行分组，按照单个或者多个分组键进行分组聚合

df1.groupby([df1['key1'], df1['key2']]).mean()



4、通过设置聚合函数中的numeric_only=True参数，可以使得分组聚合计算，只考虑数值型列
df1.groupby(["key2"]).mean(numeric_only=True)



5、可以对分出的组进行迭代输出
#对分组键为k1和k2分组的各组合进行迭代
for (k1, k2), group in df1["data1"].groupby([df1['key1'], df1['key2']], dropna=False):
    print((k1, k2))
    print(group)



6、可以将分组结果存储到字典中
dict_group = {name: group for name, group in df1.groupby("key1")}




7、可以通过对group()方法设置参数axis='columns'以及以字典的形式设置分组键（或者序列的方式，键名为索引，键值为新的分组名），从而按列进行分组
#按列进行分组
groupped = df1.groupby({'key1': 'key', 'key2': 'key', 'data1': 'key', 'data2': 'data'}, axis='columns')
#对分好的组进行迭代输出
for groub_key, group_value in groupped:
    print(groub_key)
    print(group_value)



8、更便捷的调用groupby方法
#以类似属性的方式调用
df1.groupby(['key1', 'key2'])['data1'].mean()
#和原复杂方法对比
df1['data1'].groupby([df1['key1'], df1['key2']]).mean()



9、可以通过以特定的函数来对数据进行分组，将函数结果值相同的作为一组。分组后的数据索引值为各函数值。
#将分组的原数据
group_people = pd.DataFrame(np.random.standard_normal((5, 5)),
                      columns=["a", "b", "c", "d", "e"],
                      index=["Joe", "Steve", "Wanda", "Jill", "Trey"])
group_people.iloc[2:3, [1, 2]] = np.nan # Add a few NA values

#按照索引名称含有的字符个数进行分组，获取字符个数的函数为len
group_people.groupby(len).sum()



10、对具有多级索引的数据，可以按照索引层级进行分组
#将分组的原数据
columns = pd.MultiIndex.from_arrays([["US", "US", "US", "JP", "JP"],
                                     [1, 3, 5, 1, 3]],
                                    names=["cty", "tenor"])
group_hier = pd.DataFrame(np.random.standard_normal((4, 5)), columns=columns)

#按照索引层级进行分组，由于该数据只有列索引具有多级索引，故此处只能对列的进行分组
#对最外层列索引进行分组
group_hier.groupby(level=0, axis="columns").count()

#对第二次列索引进行分组
group_hier.groupby(level=1, axis="columns").count()



11、可以通过agg()方法，按照自定义的函数进行分组，可以一次传入多个函数

df1.groupby(['key1'])['data1'].agg(['mean', peak_to_peak])

#还可以对分组的聚合函数以元组的方式或者字典的方式重命名。如果以元组的方式，则新的名字在前面。如果以字典的方式，则新的名字为键。
df1.groupby(['key1'])['data1'].agg([('平均值', 'mean'), ('极差', peak_to_peak)])



12、可以使用字典格式与agg()方法结合，从而对不同的列使用不同的聚合函数，然后再进行分组，并且默认情况下，分组后各列的列名不会改变
#对data1数据列使用mean()和max()函数，对data2列使用sum()和min()函数
df1.groupby(['key1', 'key2']).agg({'data1': ['mean', 'max'], 'data2': ['sum', 'min']})



13、默认情况下，均为将分组的键名作为分组后的索引，可以通过as_index=False, 使得索引重置为整数索引，而分组的键名转换成前几列



14、通过apply()方法，可以对groupby()方法分组后使用自定义非聚合函数，且分组结果中，分组键除了会作为索引外，原始列位置也会保留
#自定义一个默认只取前5个的函数
def top(df, n=5, column="total_bill"):
    return df.sort_values(column, ascending=False)[:n]

#通过apply()方法，对分组的数据应用此函数
group_mutifun.groupby('smoker').apply(top)



15、通过对使用apply()方法进行聚合分组的数据，在groupby方法中设置group_keys=False参数，可以使得分组结果中，去除分组键构成的索引

group_mutifun.groupby('smoker', group_keys=False).apply(top)



16、可以将函数传入至transform()中，从而将函数值在每个组内的每行数据中都输出，而不是每个组只能输出一个，不过此时行索引也变成了整数索引
#通过将mean传入给transform中，分组后的结果中，每行数据均有平均值
df1['data1'].groupby([df1['key1']]).transform('mean')



17、


