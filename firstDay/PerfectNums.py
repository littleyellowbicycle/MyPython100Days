'''
如果一个数恰好等于它的非自身因子之和，则称该数为“完全数”
'''


def FindPerfectNum():
    rge = int(input("请输入范围"))
    res = list()
    for item in range(rge + 1):
        sum = 0
        for it in range(1, item):
            if (item % it) == 0:
                sum += it
        if sum == item:
            res.append(item)
    print(res)
    pass


if __name__ == "__main__":
    FindPerfectNum()
    pass