1、通过index参数和columns参数可以给DataFrame数据进行索引命名。
  #index_data = pd.DataFrame(np.arange(12).reshape((3, 4)),
                          index = ["Ohio", "Colorado", "New York"],
                          columns = ['one', 'two', 'three', 'four'])



2、通过map()方法，可以给map()方法传入一个自定义的函数，从而以向量化的方式对数据的索引进行更改
  #自定义一个重命名索引的函数transform
  def transform(x):
    return x[:10].upper()
  #对数据的行索引和列索引均进行索引重命名的向量化操作，并且将变换后的索引赋值给原索引
  #此方法为更改原数据的索引
  index_data.index = index_data.index.map(transform)
  index_data.columns = index_data.columns.map(transform)



3、通过rename方法可以对数据的原索引进行重命名，而不更改原数据的索引

  #在rename方法中，传入调用字符串属性的方法
  #title属性为使字符的首字母大写，其余字母为小写
  index_data.rename(index = str.title, columns = str.upper)

  #以字典的方式，传入对index索引和column索引进行的更改规则
  index_data.rename(index = {'COLORADO': 'RICE'}, columns = {'THREE': '3'})
