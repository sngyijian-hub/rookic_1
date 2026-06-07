
"""
strip() 去掉首尾的换行符、多余空格
split() 按( )把一行拆成单词列表   默认是空格 也可以是其他任意的字符
二者连用 f.strip()split()  文本拆成一个个单词
for line in f:  遍历文件的每一行
open(): 建立 Python 程序和磁盘上文件之间的 “连接通道”，
        并 打开 / 创建文件，并返回一个「文件对象」。
readline()  str 适合：超大文件逐行处理、只需要前几行
readlines() list 适合：小文件快速全量读取、需要按行索引访问
"""



#方式1    最推荐

f = open("C://wxq.txt","r",encoding = "UTF-8")

for line in f:
    print(line.strip())    #去除尾部的 换行和空格

f.close()

#方式2
for line in open("C://wxq.txt","r",encoding = "UTF-8"):
    print(line.strip())

#方法3
#with open() as f: 语法    文件会自动关闭-->自动调用close
# with open("C://wxq.txt","r")as f:
    # f.readlines()


#实例
count = 0
f = open("C://songyj6//it_1.txt","r",encoding = "UTF-8")
for line in f:
    word_line = line.strip().split()
    for word in word_line:
        if word == "it":
            count += 1
print(f"it 出现的次数为:{count}次")

f.close()


