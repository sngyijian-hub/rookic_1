def func01():
    print("01的开始")
    a = 1/0
    print("01的结束")

def func02():
    print("02的开始")
    func01()
    print("02的结束")

def main():
    try:
        func02()
    except Exception as e:
        print(e)


main()