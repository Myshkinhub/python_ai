class BaseSkin:
    def show(self):
        pass

class BaseHero:
    def __init__(self, name, gender):
        self.name = name
        self.gender = gender
        self.skins = []

class ScOrigin(BaseSkin):
    def show(self):
        print("一往无前的浪！")

class MRJJ(BaseSkin):
    def show(self):
        print("新的未来，正在无限星光中闪烁")

class ScHero(BaseHero):
    def __init__(self, name, gender):
        super().__init__(name, gender)
        skin = ScOrigin()
        self.skins.append(skin)
        self.last_index = 0
        self.skins[self.last_index].show()

    def show(self):
        self.skins[self.last_index].show()

    def buy_skin(self, skin:BaseSkin):
        self.skins.append(skin)

    def change_skin(self, index):
        self.skins[index].show()
        self.last_index = index

hero = ScHero("孙策","男")
hero.buy_skin(MRJJ())
hero.change_skin(1)
hero.show()