class Animal:
    def __init__(self, name):
        self.name = name
        self.alive = True
        self.fed = False

    def eat(self, food):
        self.food = food
        if food.edible == False:
            self.alive = False
            print(f'{self.name} не стал есть {food.name}')
        else:
            self.fed = True
            print(f'{self.name} съел {food.name}')

class Plant:
    def __init__(self, name):
        self.name = name
        self.edible = False

class Mammal(Animal):
    def __init__(self, name):
        self.name = name
        super().__init__(name)

class Predator(Animal):
    def __init__(self, name):
        self.name = name
        super().__init__(name)

class Flower(Plant):
    def __init__(self, name):
        self.name = name
        super().__init__(name)

class Fruit(Plant):
    def __init__(self, name):
        self.name = name
        super().__init__(name)
        self.edible = True

a1 = Predator('Волк с Уолл-Стрит')
a2 = Mammal('Хатико')
p1 = Flower('Цветик семицветик')
p2 = Fruit('Заводной апельсин')

print(a1.name)
print(p1.name)
print(a1.alive)
print(a2.fed)
a1.eat(p1)
a2.eat(p2)
print(a1.alive)
print(a2.fed)

