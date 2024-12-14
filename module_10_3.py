from random import randint
from time import sleep
import threading


class Bank:

    def __init__(self):
        self.balance = 0
        self.lock = threading.Lock()


    def deposit(self):
        count = 100

        while count:

            #if self.lock.locked() and self.balance >= 500:
            #    self.lock.release()
            #    sleep(0.001)
            self.lock.acquire()
            count -= 1
            depo = randint(50,500)
            self.balance += depo
            print(f'Пополнение: {depo}. Баланс: {self.balance}')
            self.lock.release()
            sleep(0.001)




    def take(self):
        count = 100

        while count:
            self.lock.acquire()
            count -= 1
            kred = randint(50,500)
            print(f'Запрос на {kred}')
            if kred <= self.balance:
                self.balance -= kred
                print(f'Снятие: {kred}. Баланс: {self.balance}')
                self.lock.release()
                sleep(0.001)
            else:
                print(f'Запрос отклонён, недостаточно средств')
                self.lock.release()
                sleep(0.001)


bk = Bank()
th1 = threading.Thread(target=Bank.deposit, args=(bk,))
th2 = threading.Thread(target=Bank.take, args=(bk,))
th1.start()
th2.start()

th1.join()
th2.join()

print(f'Итоговый баланс: {bk.balance}')
