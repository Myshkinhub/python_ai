# 子类调用父类方法：不是完全替换父类方法，而是在父类原有功能基础上增加功能
# 方法1 super().方法名()
# 方法2 父类名.方法名()

class Animal():
    def __init__(self, name):
        self.name = name

    def introduce(self):
        print(f"我是一只动物,我叫{self.name}")


class Dog(Animal):
    def __init__(self, name, color):
        super().__init__(name)
        self.color = color

    def introduce(self):
        super().introduce()
        print(f'我的颜色是{self.color}')


print("方法1：super")
dog = Dog("旺财", "黑白")
dog.introduce()

class Animal:
    def __init__(self, name):
        self.name = name

    def introduce(self):
        print(f'我是一只动物,我叫{self.name}')

class Dog(Animal):
    def __init__(self, name,color):
        Animal.__init__(self, name)
        self.color = color
    def introduce(self):
        Animal.introduce(self)
        print(f'我的颜色是{self.color}')

print("\n方法2：父类名Animal")
dog = Dog('旺财','蓝色')
dog.introduce()