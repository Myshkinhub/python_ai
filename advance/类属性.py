class Student(object):
    def __init__(self, name, age):
        self.name = name
        self.age = age
        Student.count += 1

    school = '方城县第一高级中学'
    class_money = 100
    count = 0


s1 = Student('jack', 18)
s2 = Student('john',17)

print(s1.school)
print(Student.school)
print(Student.count)

# 看似是通过对象修改类属性，实则是添加了对象的属性
# 赋值操作的二义性
s1.school = "guet"
print(s1.school)

# 通过对象使用类属性进行修改，不会产生二义性
# s1.class_money = s1.class_money - 20
# 右侧的class_money是类属性进行修改，但是赋值操作对s1创建了新的对象属性（左侧的class_money）
s1.class_money -= 20
print(f"s1班费：{s1.class_money}")
print(f"班费：{Student.class_money}")

