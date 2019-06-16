"""
某公司有三种类型的员工 分别是部门经理、程序员和销售员
需要设计一个工资结算系统 根据提供的员工信息来计算月薪
部门经理的月薪是每月固定15000元
程序员的月薪按本月工作时间计算 每小时150元
销售员的月薪是1200元的底薪加上销售额5%的提成
"""
from abc import abstractclassmethod, ABCMeta


class employee(object, metaclass=ABCMeta):
    def __init__(self, name):
        self._name = name

    @property
    def name(self):
        return self._name

    @abstractclassmethod
    def get_salary(self):
        pass

    pass


class department_manager(employee):
    def get_salary(self):
        return 15000

    pass


class programmer(employee):
    def __init__(self, name, working_hour=0):
        super().__init__(name)
        self._working_hour = working_hour

    @property
    def working_hour(self):
        return self._working_hour

    @working_hour.setter
    def working_hour(self, working_hour):
        self._working_hour = working_hour if working_hour > 0 else 0

    def get_salary(self):
        return self._working_hour * 150

    pass


class saleman(employee):
    def __init__(self, name, sales=0):
        super().__init__(name)
        self._sales = sales

    @property
    def sales(self):
        return self._sales

    @sales.setter
    def sales(self, sales):
        self._sales = sales

    def get_salary(self):
        return 1200 + int(0.05 * self._sales)


def main():
    employees = [
        department_manager('刘备'),
        programmer('孔明'),
        department_manager('曹操'),
        programmer('荀彧'),
        saleman('吕布'),
        programmer('张辽')
    ]
    for em in employees:
        if isinstance(em, programmer):
            em.working_hour = int(input("%s work hours is: " % em.name))
        if isinstance(em, saleman):
            em.sales = int(input('%s sales is: ' % em.sales))
    print("===============salary is=================")
    for em in employees:
        print("%s salary is $%d 元" % (em.name, em.get_salary()))
    pass


if __name__ == "__main__":
    main()
    pass
