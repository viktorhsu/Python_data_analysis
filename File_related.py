1、通过Python内置的with open()方法，打开同辈目录下的文件
打开同辈目录下的文件：open('文件名')来打开文件内容，打开后返回一个对象，该对象需要被存储在一个变量中。最后使用read()函数来读取文件中的内容。由于read()读取到文件中最后一行时，会返回一个空行。所以读取到结果会包含空行。如果需要去除最后的空行，可以使用r.strip()函数。with语句会在打开文件后自动关闭文件。如果不用with语句来打开文件，则需要在打开文件后使用close()函数来关闭文件。file_name.close()。

with open('pi_digits.txt', 'r') as file_object:
    contents = file_object.read()
    print(contents)

#"r"：只读模式 (read)，用于读取文件内容。如果文件不存在，会引发错误。
#"w"：写入模式 (write)，用于创建新文件或覆盖已存在的文件。如果文件已存在，它会被清空。如果文件不存在，会创建新文件。
#"a"：追加模式 (append)，用于在文件末尾追加新内容，而不会覆盖原有内容。如果文件不存在，会创建新文件。
#"x"：排它性创建模式 (exclusive creation)，用于创建新文件，如果文件已存在则会引发错误。
#"b"：二进制模式 (binary)，用于处理二进制文件，如图像、音频、视频文件。以字节的形式读取或写入文件，不进行字符编码。
#"t"：文本模式 (text)，用于处理文本文件（默认模式）。以字符的形式读取或写入文件，可以指定字符编码。
#组合的模式：'rb' 和 'rt'等



2、通过Python内置的with open()方法，打开隔代目录下的文件：在open中使用相对文件路径（从与此程序文件相同的部位开始)
with open('text_files/file_name') as file_object:
其中，text_files与程序文件所在位置相同。
注意：Windows系统中，使用 \ 而不是 /.



3、通过Python内置的with open()方法，打开远亲目录下的文件，只能使用绝对文件路径。由于绝对文件路径一般较长，所以可以先将其存储在一个变量中。
file_path = '/Users/victor/Documents/Anaconda/anaconda3/lib/python3.11/site-packages/pandas/_testing/_random.py'

with open('file_path') as file_object:



4、通过Pandas中的read_csv()方法，打开csv文件
如果数据是以逗号分隔的，建议用pandas.read_csv
原数据：
a,b,c,d,message
1,2,3,4,hello
5,6,7,8,world
9,10,11,12,foo

df = pd.read_csv("examples/ex1.csv")





  


