1、插入缺失值：直接通过Python内部的None或者numpy.nan插入缺失值, 对于多维数据，也可以通过切片的方式批量插入
  #插入的缺失值均不会更改原数据
  miss_series = pd.Series([1, 2.0, 3, None, 4.5, np.nan, 8.8])
  #Series()方法首字母必须大写，None首字母也必须为大写

  #多维数据可以通过批量的方式插入空值
  df.iloc[:4, 1] = np.nan

  
  
2、判断缺失值：直接调用Python内部isna()方法和notna()方法，判断数据是否为缺失值
  miss_series.isna()
  #返回一个布尔值
  #这两种方法还可以对Series类型数据进行筛选，但是却不可以对DataFrame类型数据进行筛选



3、删除缺失值：直接调用Pthon内部dropna()方法
  miss_series.dropna()
  #输出结果默认会删除含有缺失值的行，但是新输出的无空值的数据索引还是原来的索引，不会自动生成新的连续的索引，此外，默认原数据也不会被改变。

  #可以通过设置how参数的值，使得仅过滤掉每列数据均为空值的行。
  miss_dataframe = pd.DataFrame([[1.3, 5.2, '吃饭'], [np.nan, None, np.nan], [None, 4.2, 5.4]])
  miss_dataframe.dropna(how = 'all')
  #注意，DataFrame()方法调用必须对特定的字母大写
  #注意，DataFrame()方法应该接受一个二维数组或者一个字典作为参数

  #可以通过设置thresh参数，来指定每行或者每列含有多少个空值后即可被过滤掉
  miss_dataframe.dropna(thresh = 2)

  #可以通过设置axis参数的值，来指定删除行或者列，默认为删除行
  miss_dataframe.dropna(how = 'all', axis = 'columns')


4、填补缺失值：直接调用Python内置的fillna()方法，该方法不会更改原数据，而是创建一个新的数据。
  #对所有空值填充常数
  miss_dataframe.fillna(0)

  #按照列的索引，对不同列的空值填充不同的值, 目前只可以对列进行该操作
  miss_dataframe.fillna({0: 'nann', 1: 999, 2: '睡觉'})

  #通过设置fillna()方法中methon参数为ffill或者bfill，以此可以设定填充值是根据前面的非空值来填充，或者是根据后面的非空填充值来填充。
  #可以通过设置limit参数的值，来设定每个值可以作为填充值的次数
  #通过设置axis=0 或者 axis=1 可以设定是按照横跨横轴或是纵轴的方向进行填充
  miss_data2 = pd.DataFrame(np.random.standard_normal((6,4))).round(2)
  miss_data2.iloc[1:4, 2:4] = np.nan
  miss_data2.iloc[2:4,0:3] = np.nan
  miss_data2.fillna(method = 'ffill', limit = 2, axis=1)

  #可以通过传入数据的mean, median等数据作为fillna()的参数进行填充,目前只能进行列方向上的
    miss_data2.fillna(miss_data2.median())

    

  
  

  

  



  








  
