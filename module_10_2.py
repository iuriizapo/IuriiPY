import time
import threading


class Knight(threading.Thread):
    def __init__(self, name, power):
        super().__init__()
        self.name = name
        self.power = power

    def run(self):
        enemy = 100
        count = 0
        print(f'{self.name}, на нас напали!')
        while enemy:
            time.sleep(1)
            enemy -= self.power
            count += 1
            print(f'{self.name} сражается {count} дней, осталось {100-count*self.power} воинов.')
        else:
            print(f'{self.name} одержал победу спустя {count} дней(дня)!')



first_knight = Knight('Sir Lancelot', 10)
second_knight = Knight("Sir Galahad", 20)
first_knight.start()
second_knight.start()
first_knight.join()
second_knight.join()

while first_knight.is_alive() or second_knight.is_alive():
    pass
else:
    print(f'Все битвы закончились!')


