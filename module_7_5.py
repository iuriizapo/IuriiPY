import os
import time


directory = os.getcwd()
print(directory)

for i in os.walk(directory):
    print(i)
filepath = os.getcwd()
print(filepath)
for dirpath, dirnames, filenames in os.walk("."):
    # перебрать каталоги
    for dirname in dirnames:
        print("Каталог:", os.path.join(dirpath, dirname))
    # перебрать файлы
    for filename in filenames:
        print("Файл:", os.path.join(dirpath, filename))
filename = 'module_7_5.py'
filetime = os.path.getmtime(filename)
print(filetime)
filesize = os.stat('module_7_5.py').st_size
print(filesize)
filesize = os.path.getsize(filename)
print(filesize)
formatted_time = time.strftime("%d.%m.%Y %H:%M", time.localtime(filetime))
print(formatted_time)
parent_dir = os.path.dirname(filepath)
print(parent_dir)
print(f'Обнаружен файл: {filename}, Путь: {filepath}, Размер: {filesize} байт, Время изменения: {formatted_time}, Родительская директория: {parent_dir}')