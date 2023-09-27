1、自定义分割区间, 不均等配额分割：通过pd.cut()方法，可以将数据按照自定义的分割区间进行分类。
  #可以完全自定义每个分割区间的柱子，也可以直接定义分割区间的数量，则可以自动按照最大值和最小值来进行等值分割
  bin_data = [20, 22, 25, 27, 21, 23, 37, 31, 61, 45, 41, 32]
  bins = [18, 25, 35, 60, 100]
  bin_data_categories = pd.cut(ages, bins)
  或
  bin_data_categories = pd.cut(ages, 4)

  #可以通过pd.cut()方法中的precision参数，设置每个分割柱的小数位数
  bin_data_categories = pd.cut(ages, 4, precision=2)

  #通过codes属性，可以对每个分割区间进行数字编号，并且将每个值以分类编号的方式标记
  bin_data_categories.codes

  #通过调用categories属性，或者对其引用数字索引，可以获取以数字编号表示的指定的分割区间
  bin_data_categories.categories[1]

  #pd.value_counts可以对列表中的每个元素去重统计每个元素出现的个数，故可以以此统计每个分割区间出现的次数，即包含元素的个数
  pd.value_counts(bin_data_categories)

  #可以通过设置pd.cut()方法中 right=False或者right=True来控制分割区间的左右闭合情况
  pd.cut(bin_data, bins, right=False)

  #可以通过设置方法pd.cut()中的labels参数，来给每个分割区间重命名
  group_names = ['Youth', 'YoungAdult', 'MiddleAged', 'Senior']
  pd.cut(bin_data, bins, right=False, labels=group_names)




2、均等配额分割：通过pd.qcut()方法，即可实现配额分割，即每个分割区间内含有的样本数均相同
bin_qdata = np.random.standard_normal(1000)
bin_qdata_categories = pd.qcut(bin_qdata, 5, precision=2)
pd.value_counts(bin_qdate_categories) #验证每个分割区间的样本数是否相同




  
  
