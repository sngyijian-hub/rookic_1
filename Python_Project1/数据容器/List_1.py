#list 列表 []
name = ["Uzi","Faker","Zeus"]
print(name[0])
print(name[-1])
#嵌套列表
name_index = [[1,2,3],
              [4,5,6],
              [7,8,9]]
print(name_index[0][0])

#常用操作

list1 = [1,2,3,4,5,6,7,8,9]
for i in list1:
    print(f"{i} ",end="\t")
print()
index = 0
while index < len(list1):
    print(f"{list1[index]} ",end="\t")
    index += 1
print()

# list.append(10)

#案例
num1 = [1,2,3,4,5,6,7,8,9]
num2 = []

for num in num1:
    if num % 2 ==0:
        num2.append(num)
print(num2)
