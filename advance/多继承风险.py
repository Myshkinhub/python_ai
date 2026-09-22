'''
需求:
1. 定义一个汽车Car基类，构造方法__init__接受汽车的名字和颜色

2. 定义GasolineCar类，继承自Car, 实现__init__方法，接受参数名字，颜色
   以及充能方式
   实现run方法，输出耗油运行
   实现energy方法，输出默认使用燃油

3. 定义ElectricCar类, 实现__init__方法，接受参数名字，颜色
   以及充能方式
   继承自Car，实现run方法，输出耗电运行
   实现energy方法，输出默认使用电能

4. 定义HybridCar类，同时继承自ElectricCar,GasolineCar，
实现run方法，油电混动运行

5.  实例化一个HybridCar对象，调用energy以及run方法，看看输出
'''

class  Car:
    def __init__(self, name, color):
        self.name = name
        self.color = color

class GasolineCar(Car):
    def __init__(self, name, color, charge_type):
        super().__init__(name, color)
        self.charge_type = charge_type

    def run(self):
        print(f"消耗{self.charge_type}运行")

    def energy(self):
        print(f"默认使用{self.charge_type}")

class ElectricCar(Car):
    def __init__(self, name, color, charge_type):
        super().__init__(name, color)
        self.charge_type = charge_type

    def run(self):
        print(f"消耗{self.charge_type}运行")

    def energy(self):
        print(f"默认使用{self.charge_type}")


class HybridCar(ElectricCar, GasolineCar):
    # def __init__(self, name, color, charge_type):
    #     super().__init__(name, color, charge_type)

    def __init__(self, name, color, charge_type):
        self.name = name
        self.color = color
        self.charge_type = charge_type

c1 = GasolineCar("奔驰", "黑色","燃油")
c1.run()
c1.energy()

c2 = ElectricCar("比亚迪", "白色","电能")
c2.run()
c2.energy()


"""
如果HybridCar没有实现__init__方法, 将会导致通过mro顺序调用上一级的__init__方法
而上一级是ElectricCar类，ElectricCar类的__init__方法内部又调用了super()所以会通过mro找到上一级
这个上一级其实是GasolineCar, 进而造成__init__调用参数不匹配而失败
"""
# super() 在当前的 MRO（方法解析顺序）列表中，从当前类之后，寻找下一个类，并返回一个代理对象，用来调用该类的方法

print(HybridCar.__mro__)
c3 = HybridCar("特斯拉", "黑色", "油电混合")
c3.run()

# 结论：当使用多继承时，子类调用父类的方法，一定要用父类名.方法名(参数1,参数2...)