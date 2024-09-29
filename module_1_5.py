immutable_var = 1 ,2 ,3 ,1>2 ,2<3 ,False ,'Вечерело', 5**2, [ 'a', 'b', 'c']
print(immutable_var)
immutable_var [8] [2] = 'x'
print(immutable_var)
#immutable_var [0] = 5   #TypeError: 'tuple' object does not support item assignment
mutable_list = [1 ,2 ,3 ,1>2 ,2<3 ,False ,'Вечерело', 5**2] + [ 'a', 'b', 'c']
print(mutable_list)
mutable_list.extend('fly')
print(mutable_list)
mutable_list.append('Dubai')
print(mutable_list)
mutable_list [14] = 'Победа'
print(mutable_list)