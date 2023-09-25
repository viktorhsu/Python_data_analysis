1、根据指定的条件，检测异常值
out_data = pd.DataFrame(np.random.standard_normal((1000,4)))

#先通过describe()方法，获取数据的基本信息，从而便于规定异常值的标准
out_data.describe()

#根据数据的基本描述信息，对out_data的所有数据，设定abs()>3的即为异常值
#直接调用abs()方法，返回的是一个布尔数组
out_data.abs()>3

#筛选出out_data中所有存在abs()>3的行
out_data[(out_data.abs()>3).any(axis='columns')]

#也可以只根据特定的列，筛选出特定列存在异常值的行
out_columns = out_data[2]
out_columns[(out_columns.abs()>3)]




2、对符合条件的值进行特定的操作：通常通过numpy中的sign()方法，根据数值的正负号，将数值转换成1或者-1
out_data[(out_data.abs()>3)] = np.sign(out_data)*3

#再次查看数据的基本描述信息，以判断是否对异常值处理成功
out_data.describe()




