num = int(input('Введите число от 3 до 20 '))
result = []
for i in range(1,20):
    for j in range(2,20):
        if i < j:
            if num % (i + j) == 0:
                result.append(i)
                result.append(j)

print(*result, sep='')
