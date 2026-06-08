# ====== Day1 Python固基 ======

# ---------- 练习1: 列表推导式 ----------
def list_comprehension():
    result = [i ** 2 for i in range(1, 21) if i % 3 == 0]
    print("1~20能被3整除的平方:", result)


# ---------- 练习2: 计时装饰器 ----------

import time
def timer(func):
    """ 装饰器：打印函数运行时间"""
    def wrapper(*args,**kwargs):
        start = time.time()
        result = func(*args,**kwargs)
        end = time.time()
        cost_time = end - start
        print(f"{func.__name__}cost_time:{cost_time:.8f}s")
        return result
    return wrapper

@timer
def sum_to_n(n):
    return sum(range(1,n+1))
print(sum_to_n(100000))
    # ---------练习3: 重试装饰器 ----------
def retry(max_attempt=3,delay=1):
    def wrapper1(fn):
        def wrapper2(*args,**kwargs):
            for i in range(1,max_attempt+1):
                try:
                    result = fn(*args,**kwargs)
                    return result
                except Exception as error:
                    print(f"第{i}次失败，原因：{error}")
                    if i ==max_attempt:
                        raise
                    time.sleep(delay)

        return wrapper2
    return wrapper1



# ---------- 运行所有练习 ----------
# if __name__ =="__main__":
#     @timer
#     def sum_to_n(n):
#         return sum(range(1, n + 1))
#     @retry
#     def sum_to_n(n):
#         return sum(range(1, n + 1))



#生成器I： 一行一行读
def read_line(filename):
    with open(filename,'r',encoding='utf-8') as file:
        for line in file:
            yield line.strip()


#生成器II: 读带 [ERROR] 的
def filter_errors(lines):
    for line in lines:
        if '[ERROR]' in line:
            yield line



#主函数
@timer
def filter_log(filename):

    readline = read_line(filename)
    errorline = filter_errors(readline)

    for line in errorline:
        print(line)
if __name__=="__main__":
    filter_log('app.log')