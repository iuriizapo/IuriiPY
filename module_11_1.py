import random
import numpy as np
import matplotlib
import matplotlib.pyplot as plt


n, m = 3, 3
matrixA = [[2, 4, 6], [1, 3, 5], [6, 4, 8]]
for row in matrixA:
    print(*row)
print()
k = 3
matrixB = [[7, 4, 2], [3, 0, 6], [1, 7, 9]]
for row in matrixB:
    print(*row)
print()
matrixC = [[0] * k for _ in range(n)]

for a in range(k):
    for i in range(n):
        for j in range(m):
            matrixC[i][a] += matrixA[i][j] * matrixB[j][a]

for row in matrixC:
    print(*row)
print()

step = 2    #возведение матрицы А в квадрат
matrixB = matrixA.copy()
matrixC = [[0] * n for _ in range(n)]
while step-1:
    step -= 1
    for a in range(n):
        for i in range(n):
            for j in range(n):
                matrixC[i][a] += matrixA[i][j] * matrixB[j][a]
    matrixA = matrixC.copy()
    matrixC = [[0] * n for _ in range(n)]


for row in matrixA:
    print(*row)

# Фундаментальный элемент NumPy – массив (array)
a = np.array([1,2,3,4,5,6,7,8,9])
a = a.reshape(3, 3)   #из одномерного массива создаем квадратную двухмерную матрицу
print(a)
b = np.array([random.randint(0,100) for _ in range(125)])
b = b.reshape(5,5,5)    #из одномерного массива создаем кубическую матрицу
print(b)
c = np.matmul(b,b)   #возведение матрицы b в квадрат
print(c)
max_c = np.amax(c)
min_c = np.amin(c)
print(max_c, min_c)

print(matplotlib.get_backend())    #вызвали функцию get_backend() для получения
                                   # информации о текущем выбранном backend’е.
plt.plot([1, 2, -6, 0, 4])
plt.show()

y = np.arange(0, 5, 1)             # [0, 1, 2, 3, 4]
x = np.array([a*a for a in y])   # [ 0,  1,  4,  9, 16]
y2 = [0, 1, 2, 3]
x2 = [i+1 for i in y2]
lines = plt.plot(x, y, '-go', x2, y2, 's:m')
plt.show()

x = np.arange(-2*np.pi, 2*np.pi, 0.1)
y = np.cos(x)
plt.plot(x, y)
plt.fill_between(x, y, where=(y < 0), color='r', alpha=0.5)
plt.fill_between(x, y, where=(y > 0), color='g', alpha=0.5)
plt.show()
