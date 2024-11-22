import io


def custom_write(file_name, strings):
    file = open(file_name, 'r+', encoding='utf-8')
    l = strings
    d = {}
    for i in range(len(l)):
        d[(i+1,file.tell())] = l[i]
        file.write(f'{l[i]}\n')
    file.close()
    return d


info = ['Text for tell.', 'Используйте кодировку utf-8.',
        'Because there are 2 languages!', 'Спасибо!']
result = custom_write('test.txt', info)
for elem in result.items():
    print(elem)

