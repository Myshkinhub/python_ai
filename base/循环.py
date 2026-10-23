import random

"""
防御式编程
1.不要相信用户的输入，对输入的数据和传入的参数都进行判断
2.对符合条件的数据提前处理，处理完成后提前跳过后面的逻辑

"""
answer = random.randint(1, 20)
count = 3
while 1:
    guess = int(input("请输入一个小于20的数字："))
    if guess == answer:
        print("恭喜你猜对了")
        break
    elif guess < answer:
        count -= 1
        print(f"猜小了，请再次尝试，您还有{count}次机会")
    elif guess > answer:
        count -= 1
        print(f"猜大了，请再次尝试，您还有{count}次机会")

    if count == 0:
        print("您的次数用尽！")
        break
