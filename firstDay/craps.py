'''
'''
from random import randint


def throw():
    return randint(1, 6) + randint(1, 6)
    pass


def game():
    sum = throw()
    record = 0
    if sum == 7 or 11:
        return True
    elif sum == 2 or 3 or 12:
        return False
    else:
        record = sum
    while (1):
        sum = throw()
        if sum == record:
            return True
        if sum == 7:
            return False
    pass


if __name__ == "__main__":
    for x in range(50):
        if game():
            print('player win')
        else:
            print('player lose')
    pass