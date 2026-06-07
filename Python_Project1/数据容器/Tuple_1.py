#Tuple元组  不能被修改-append()
#字面量
t1 = (1,3,5,"heima")
print(t1,"类型:",type(t1))

t2 = (1)      #一个元素 要写 逗号，  否则不是元组
t3 = (2,)
print(type(t2))
print(type(t3))

#嵌套
t4=((1,2,3),
    (4,5,6),
    (7,8,9))
print(t4[0][0])

print(t1.index(1))

t5 = (1,2,[3,4,5])

