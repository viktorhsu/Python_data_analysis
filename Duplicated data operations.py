1、判断是否为重复值：直接调用pandas中的duplicated()方法, 只能判断是否为重复的行，返回一个布尔值序列
  #默认为当所有列均相同时，该行才重复，但也可以通过subset=['column1', 'column2']的方式，表示当column1和column2都重复时，才判断为重复行
  dup_data = pd.DataFrame({'k1': ["one", "two"] * 3 + ["two"], 'k2': [1, 1, 2, 3, 3, 4, 4]})
  dup_data['v'] =range(7)
  dup_data.duplicated()
  dup_data.duplicated(subset = ['k1', 'k2'])


  
2、删除重复的行：直接调用drop_duplicates()方法，默认为保留第一次出现的行，但也可以通过设置keep = 'last'保留最后一次出现的行
  #默认为每列数据都一样才为重复行
  dup_data.drop_duplicates(keep = 'last')
  #也可以给drop_duplicates传入subset参数，指定判断为重复值的标准
  dup_data.drop_duplicates(subset = ['k1'], keep = 'last')
  
  
