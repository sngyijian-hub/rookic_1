"""
只有文本文件才能 r w a
b:二进制处理
rb: 二进制读
wb：二进制写

"""
#实例:  将C盘的图片复制到D盘
fr = open("C://songyj6//LOL铂金.png","rb")
fw = open("C://songyj6//rang//LOL铂金.png","wb")


fw.write(fr.read())

fr.close()
fw.close()


