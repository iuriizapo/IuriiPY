import os
import time


for dirpath, dirnames, filenames in os.walk("."):
    # перебрать каталоги
    for dirname in dirnames:
        print("Каталог:", os.path.join(dirpath, dirname))
    # перебрать файлы
    for filename in filenames:
        filepath = os.getcwd()
        filetime = os.path.getmtime(filename)
        filesize = os.path.getsize(filename)
        formatted_time = time.strftime("%d.%m.%Y %H:%M", time.localtime(filetime))
        parent_dir = os.path.dirname(filepath)
        print(f'Обнаружен файл: {filename}, Путь: {filepath}, Размер: {filesize} байт, Время изменения:'
              f' {formatted_time}, Родительская директория: {parent_dir}')
