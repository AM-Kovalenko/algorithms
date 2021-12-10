import numpy as np
import matplotlib.pyplot as plt

N = 100
sigma = 3
k = 0.5
b = 2

f = np.array([k * z + b for z in range(N)])  # теоретическая кривая
y = f + np.random.normal(0, sigma, N)
x = np.array(range(N))

# Если k b -неизвестны, то их можно найти по МНК:
mx = x.sum() / N
my = y.sum() / N
a2 = np.dot(x.T, x) / N       # dot -умножение двух векторов или матриц
a11 = np.dot(x.T, y) / N

# вычисление оценок параметров k,b:
kk=(a11 - mx*my)/(a2 - mx**2)
bb = my - kk*mx

ff = np.array([kk * z + bb for z in range(N)])


plt.plot(f)
plt.plot(ff, c='red')
plt.scatter(x, y, s=2, c='red')  # фукция отображает отдельные точки
plt.grid(True)
plt.show()
