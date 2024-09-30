my_dict = {'Anna': 1987, 'Yana': 2001, 'Mila': 1995}
print('Dictionary:', my_dict)
print('Existing value:', my_dict.get('Yana'))
print('Not existing value:', my_dict.get('Olga'))
my_dict.update({'Zoya': 1978, 'Raya': 2002})
a=my_dict.pop('Mila')
print('Deleted value:', a)
print('Modified dictionary:', my_dict)
my_set = {1, 2, 3, 1, 2, 3, 'Sky', 10>9, True, 'Sky'}   # Как и в лекции логические элементы 10>9 и True не отобразились. Я не понял почему?
print(my_set)
my_set.add(4)
my_set.add('Blue')
my_set.remove(1)
print('Modified set:', my_set)