"""
贪婪法：在对问题求解时，总是做出在当前看来是最好的选择，不追求最优解，快速找到满意解。
输入：
20 6
电脑 200 20
收音机 20 4
钟 175 10
花瓶 50 2
书 10 1
油画 90 9
"""

import codecs

class Thing(object):
    """物品"""

    def __init__(self, name, price, weight):
        self.name = name
        self.weight = weight
        self.price = price

    @property
    def value(self):
        return self.price / self.weight


def input_thing():
    name_str, price_str, weight_str = input("name price weight:").split()
    return name_str, int(price_str), int(weight_str)
    pass

def input_file():
    str_list=[]
    with codecs.open('./thingslist.txt','r',encoding='utf-8') as f:
        str_list=f.read().splitlines()
    return str_list

def input_str(string):
    name,price,weight=string.split()
    print(name+price+weight)
    return name,int(price),int(weight) 

def main():
    max_weight, num_of_things = map(int, input("total_weight num_things").split())
    all_things = []
    #for _ in range(num_of_things):
    #    all_things.append(Thing(*input_thing()))

    for   string in input_file():
        all_things.append(Thing(*input_str(string) ))

    all_things.sort(key=lambda x: x.value, reverse=True)
    print(all_things)
    total_weight = 0
    total_price = 0
    for thing in all_things:
        if total_weight < max_weight - thing.weight:
            total_weight += thing.weight
            total_price += thing.price
            print(f'thelf take {thing. name}')
    print(f'total price:{total_price}$')


if __name__ == "__main__":
    main()
    pass
