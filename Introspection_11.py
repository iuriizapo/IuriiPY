import inspect
import sys


class Runner:
    def __init__(self, name, speed=5):
        if isinstance(name, str):
            self.name = name
        else:
            raise TypeError(f'Имя может быть только строкой, передано {type(name).__name__}')
        self.distance = 0
        if speed > 0:
            self.speed = speed
        else:
            raise ValueError(f'Скорость не может быть отрицательной, сейчас {speed}')

    def run(self):
        self.distance += self.speed * 2

    def walk(self):
        self.distance += self.speed

    def __str__(self):
        return self.name

    def __repr__(self):
        return self.name

    def __eq__(self, other):
        if isinstance(other, str):
            return self.name == other
        elif isinstance(other, Runner):
            return self.name == other.name


class Tournament:
    def __init__(self, distance, *participants):
        self.full_distance = distance
        self.participants = list(participants)

    def start(self):
        finishers = {}
        place = 1
        while self.participants:
            for participant in self.participants:
                participant.run()
                if participant.distance >= self.full_distance:
                    finishers[place] = participant
                    place += 1
                    self.participants.remove(participant)

        return finishers

def introspection_info(obj):
    atr_met = dir(obj)
    if '__static_attributes__' in atr_met:
        stat_atr = obj.__static_attributes__
    else:
        stat_atr = None
    if hasattr(obj, '__name__'):
        name = obj.__name__
    else:
        name = None

    return (f'Name: {name}\n'
            f'Type: {type(obj)}\n'
            f'attributes: {stat_atr}\n'
            f'methods: {atr_met}\n'
            f'size: {sys.getsizeof(obj)}\n'
            f'module: {inspect.getmodule(obj)}\n'
            f'version: {sys.version}')


first = Runner('Вася', 10)
second = Runner('Илья', 5)
third = Runner('Арсен', 10)

t = Tournament(101, first, second)
print(t.start())

a = introspection_info(Runner)
print(a)


