1、具有相同列的数据集的连接：通过pd.merge()方法可以对2个或者多个数据集进行连接，内连接，外连接，左连接，右连接等
#连接规则为根据对2个数据集指定的2歌键列中的值进行匹配
merge_df1 = pd.DataFrame({"key": ["b", "b", "a", "c", "a", "a", "b"],
                          "data1": pd.Series(range(7), dtype="Int64")})

merge_df2 = pd.DataFrame({"key": ["a", "b", "d"],
                          "data2": pd.Series(range(3), dtype="Int64")})

#内连接：how='inner'
pd.merge(merge_df1, merge_df2, how = 'inner', on = 'key')

#外连接：how='outer'
pd.merge(merge_df1, merge_df2, how = 'outer', on = 'key')

#左连接：how='left'
pd.merge(merge_df1, merge_df2, how = 'left', on = 'key')

#右连接：how='right'
pd.merge(merge_df1, merge_df2, how = 'right', on = 'key')



2、没有相同列的数据集的连接：通过设置pd.merge()方法中，left_on和right_on参数，以指定两个数据集连接的不同列.内连接，左连接，外连接，右连接等。
merge_columndf1 = pd.DataFrame({"lkey": ["b", "b", "a", "c", "a", "a", "b"],
                                "data1": pd.Series(range(7), dtype="Int64")})  

merge_columndf2 = pd.DataFrame({"rkey": ["a", "b", "d"],
                                "data2": pd.Series(range(3), dtype="Int64")})

#内连接：how='inner'
pd.merge(merge_columndf1, merge_columndf2, left_on = 'lkey', right_on = 'rkey', how = 'inner')

#左连接：how='left'
pd.merge(merge_columndf1, merge_columndf2, left_on = 'lkey', right_on = 'rkey', how = 'left')



3、根据多个键列进行连接：通过设置pd.merge()方法中的on = ['key1', 'key2']或者left_on = ['lkey1', 'lkey2'], right_on = ['rkey1', 'rkey2']
left = pd.DataFrame({"lkey1": ["foo", "foo", "bar"],
                     "lkey2": ["one", "two", "one"],
                     "lval": pd.Series([1, 2, 3], dtype='Int64')})

right = pd.DataFrame({"rkey1": ["foo", "foo", "bar", "bar"],
                      "rkey2": ["one", "one", "one", "two"],
                      "rval": pd.Series([4, 5, 6, 7], dtype='Int64')})

#左连接：how='left'
pd.merge(left, right, left_on = ['lkey1', 'lkey2'], right_on = ['rkey1', 'rkey2'], how='left')



4、如果两个进行连接的数据集，存在以索引列作为键列的情况，则可以通过设置right_index = True或者left_index = True来代替left_on和right_on
left1 = pd.DataFrame({"key": ["a", "b", "a", "a", "b", "c"],
                      "value": pd.Series(range(6), dtype="Int64")})

right1 = pd.DataFrame({"group_val": [3.5, 7]}, index=["a", "b"])

#左连接
pd.merge(left1, right1, left_on = 'key', right_index=True, how='inner')



4、对具有多级索引的数据集进行合并：方法同非多级索引数据集一致
left_nonhierarchical_frame = pd.DataFrame({"key1": ["Ohio", "Ohio", "Ohio","Nevada", "Nevada"],
                                  "key2": [2000, 2001, 2002, 2001, 2002],
                                  "data": pd.Series(range(5), dtype="Int64")})

right_hierarchical_index = pd.MultiIndex.from_arrays([["Nevada", "Nevada", "Ohio", "Ohio", "Ohio", "Ohio"],
[2001, 2000, 2000, 2000, 2001, 2002]])

right_hierarchical_frame = pd.DataFrame({"event1": pd.Series([0, 2, 4, 6, 8, 10], dtype="Int64", index=right_hierarchical_index),
                      "event2": pd.Series([1, 3, 5, 7, 9, 11], dtype="Int64", index=right_hierarchical_index)})

#外连接
pd.merge(left_nonhierarchical_frame, right_hierarchical_frame, left_on=['key1', 'key2'], right_index=True, how='outer')

#左连接
pd.merge(left_nonhierarchical_frame, right_hierarchical_frame,
        left_on=['key1', 'key2'], right_index=True, how='left')



5、对于具有相同索引，而不存在相同列值的数据集，可以直接对数据集调用join()方法, join()方法还可以同时对多个数据集进行合并
#该方法默认为左连接，即将被调用的数据集左连接到调用的数据集中
#该方法默认的连接键为两个数据集的索引,即使2个数据集的索引不存在相同的值，也可以进行连接
dj_lframe = pd.DataFrame({'key1': [1, 2, 3, 4, 5], 'key2': ['one', 'two', 'three', 'four', 'five']},
                        index=['a', 'b', 'c', 'd', 'e'])
dj_rframe = pd.DataFrame({'key3': [1, 2, 5, 3, 5], 'key4': ['one', 'six', 'three', 'seven', 'five']},
                        index=['f', 'b', 'm', 'd', 'e'])

