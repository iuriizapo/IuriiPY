data_structure = [
 [1, 2, 3],
 {'a': 4, 'b': 5},
 (6, {'cube': 7, 'drum': 8}),
 "Hello",
 ((), [{(2, 'Urban', ('Urban2', 35))}])
]
structure_sum = 0
def calculate_structure_sum(x):
    global structure_sum
    for i in range(len(x)):
        if isinstance(x[i], int):
            structure_sum += x[i]
        elif isinstance(x[i], str):
            structure_sum += len(x[i])
        elif isinstance(x[i], list):
            calculate_structure_sum(x[i])
        elif isinstance(x[i], tuple):
            calculate_structure_sum(list(x[i]))
        elif isinstance(x[i], set):
            calculate_structure_sum(list(x[i]))
        elif isinstance(x[i], dict):
            y = x[i]
            calculate_structure_sum(list(y.items()))


calculate_structure_sum(data_structure)
print(structure_sum)

