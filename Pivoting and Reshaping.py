1、通过stack()方法对数据集的索引进行操作，将Wide数据转换成Long数据。同unstack()方法一样，只作用于索引。
#即将一行具有多列值的数据，转换成一行只有一列值
#默认为将最内层的列索引名（即level=-1),转换成最内层的行索引
#默认为dropna=True,即将转换后包含空值的行删除
stack_data1 = pd.DataFrame(np.arange(6).reshape((2, 3)),
                             index=pd.Index(["Ohio", "Colorado"], name="state"),
                             columns=pd.Index(["one", "two", "three"],
                                              name="number"))
stack_data1.stack()



2、通过unstack()方法，可以将Long数据，转换成Wide数据.注意unstack()方法和pivot()方法最本质的区别，unstack()方法只作用于索引
#默认为将最内层的行索引，转换成最内层的列索引，即level=-1
#默认为dropna=True
stack_data1.stack().unstack()



3、通过pivot()方法，对数据集进行透视，即类似于将Long数据转换成Wide数据。相当于先对数据进行set_index()操作，再进行unstack()操作
data2 = {
    'date': ['1959-01-01', '1959-01-01', '1959-01-01', '1959-04-01', '1959-04-01',
             '1959-04-01', '1959-07-01', '1959-07-01', '1959-07-01', '1959-10-01'],
    'item': ['realgdp', 'infl', 'unemp', 'realgdp', 'infl', 'unemp',
             'realgdp', 'infl', 'unemp', 'realgdp'],
    'value': [2710.349, 0.0, 5.8, 2778.801, 2.34, 5.1, 2775.488, 2.74, 5.3, 2785.204],
    'value2': [0.802926, 0.575721, 1.381918, 0.000992, -0.143492, -0.206282,
               -0.222392, -1.682403, 1.811659, -0.351305]
}

pivot_data2 = pd.DataFrame(data2)
pivot_data2

pivot_data2.pivot(index='date', columns='item')



4、通过pandas.melt方法，执行pivot方法的逆操作，即将多列转换成一列（将Wide数据转换成Long数据）
#与stack方法类似的地方在于，均为将宽数据转换成长数据，但是melt方法为对数据列进行操作，而stack方法为对索引进行操作
#value_vars参数默认为去除id_vars以外的变量。
#注意value_vars=['A', 'B', 'C']和value_vars=['A', 'B']输出结果的区别
melt_df.melt(id_vars = 'key', value_vars=['A', 'B', 'C'], var_name= 'ABC', value_name= 'score')
或
pd.melt(melt_df, id_vars = 'key', value_vars=['A', 'B', 'C'], var_name= 'ABC', value_name= 'score')







