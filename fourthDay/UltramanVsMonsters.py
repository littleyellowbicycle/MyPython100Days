from abc import abstractmethod, ABCMeta
from random import randint, randrange

#define base class fighter


class fighter(object):
    def __init__(self, name, hp):
        self._name = name
        self._hp = hp
        pass

    @property
    def name(self):
        return self._name

    @property
    def hp(self):
        return self._hp

    @hp.setter
    def hp(self, hp):
        self._hp = hp if hp >= 0 else 0

    @property
    def alive(self):
        return self._hp > 0

    @abstractmethod
    def attack(self, other):
        pass

    pass


#define Ultraman
class Ultraman(fighter):
    def __init__(self, name, hp, mp):
        super().__init__(name, hp)
        self._mp = mp
        pass

    @property
    def mp(self):
        return self._mp

    @mp.setter
    def mp(self, mp):
        self._mp = mp if mp >= 0 else 0

    #define attack,magic_attack,huge_attack
    def attack(self, other):
        other._hp -= randint(10, 25)

    def huge_attack(self, other):
        """
        究极必杀技(打掉对方至少50点或四分之三的血)
        :param other: 被攻击的对象
        :return: 使用成功返回True否则返回False
        """
        if self._mp >= 50:
            self._mp -= 50
            injury = other.hp * 3 // 4
            injury = injury if injury >= 50 else 50
            other.hp -= injury
            return True
        else:
            self.attack(other)
            return False
        pass

    def magic_attack(self, others):
        """
        魔法攻击
        :param others: 被攻击的群体
        :return: 使用魔法成功返回True否则返回False
        """
        if self._mp >= 20:
            self._mp -= 20
            for other in others:
                if other.alive:
                    other.hp -= randint(15, 20)
            return True
        else:
            return False
        pass

    def resume(self):
        r_p = randint(1, 10)
        self._mp += r_p
        return r_p

    def __str__(self):
        return '~~~%s奥特曼~~~\n' % self._name + \
                    '生命值: %d\n' % self._hp + \
                    '魔法值: %d\n' % self._mp

    pass


#define monster
class monster(fighter):
    def __init__(self, name, hp):
        super().__init__(name, hp)

    def attack(self, other):
        other.hp -= randint(10, 20)

    def __str__(self):
        return '~~~%s小怪兽~~~\n' % self._name + \
                    '生命值: %d\n' % self._hp

    pass


def is_any_alive(monsters):
    """
    判断有没有小怪兽是活着的
    """
    for monster in monsters:
        if monster.alive > 0:
            return True
    return False


def select_alive_one(monsters):
    """
    选中一只活着的小怪兽
    """
    monsters_len = len(monsters)
    while True:
        index = randrange(monsters_len)
        monster = monsters[index]
        if monster.alive > 0:
            return monster


def display_info(ultraman, monsters):
    """
    显示奥特曼和小怪兽的信息
    """
    print(ultraman)
    for monster in monsters:
        print(monster, end='')


def main():
    print("game start")
    u = Ultraman('迪迦', 1000, 50)
    m1 = monster('白元芳', 300)
    m2 = monster('狄仁杰', 400)
    m3 = monster('方启鹤', 750)
    m_list = [m1, m2, m3]
    fight_round = 1
    while u.alive and is_any_alive(m_list):
        print('========第%02d回合========' % fight_round)
        attack = randint(1, 10)
        m = select_alive_one(m_list)
        if attack <= 6:
            print('%s使用普通攻击打了%s.' % (u.name, m.name))
            u.attack(m)
            print('%s恢复了%s点魔力.' % (u.name, u.resume()))
        elif attack < 10:
            if u.magic_attack(m_list):
                print('%s使用AOE攻击' % (u.name))
            else:
                print('%s使用AOE攻击失败' % (u.name))
        else:
            if u.huge_attack(m):
                print('%s使用致命攻击打了%s.' % (u.name, m.name))
            else:
                print('%s使用普通攻击打了%s.' % (u.name, m.name))
                print('%s恢复了%s点魔力.' % (u.name, u.resume()))
        if m.alive:
            m.attack(u)
            print('%s攻击了%s.' % (m.name, u.name))
            if u.alive == False:
                print('%s杀死了%s.' % (m.name, u.name))
                break
        display_info(u, m_list)
        fight_round += 1
    print('\n========战斗结束!========\n')
    if u.alive > 0:
        print('%s奥特曼胜利!' % u.name)
    else:
        print('小怪兽胜利!')
    pass


if __name__ == "__main__":
    main()
    pass