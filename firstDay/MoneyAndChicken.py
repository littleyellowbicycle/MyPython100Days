def func():
    male = 5
    famale = 3
    kid = 1 / 3
    count = 100
    cast = 100
    res = list()
    for m in range(21):
        for f in range(int((100 - m * 5) / 3)):
            k = (100 - m * 5 - f * 3) * 3
            if 100 == (k + f + m):
                temp = [m, f, k]
                res.append(temp)
    print(res)
    pass


if __name__ == "__main__":
    func()
    pass