def get_matrix(n, m, value):
    list_m = []
    list_n = []
    for i in range(m):
        list_m.append(value)
    for j in range(n):
        list_n.append(list_m)
    print(list_n)

get_matrix(3, 5, 8)



