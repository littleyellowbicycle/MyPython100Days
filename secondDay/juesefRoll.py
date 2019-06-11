def main():
    persons = [True] * 30
    count = 0
    index = 0
    num = 0
    while count < 15:
        if persons[index]:
            num += 1
            if num == 9:
                persons[index] = False
                count += 1
                num = 0
                #print('flag', end=' ')
        index += 1
        index = index % 30
    for person in persons:
        print('欧皇' if person else '非酋', end=' ')
    pass


if __name__ == "__main__":
    main()
    pass