#如不指定how参数到值，则默认为将数据集dj_rframe左连接至dj_lframe中, 且默认的连接键均为2个数据集的索引
dj_lframe.join(dj_rframe, how='outer')


#也可以通过on参数来指定调用join方法的对象用来匹配的列，但被调用的数据匹配列只能为索引
left1 = pd.DataFrame({"key": ["a", "b", "a", "a", "b", "c"],
                      "value": pd.Series(range(6), dtype="Int64")})
right1 = pd.DataFrame({"group_val": [3.5, 7]}, index=["a", "b"])

left1.join(right1, on='key', how='outer')


#使用join方法同时对三个数据集进行合并
left2 = pd.DataFrame([[1., 2.], [3., 4.], [5., 6.]],
                     index=["a", "c", "e"],
                     columns=["Ohio", "Nevada"]).astype("Int64")

right2 = pd.DataFrame([[7., 8.], [9., 10.], [11., 12.], [13, 14]],
                      index=["b", "c", "d", "e"],
                      columns=["Missouri", "Alabama"]).astype("Int64")

another = pd.DataFrame([[7., 8.], [9., 10.], [11., 12.], [16., 17.]],
                       index=["a", "c", "e", "f"],
                       columns=["New York", "Oregon"])

left2.join([right2, another])



6、通过numpy中的concatenate方法，根据指定轴的方向，合并2个或多个数组。注意，需要合并的数组需要以元组的形式作为参数传入
arr1 = np.array([[1, 2], [3, 4]])
arr2 = np.array([[5, 6]])

#横向合并
np.concatenate((arr1, arr2), axis=1)

#纵向合并
np.concatenate((arr1, arr2), axis=0)



7、通过concat方法，可以将数据集（一般是Series或者DataFrame）在横轴方向或者纵轴方向进行简单的堆叠，而不需要根据指定的索引或者列进行匹配。
s1 = pd.Series([0, 1, 3, 4], index=["a", "b", "c", "e"], dtype="Int64")
s2 = pd.Series([2, 3, 4], index=["a", "d", "e"], dtype="Int64")
s3 = pd.Series([3, 4, 5, 6], index=["d", "e", "f", "g"], dtype="Int64")

#横向堆叠，索引值会去重
pd.concat([s1, s2, s3], axis=1)

#纵向堆叠, 索引值不会去重
pd.concat([s1, s2, s3], axis=0)

#纵向堆叠时，还可以设置参数join='inner'
pd.concat([s1, s2, s3], axis="columns", join='inner')



#无论是横向堆叠还是纵向堆叠，均可以通过concat()方法中的key参数，对合并的结果中，各数据集块进行标记
pd.concat([s1, s2, s3], keys=['one', 'two', 'three'], axis=0) #纵向
pd.concat([s1, s2, s3], keys=['one', 'two', 'three'], axis=1) #横向



#进行纵向合并时，如果给给数据分区设定了区域标签，则会使得输出结果具有二级索引，可以通过unstack()方法，默认将最内层的索引解构成列
#此时最内层行索引会被转变成列，只会保留最外层索引
pd.concat([s1, s2, s3], keys=['one', 'two', 'three'], axis=0).unstack()



#对DataFrame数据集之间使用concat()方法进行堆叠时，在对分区命名时，有2种方法，一种方法为传统的keys参数命名，另一种方法为通过字典的方式进行命名
pd.concat((concat_df1, concat_df2), keys=['one', 'two'], axis=0) #keys参数方式
pd.concat({'one': concat_df1, 'two': concat_df2}, axis=1) #字典方式



#还可以通过concat()方法中的names参数，对各数据区域标签（即最外层索引）进行命名
pd.concat({'one': concat_df1, 'two': concat_df2}, axis=1, names=['upper', 'lower']) #横向合并后，对最外层索引进行命名
pd.concat({'one': concat_df1, 'two': concat_df2}, axis=0, names=['upper', 'lower']) #纵向合并后，对最外层索引进行命名



#通过设置concat()方法中的ignore_index=True，还可以使得输出的合并结果中，索引重置为整数索引

#横向合并时，会重置列索引
pd.concat((concat_df1, concat_df2), axis=1, ignore_index=True)

#纵向合并时，会重置行索引
pd.concat((concat_df1, concat_df2), axis=0, ignore_index=True)



8、通过对数据集调用combine_first()方法，可以用另外一个数据集的值去填补该数据集的空值
concat_first_df1 = pd.DataFrame({"a": [1., np.nan, 5., np.nan],
                                 "b": [np.nan, 2., np.nan, 6.],
                                 "c": range(2, 18, 4)})

concat_first_df2 = pd.DataFrame({"a": [5., 4., np.nan, 3., 7.],
                                 "b": [np.nan, 3., 4., 6., 8.]})

#用数据集concat_first_df2去填补数据集concat_first_df1的空值
concat_first_df1.combine_first(concat_first_df2)

#用数据集concat_first_df1去填补数据集concat_first_df2的空值
concat_first_df2.combine_first(concat_first_df1)






