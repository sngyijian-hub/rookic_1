"""
备份
数据的清洗和过滤
.bak :备份文件
    -建议 读一行写一行

"""
fr = open("C://songyj6//it_4.txt","r",encoding="utf-8")
fw = open("C://songyj6//it_4.txt.bak","w",encoding="utf-8")
print()
# fw.write(fr.read())
for line in fr.readlines():
    line = line.strip() #去除 \n 和 前后多余空格
    # print(line.split(",")[3])
    if "no" == line.split(",")[3]:
        continue

    fw.write(f"{line}\n")
    # fw.write("\n")



fr.close()
fw.close()