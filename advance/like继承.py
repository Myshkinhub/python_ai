class PaperPlane():
    def fly(self):
        print("纸飞机会飞")

class Bird():
    def fly(self):
        print("鸟会飞")

class Angle(Bird):
    def fly(self):
        print("🦅会飞")

def fly_bird(bird: Bird):
    bird.fly()

# like继承，无需两个类之间有明确的继承关系，有相同的方法即可
# python不仅支持is方式的继承，也支持like方式的继承
if __name__ == "__main__":
    angle = Angle()
    fly_bird(angle)
    plane = PaperPlane()
    fly_bird(plane)
