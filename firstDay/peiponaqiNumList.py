'''
斐波那契数列（Fibonacci sequence），又称黄金分割数列
'''


def MakeNumList():
    res = [1, 1]
    Range = int(input("请输入数列个数: "))
    if Range >= 3:
        for item in range(3, Range + 1):
            res.append(res[item - 2] + res[item - 3])
    print(res)
    pass


if __name__ == "__main__":
    MakeNumList()
    pass