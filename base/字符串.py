str = "helloworld"

# 字符串切片，类似range
print(str[1:5:2])
print(str[-1:-5:-1])

# index抛出异常，且字典元组均有, find查找子串失败返回-1，字符串独有

# replace函数不会修改原字符串，只是返回一个新的
str1 = "python is python"
# 不声明替换次数，则全部替换
str2 = str1.replace('python', 'java', 1)
print(str2)

email = "3198353401@qq.com"
# split返回一个列表
list1 = email.split("@")
print(list1[0])

#
new_str = '-'.join(list1)
print(new_str)
