#1. 捕获多个异常，但不能区分

try:
    open("asd","r")
except (NameError, FileNotFoundError) as e:
    print("有异常，异常为:" , e)


#2. 捕获多个异常 能区分
try:
    1 / 0
except (FileNotFoundError) as e:
    print("文件没找到")
except ZeroDivisionError as e:
    print("除0异常")

#3. 捕获全部异常  有问题就捕获
try:
    1/0
except Exception as e:
    print("Error")


#4. 异常的 else 语法

try:
    1/0
except Exception as e:
    print("Error")
else:    #（可选）
    print("Success")

finally:  #（可选） 关闭xx 释放xx  起收尾的作用
    print("有没有问题，我都执行")