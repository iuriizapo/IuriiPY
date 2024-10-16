def print_params(a = 1, b = 'строка', c = True):
    print(a, b, c)

print_params(b = 25)
print_params(c = [1,2,3])
print_params()

values_list = [18, 'qwerty', False]
values_dict = {'a': 8, 'b': [1, 2, 3], 'c': True}

print_params(*values_list)
print_params(**values_dict)

values_list_2 = ['OPen', (1, 3, 5)]

print_params(*values_list_2, 42)
