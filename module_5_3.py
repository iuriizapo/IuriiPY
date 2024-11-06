class House:
    def __init__(self, name, floor):
        self.name = name
        self.number_of_floors = floor

    def __str__(self):
        return (f'Название: {self.name}, кол-во этажей: {self.number_of_floors}')

    def __eq__(self, other):
        if isinstance(other, House):
            return self.number_of_floors == other.number_of_floors
        elif isinstance(other, int):
            return self.number_of_floors == other
        else:
            return 'Всё пропало!'
    def __ne__(self, other):
        return not (self == other)

    def __lt__(self, other):
        return self.number_of_floors < other.number_of_floors
    def __ge__(self, other):
        return not (self < other)

    def __gt__(self, other):
        return self.number_of_floors > other.number_of_floors
    def __le__(self, other):
        return not (self > other)

    def __add__(self, other):
        if isinstance(other, int):
            self.number_of_floors = self.number_of_floors + other
            return self
        elif isinstance(other, House):
            self.number_of_floors = self.number_of_floors + other.number_of_floors
            return self
        else:
            return 'Всё пропало!'
    def __radd__(self, other):
        return self.__add__(other)
    def __iadd__(self, other):
        return self.__add__(other)








h1 = House('ЖК Эльбрус', 10)
h2 = House('ЖК Акация', 20)
print(h1)
print(h2)
print(h1 == h2)
print(h1 != h2)
print(h1 < h2)
print(h1 >= h2)
print(h1 > h2)
print(h1 <= h2)
print(h1)
print(h2)
h1 = h1 + 10
print(h1)
print(h1 == h2)
h2 = 10 + h2 # __radd__
print(h2)
h1 += 10 # __iadd__
print(h1)
print(isinstance(h1, int))
print(type(h1))
