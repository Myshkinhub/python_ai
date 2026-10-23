
#age = input("请输入年龄：")

age = 18
print(f"年龄：{age}")

#input返回的是字符串类型
print(f"年龄的数据类型：{type(age)}")

age = int(age)
print(age*2)

#python只有堆区和栈区
"""
变量存储的是数据的地址

所有的数据都存储在堆区
每次赋值时原来的数据在堆区的空间不会自动释放
通过计数器维护，通过垃圾回收器处理

变量本身没有类型 type()打印的是变量指向的地址单元里的数据的类型
说age的类型为某某某，是为了简化描述
"""
age = "hello world"
print(age)

print(28*'*')
print(28*'1')


num = 3
# **是幂运算
print(num**3)

#//是整除
print(10//3)