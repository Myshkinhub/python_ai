# weight = int(input("请输入体重(kg)："))
# height = input("请输入身高(cm)：")
# height = int(height) / 100
# bmi = weight / (height * height)
#
# if bmi < 18.5:
#     print("偏瘦")
# elif 18.5<=bmi<23.9:
#     print("正常")
#
# elif 24<=bmi<27.9:
#     print("超重")
# else:
#     print("肥胖")

#三元表达式

age = 20
status = "成年" if age >= 18 else "未成年"
print(status)

member = input("请问您是否是会员，输入是或否：")
price = float(input("请输入您的消费金额："))

if member=='是':
    if price >= 200:
        cost = price - 50
    else:
        cost = price * 0.9
else:
    cost = price

print(f"您的实际支付金额为{cost:.2f}元")