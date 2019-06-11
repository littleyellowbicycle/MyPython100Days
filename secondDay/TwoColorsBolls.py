from random import randrange, randint, sample


def display(balls):
    '''
    for index, ball in enumerate(balls):
        if index == len(balls) - 1:
            print('|', end='\n')
        print('%2d' % ball, end=' ')
    '''
    for index in range(len(balls)):
        if index == len(balls) - 1:
            print("|")
        print('%2d' % balls[index], end=' ')
    pass


def random_select():
    red = [x for x in range(1, 33)]
    balls = []
    balls = sample(red, 6)
    blue = [x for x in range(1, 17)]
    balls.append(blue[randint(0, 15)])
    return balls
    pass


if __name__ == "__main__":
    n = int(input("请输入投注数: "))
    for i in range(n):
        display(random_select())
    pass
