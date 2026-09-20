class Student(object):
    def __init__(self, name, score):
        self.name = name
        #__score表示私有属性
        self.__score = score

    def get_score(self):
        return self.__score

    def set_score(self, score):
        self.__score = score

    def __introduce(self):
        print(f"我叫{self.name},我的分数是{self.__score}")

    # 公有方法调用私有方法
    def introduce(self):
        if(self.__score > 60):
            self.__introduce()

s1 = Student('jack', 80)

# 无法访问私有属性__score
print(s1.name)
s1.set_score(90)
print(s1.get_score())

# 私有属性无法在类外访问，python无法像C++一样实现真正的私有隔离
# 只是将__introduce简单换了个名字
# s1.__introdue

print(Student.__dict__)
print(s1.__dict__)
# __introduce名字被替换为了_Student__introduce
s1._Student__introduce()

# 无法在类外访问私有属性__score 同理
# print(s1.__score)
print(s1._Student__score)

s2 = Student('smith', 80)
s2.introduce()