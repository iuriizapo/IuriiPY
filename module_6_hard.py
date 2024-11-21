import math


class Figure:
    sides_count = 0
    def __init__(self, col=(0, 0, 0), *args):
        self.filled = True
        if self.__is_valid_sides(*args):
            self.__sides = list(args)
        else:
            if len(list(args)) == 1:
                self.__sides = list(args * self.sides_count)
            else:
                self.__sides = [1] * self.sides_count
        if self.__is_valid_color(col):
            self.__color = list(col)


    def get_color(self):
        print(self.__color)

    def __is_valid_color(self, col=(0, 0, 0)):
        if 0 <= col[0] <= 255 and 0 <= col[1] <= 255 and 0 <= col[2] <= 255:
            return True
        else:
            return False

    def set_color(self, col=(0, 0, 0)):
        if self.__is_valid_color(col):
            self.__color = list(col)


    def get_sides(self):
        return self.__sides

    def __len__(self):
        return sum(self.__sides)

    def set_sides(self, *args):
        if len(list(args)) == 1:
            self.__sides = list(args * self.sides_count)
        elif len(list(args)) == self.sides_count:
            self.__sides = list(args)

    def __is_valid_sides(self, *args):
        sides = list(args)
        for side in sides:
            if len(sides) == self.sides_count and isinstance(side, int) == True:
                return True
            else:
                return False

class Circle(Figure):
    sides_count = 1
    def __init__(self, col=(0, 0, 0), *args):
        super().__init__( col, *args)
        self.__radius = len(self)/ 2 / math.pi

    def get_square(self):
        return self.__radius ** 2 * math.pi

class Triangle(Figure):
    sides_count = 3
    def __init__(self, col=(0, 0, 0), *args):
        super().__init__( col, *args)

    def get_square(self):
        a = self.get_sides()
        p = len(self) / 2
        return (p * (p - a[0]) * (p - a[1]) * (p - a[2])) ** 0.5

class Cube(Figure):
    sides_count = 12
    def __init__(self, col=(0, 0, 0), *args):
        super().__init__( col, *args)

    def get_volume(self):
        return (len(self) / 12) ** 3


c1 = Circle((200, 200, 100), 10, 15, 6)    # т.к. сторона у круга всего 1, то его стороны будут - [1]
print(c1.get_sides())
t1 = Triangle((200, 200, 100), 10, 6)     # т.к. сторон у треугольника 3, то его стороны будут - [1, 1, 1]
print(t1.get_sides())
k1 = Cube((200, 200, 100), 9)     # т.к. сторон(рёбер) у куба - 12, то его стороны будут - [9, 9, 9, ....., 9] (12)
print(k1.get_sides())
k2 = Cube((200, 200, 100), 9, 12)      # т.к. сторон(рёбер) у куба - 12, то его стороны будут - [1, 1, 1, ....., 1]
print(k2.get_sides())

circle1 = Circle((200, 200, 100), 10) # (Цвет, стороны)
cube1 = Cube((222, 35, 130), 6)
# Проверка на изменение цветов:
circle1.set_color((55, 66, 77))     # Изменится
print(circle1.get_color())
cube1.set_color((300, 70, 15))    # Не изменится
print(cube1.get_color())

# Проверка на изменение сторон:
cube1.set_sides(5, 3, 12, 4, 5) # Не изменится
print(cube1.get_sides())
circle1.set_sides(15) # Изменится
print(circle1.get_sides())

# Проверка периметра (круга), это и есть длина:
print(len(circle1))

# Проверка объёма (куба):
print(cube1.get_volume())



