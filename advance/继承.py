# 动物类
class Animal:
    def __init__(self, name, age):
        self.name = name
        self.age = age

        # 私有方法, 咆哮
    def __roar(self):
        print('野性的呼唤，原始觉醒')

# 猫类
class Cat(Animal):
    pass

class Dog(Animal):
    # Dog类的__init__方法会覆盖掉父类同名的__init__方法
    def __init__(self, name, age):
        self.name = name
        self.age = age
        self.type = 'dog'

# 调用的是Animal的__init__方法
cat = Cat('小猫',5)
# 创建Dog实例
dog = Dog('小狗',6)
print(cat.name, cat.age)
print(dog.type)


class Bird(Animal):
    # 将共性属性的初始化放入Animal，调用Animal的__init__方法
    # 将Bird特性的属性的初始化放入Bird
    def __init__(self, name, age, type):
        # 调用父类的__init__方法
        super().__init__(name, age)
        # 特性属性的初始化
        self.type = type


bird =  Bird('小鸟',200,'金雕')
print(bird.type)
print(bird.age)
print(bird.name)

# 在Bird的__dict__看不到从父类继承的方法
print(Bird.__dict__)
# 在Animal中看到私有方法__roar改名了_Animal__roar
print(Animal.__dict__)
# 可以理解为_Animal__roar被Bird类继承了
# 根据__mro__顺序去查找，先查找Bird类，没有_Animal__roar
# 继续去上一级Animal查找，找到_Animal__roar
bird._Animal__roar()


# 多继承
class baseA:
    def show(self):
        print("A")

class baseB:
    def show(self):
        print("B")

class C(baseA, baseB):
    pass

c = C()
c.show()
# 显示的是A而不是B，因为多继承时python按照mro查找方法
# MRO（Method Resolution Order，方法解析顺序）
print(C.__mro__)

