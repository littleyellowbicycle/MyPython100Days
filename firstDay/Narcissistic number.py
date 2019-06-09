'''
水仙花数是指一个 3 位数，它的每个位上的数字的 3次幂之和等于它本身
'''


def find():
    rge = int(input('请输入范围: '))
    res = list()
    for item in range(rge + 1):
        temp = item
        sum = 0
        while (1):
            it = item % 10
            sum += it * it * it

            item = int(item / 10)  #????
            if (temp == 153):
                print(item)
            if item < 1:
                if sum == temp:
                    res.append(temp)
                print(item)
                if temp == 153:
                    print('sum is %d' % sum)
                break

    nostr = 'there is no num in range %d'
    exstr = 'these num is:'
    if len(res) == 0:
        print(nostr % (rge))
    else:
        print(exstr)
        print(res)


if __name__ == "__main__":
    find()