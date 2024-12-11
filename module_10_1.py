import time
import threading


def wite_words(word_count, file_name):
    with open(file_name, 'a',encoding='utf-8') as file:
        for i in range(1, word_count+1):
            file.write(f'Какое-то слово № {i}\n')
            time.sleep(0.1)

    print(f'Завершилась запись в файл {file_name}')

ts = time.time()
wite_words(10, 'example1.txt')
wite_words(30, 'example2.txt')
wite_words(200, 'example3.txt')
wite_words(100, 'example4.txt')
te = time.time()
print(f'Работа потоков {time.strftime("%H:%M:%S", time.gmtime(te-ts))}')
print()
ts = time.time()
thr1 = threading.Thread(wite_words(10, 'example5.txt'))
thr2 = threading.Thread(wite_words(30, 'example6.txt'))
thr3 = threading.Thread(wite_words(200, 'example7.txt'))
thr4 = threading.Thread(wite_words(100, 'example8.txt'))
thr1.start()
thr1.join()
thr2.start()
thr2.join()
thr3.start()
thr3.join()
thr4.start()
thr4.join()
te = time.time()
print(f'Работа потоков {time.strftime("%H:%M:%S", time.gmtime(te-ts))}')
