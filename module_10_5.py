import datetime
from multiprocessing import Pool


def read_info(name):
    all_data = []
    with open(name, encoding='utf-8') as file:
        while file.readline():
            line = file.readline()
            all_data.append(line)
        else:
            print(f'Чтение файла {name} завершено')


filenames = [f'./file {number}.txt' for number in range(1, 5)]

#t_start = datetime.datetime.now()
#for file in filenames:
#    read_info(file)
#t_end = datetime.datetime.now()
#print('Время работы: ' + str(t_end - t_start))

def pool_start():
    t_start = datetime.datetime.now()
    p = Pool(4)
    p.map(read_info, filenames)
    t_end = datetime.datetime.now()
    print('Время работы: ' + str(t_end - t_start))


if __name__ == '__main__':
    pool_start()

