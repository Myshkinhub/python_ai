'''
用一个父类对象引用子类对象，通过父类对象调用方法，能够触发子类对象的方法
这种机制就是多态

多态必要条件:
1. 必须要有继承关系
2. 子类重写父类方法
3. 父类对象引用子类对象
'''

class Animal:
    def __init__(self, name, age):
        self.name = name
        self.age = age

    def behavior(self):
        print(f"我是{self.name}，跑跑跑")


class Dog(Animal):
    def __init__(self, name, age):
        Animal.__init__(self, name, age)

    def behavior(self):
        print(f"我叫{self.name}，汪汪汪")


class Cat(Animal):
    def __init__(self, name, age):
        Animal.__init__(self, name, age)

    def behavior(self):
        print(f"我叫{self.name}，喵喵喵")


def animal_behavior(Animal):
    Animal.behavior()

if __name__ == '__main__':
    c = Cat("小猫", 2)
    d = Dog("小狗", 3)
    animal_behavior(Animal("动物", 10))
    animal_behavior(Cat("小猫", 2))
    animal_behavior(Dog("小狗", 3))

