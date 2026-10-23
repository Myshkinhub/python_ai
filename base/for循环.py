# str = "hello world"
# for char in str:
#     print(char, end=' ')
#
# print("\n")
# # 不包括stop
# for a in range(1, 20, 2):
#     print(a, end=' ')
#
# for a in range(0, 2):
#     username = input("请输入用户名：")
#     password = input("请输入密码：")
#     if username == "username":
#         if password == "python":
#             print("用户名正确，密码正确！")
#             break
#         else:
#             print("用户名正确，密码错误")
#     else:
#         print("用户名错误，登录失败")
# # for循环跟的else子句表示，循环正常结束，没有被break中断时执行的代码块
# else:
#     print("次数用尽，登录失败！")

# 打印九九乘法表
for i in range(1, 10):
    for j in range(1, i + 1):
        print((f"{i} * {j} = {i * j}"), end=' ')
    print()
