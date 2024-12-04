import random


first = 'Мама мыла раму'
second = 'Рамена мало было'
res = list(map(lambda x,y: x == y, first, second))
print(res)

def get_advanced_writer(file_name):

    def write_everything(*data_set):
        with open(file_name,'a', encoding='utf-8') as file:
            for data in data_set:
                file.write(f'{data}\n')
    return write_everything

write = get_advanced_writer('test.txt')
write('Это строчка', ['А', 'это', 'уже', 'число', 5, 'в', 'списке'])

class MysticBall:
    def __init__(self, *args):
        self.words = args
    def __call__(self):
        word = random.choice(self.words)
        return word

first_ball = MysticBall('Да', 'Нет', 'Наверное')
print(first_ball())
print(first_ball())
print(first_ball())
