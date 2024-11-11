class Animal:
    live = True
    sound = None
    _DEGREE_OF_DANGER = 0
    def __init__(self, speed, _cords = [0, 0, 0]):
        self.speed = speed
        self._cords = _cords

    def move(self, dx, dy, dz):
        self._cords[0] = dx * self.speed
        self._cords[1] = dy * self.speed
        if dz >= 0:
            self._cords[2] = dz * self.speed
        else:
            print("It's too deep, i can't dive :(")

    def get_cords(self):
        print(f'X: {self._cords[0]} Y: {self._cords[1]} Z: {self._cords[2]}')

    def attack(self):
        print("Sorry, i'm peaceful :)" if self._DEGREE_OF_DANGER < 5 else "Be careful, i'm attacking you 0_0")

    def speak(self):
        print(self.sound)

class Bird(Animal):
    beak = True
    def __init__(self, speed, _cords = [0, 0, 0]):
        super().__init__(speed, _cords = [0, 0, 0])

    def lay_eggs(self):
        from random import randint
        print(f"Here are(is) {randint(1, 4)} eggs for you")

class AquaticAnimal(Animal):
    _DEGREE_OF_DANGER = 3
    def __init__(self, speed, _cords = [0, 0, 0]):
        super().__init__(speed, _cords = [0, 0, 0])

    def dive_in(self, dz):
        self._cords[2] = self._cords[2] - int(abs(dz) / 2 * self.speed)

class PoisonousAnimal(Animal):
    _DEGREE_OF_DANGER = 8
    def __init__(self, speed, _cords = [0, 0, 0]):
        super().__init__(speed, _cords = [0, 0, 0])

class Duckbill(PoisonousAnimal, AquaticAnimal, Bird):
    sound = "Click-click-click"
    def __init__(self, speed, _cords = [0, 0, 0]):
        super().__init__(speed, _cords = [0, 0, 0])


db = Duckbill(10)

print(db.live)
print(db.beak)

db.speak()
db.attack()

db.move(1, 2, 3)
db.get_cords()
db.dive_in(6)
db.get_cords()
db.lay_eggs()







