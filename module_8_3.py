class IncorrectVinNumber(Exception):
    def __init__(self, *args):
        self.message = args

class IncorrectCarNumbers(Exception):
    def __init__(self, *args):
        self.message = args

class Car:
    def __init__(self, model, vin, number):
        self.model = model
        if self.__is_valid_vin(vin):
            self.__vin = vin
        if self.__is_valid_numbers(number):
            self.__numbers = number

    def __is_valid_vin(self, vin):
        if not 1000000 <= vin <= 9999999:
            raise IncorrectVinNumber('Неверный диапазон для vin номера', vin)
        elif not isinstance(vin, int):
            raise IncorrectVinNumber('Некорректный тип vin номер', vin)
        else:
            return True

    def __is_valid_numbers(self, number):
        if not isinstance(number, str):
            raise IncorrectCarNumbers('Некорректный тип данных для номеров', number)
        elif len(number) != 6:
            raise IncorrectCarNumbers('Неверная длина номера', number)
        else:
            return True

try:
    first = Car('Model1', 1000000, 'f123dj')
except IncorrectVinNumber as exc:
    print(exc.message)
except IncorrectCarNumbers as exc:
    print(exc.message)
else:
    print(f'{first.model} успешно создан')

try:
    second = Car('Model2', 300, 'т001тр')
except IncorrectVinNumber as exc:
    print(exc.message)
except IncorrectCarNumbers as exc:
    print(exc.message)
else:
    print(f'{second.model} успешно создан')

try:
    third = Car('Model3', 2020202, 'нет номера')
except IncorrectVinNumber as exc:
    print(exc.message)
except IncorrectCarNumbers as exc:
    print(exc.message)
else:
    print(f'{third.model} успешно создан')