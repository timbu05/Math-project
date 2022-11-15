import numpy as np
import matplotlib.pyplot as plt
import pylab
from math import pi, cos, log


def power(a, n):
    return (1 if n == 0
            else power(a * a, n // 2) if n % 2 == 0
    else a * power(a, n - 1))



x_data = np.arange(-2, 2.01, 0.01) # массив координат x
n = 100
b = 0.9 # выбираем b<1
eps = 1e-4
m = round(log(eps) / log(b)) + 1
n = m
a = 3 # выбираем a
y_data = np.array([]) # задаем пустой массив, куда потом будем кидать координаты y
for x in x_data: # проходимся по x
    y = 0
    for i in range(n): # проходимся по значениям показателя степени
        ai = power(a, i) * x * pi # применяем формулу
        bi = power(b, i)
        y += cos(ai) * bi
    y_data = np.append(y_data, y) # добавляем полученное значение y

plt.figure(figsize=(20, 20))
plt.plot(x_data, y_data) # рисуем
plt.grid = True
pylab.xlim (-4, 4)

plt.show()