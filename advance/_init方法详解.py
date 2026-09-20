class Student:
    def __init__(self, name, age):
        # 不要忘记self, self不是C++的隐式this指针，而是显式的实例引用(必须作为第一个参数写出来)
        # self只是一个普通的形参，约定俗成命名为self

        # 为对象添加对应参数
        self.name = name
        self.age = age

    def introduce(self):
        print(f"我叫{self.name}, 我今年{self.age}岁")

s1 = Student("myshkin",23)
s2 = Student("jack", 18)
# 类似C++的指针，py自动解引用，可通过变量名直接访问对象
# 变量s1、s2在栈区，存储的是对象在堆区的地址

# 调用时，s1自动传递给self
s1.introduce()


print(Student.__dict__)

"""
创建对象时自动调用__init__方法
1. __init__方法的self，指向当前对象地址，其在调用init方法前
通过调用__new__方法在堆区创建，解释器自动将该对象地址赋值给self，无需传入
2. 其他变量即正常的参数传递
"""
