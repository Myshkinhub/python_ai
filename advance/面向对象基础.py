class Student:
    pass


s1 = Student()
s2 = Student()

print(s1)
print(s2)

s1.name = "myshkin"
s1.age = 18
s2.name = "jack"
print(f's1.age : {s1.age}')
print(f's1.name : {s1.name}')

# 添加属性的方式可能会导致买个对象的属性不统一，正式项目中使用__init__方法统一初始化属性

