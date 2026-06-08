  ---
  从零理解装饰器

  第 0 层：函数就是变量

  def greet():
      print("hello")

  # 函数可以赋值给另一个变量
  f = greet        # 注意：没有括号！不是调用，是"把函数本身赋值"
  f()              # 输出 hello —— 和 greet() 一样

  Python 里函数是"一等公民"——可以当参数传、可以赋值、可以返回。这是理解装饰器的唯一前提。

  ---
  第 1 层：函数里套函数

  def outer():
      print("外层开始")
      def inner():          # 在函数里面定义函数
          print("内层")
      print("外层结束")
      return inner          # 返回内层函数本身

  f = outer()    # 打印: 外层开始 → 外层结束
  f()            # 打印: 内层

  outer() 执行完返回了 inner 这个函数，你可以之后调用它。这就是闭包。

  ---
  第 2 层：给函数"包一层"，不改原函数

  def add(a, b):
      return a + b

  # 我想在不改 add 源码的情况下，让它自动打印日志
  def log_wrapper(fn):         # 接收一个函数
      def new_fn(a, b):        # 造一个新函数
          print(f"调用前: 参数={a},{b}")
          result = fn(a, b)    # 调用原函数
          print(f"调用后: 结果={result}")
          return result
      return new_fn            # 返回新函数

  add = log_wrapper(add)       # 用包装版替换原来的 add
  add(3, 5)
  # 调用前: 参数=3,5
  # 调用后: 结果=8

  这就是装饰器的本质：一个函数，吃进原函数，吐出增强版函数。

  ---
  第 3 层：@ 语法糖

  上面那句 add = log_wrapper(add) 太啰嗦了，Python 给了简写：

  @log_wrapper
  def add(a, b):
      return a + b

  # ↑ 等价于 add = log_wrapper(add)

  @ 就是你写 add = log_wrapper(add) 的快捷方式，仅此而已。

  ---
  第 4 层：*args, **kwargs 是什么

  问题来了：如果函数参数不固定怎么办？有的函数2个参数，有的3个，有的没有？

  # *args    → 把所有位置参数收成一个元组
  # **kwargs → 把所有关键字参数收成一个字典

  def catch_all(*args, **kwargs):
      print("位置参数:", args)
      print("关键字参数:", kwargs)

  catch_all(1, 2, name="张三", age=20)
  # 位置参数: (1, 2)
  # 关键字参数: {'name': '张三', 'age': 20}

  问题来了：如果函数参数不固定怎么办？有的函数2个参数，有的3个，有的没有？

  # *args    → 把所有位置参数收成一个元组
  # **kwargs → 把所有关键字参数收成一个字典

  def catch_all(*args, **kwargs):
      print("位置参数:", args)
      print("关键字参数:", kwargs)

  catch_all(1, 2, name="张三", age=20)
  # 位置参数: (1, 2)
  # 关键字参数: {'name': '张三', 'age': 20}

  所以 wrapper(*args, **kwargs) 的意思是：不管原函数要什么参数，原样传给它。

  ---
  回到计时装饰器，现在再看

  import time

  def timer(func):                           # ① 吃进原函数
      def wrapper(*args, **kwargs):          # ② 造新函数，参数原样转发
          start = time.time()                # ③ 开始计时
          result = func(*args, **kwargs)     # ④ 调用原函数
          cost = time.time() - start         # ⑤ 结束计时
          print(f"{func.__name__} 耗时: {cost:.4f}秒")
          return result                      # ⑥ 返回原函数的结果
      return wrapper                         # ⑦ 返回这个新函数

  @timer                                     # 等价于 sum_to_n = timer(sum_to_n)
  def sum_to_n(n):
      return sum(range(1, n + 1))

  执行流程：sum_to_n(100) → 实际是 wrapper(100) → start = now → 调真正的 sum_to_n(100) → cost = now - start → 打印耗时 →
  返回结果。
