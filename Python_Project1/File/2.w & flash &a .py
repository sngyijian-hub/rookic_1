"""
mode:
- r 只读
- w 写入
    -若文件不存在，则创建；若有文件内容，则清空后写入
- a 追加
    -文件不存在，则创建，若文件存在，则在原内容后追加
flush: 将缓存内容写到硬盘
    -不用它运行更快   用它数据更安全
"""
f = open("C://songyj6//it_2_new.txt","w",encoding = "UTF-8")
# C:\\songyj6\\stu_info\\stu.txt
#w 1
# 将helloworld写入文件
# write函数表示 将内容写入到缓冲区
f.write("哈哈哈")

# 将缓存内容写到硬盘
# close() 之前会自动 flush()
f.flush()

f.close()

##理解flush的实例
import time
s = time.time()
f = open("C://songyj6//it_3.txt", "w",encoding="utf-8")

for i in range(10000):
    f.write(str(i) + "\n")
    f.flush()
print(s)
f.close()

## a
f = open("C://songyj6//it_3_new.txt","a",encoding = "UTF-8")
f.write("啦啦啦")
f.write("\n嘎嘎嘎")
