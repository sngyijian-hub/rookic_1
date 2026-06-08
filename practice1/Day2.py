# ====== Day2 ======

# ---------- 练习1: 迭代器 ----------
class CountDown:
    def __init__(self,start):
        self.current = start

    def __iter__(self):
        return self
    def __next__(self):
        if self.current < 0:
            raise StopIteration
        result = self.current

        self.current = result - 1

        return result
# ---------- 练习2: 生成器 ----------
def countdown(start):
    while start >= 0:
        yield start
        start -= 1

def fibonacci(n):
    a,b=1,1
    for i in range(n):
        yield a
        a,b=b,a+b

for num in fibonacci(8):
    print(num,end=' ')

# ---------- 练习3:  ----------



