print("hello world")
age = 18
weight = 20.5
name = "myshkin"

print(type(age))

print(f"姓名:{name}, 体重:{weight:.2f}, 年龄:{age:06d}")
print("年龄:{},体重:{}".format(age, weight))

print("姓名：%s\n年龄：%d\n体重：%.2f"%(name,age,weight))
