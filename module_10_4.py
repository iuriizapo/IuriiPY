import time
import threading
from queue import Queue
from random import randint


class Table:
    def __init__(self, num, guest=None):
        self.num = num
        self.guest = guest


class Guest(threading.Thread):
    def __init__(self, name):
        super().__init__()
        self.name = name

    def run(self):
        time.sleep(randint(3,10))


class Cafe:
    def __init__(self, *args):
        self.tables = args
        self.queue_guest = Queue()

    def guest_arrival(self, *guests):
        guest_s = guests
        for x, y in zip(self.tables, guest_s):
            x.guest = y.name
            print(f'{y.name} сел(-а) за стол номер {x.num}')
            y.start()
            y.join()

        for i in list(guest_s)[len(self.tables):]:
            print(f'{i.name} в очереди')
            self.queue_guest.put(i)

    def discuss_guests(self):

        queue_table = Queue()
        while not self.queue_guest.empty():
            for arg in self.tables:
                if arg.guest:
                    for guest in guests:
                        if guest.name == arg.guest:
                            while guest.is_alive():
                                pass
                            else:
                                print(f'{guest.name} покушал(-а) и ушёл(ушла)\nСтол номер {arg.num} свободен')
                                arg.guest = None
                                queue_table.put(arg)

            if queue_table.empty():
                pass
            else:
                item = queue_table.get()
                pers = self.queue_guest.get()
                item.guest = pers.name
                print(f'{pers.name} вышел(-ла) из очереди и сел(-а) за стол номер {item.num}')
                pers.start()
                pers.join()
        else:
            for arg in self.tables:
                if arg.guest:
                    print(f'{arg.guest} покушал(-а) и ушёл(ушла)\nСтол номер {arg.num} свободен')
                    arg.guest = None
            else:
                print(f'Кафе отработало до последнего клиента! Всем спасибо! Все свободны!')


tables = [Table(number) for number in range(1, 6)]
guests_names = [
'Maria', 'Oleg', 'Vakhtang', 'Sergey', 'Darya', 'Arman',
'Vitoria', 'Nikita', 'Galina', 'Pavel', 'Ilya', 'Alexandra'
]
guests = [Guest(name) for name in guests_names]
cafe = Cafe(*tables)
cafe.guest_arrival(*guests)
cafe.discuss_guests()