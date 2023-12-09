# улитка паскаля
import math

a = 3
b = 3


def bool_func_pascal(x, y):
    return ((x ^ 2 + y ^ 2 - 2 * a * x) ^ 2 == 4 * b ^ 2 * (x ^ 2 + y ^ 2))


# phi*math.pi/180
def r(phi):
    return (2 * a * math.cos(phi) + 2 * b)


x = []
square_right = []
square_center = []
print("right dots:")
for n in [10, 100, 1000]:
    sum = 0
    for k in range(1, n):
        sum += 0.5 * (2 * math.pi / n) * (r((2 * math.pi * k / n)) ** 2)
    square_right.append(sum)
    print(sum)

print("mid dots:")

for n in [10, 100, 1000]:
    sum = 0
    for k in range(1, n):
        mid = (2 * math.pi * (2 * k + 1)) / (2 * n)
        sum += 0.5 * (2 * math.pi / n) * (r(mid) ** 2)
    square_center.append(sum)
    print(sum)

for i in range (3):
    print(square_center[i]-square_right[i])

def _rectangle_rule(func, left, right, nseg, frac):
    """Обобщённое правило прямоугольников."""
    dx = 1.0 * (right - left) / nseg
    sum = 0.0
    xstart = left + frac * dx  # 0 <= frac <= 1 задаёт долю смещения точки,
    # в которой вычисляется функция,
    # от левого края отрезка dx
    for i in range(npoints):
        sum += func(xstart + i * dx)

    return sum * dx


def left_rectangle_rule(func, a, b, nseg):
    """Правило левых прямоугольников"""
    return _rectangle_rule(func, a, b, nseg, 0.0)


def right_rectangle_rule(func, a, b, nseg):
    """Правило правых прямоугольников"""
    return _rectangle_rule(func, a, b, npoints, 1.0)


def midpoint_rectangle_rule(func, a, b, nseg):
    """Правило прямоугольников со средней точкой"""
    return _rectangle_rule(func, a, b, nseg, 0.5)


import numpy as np
import matplotlib.pyplot as plt

plt.subplot(111, polar=True)  # Полярная система координат

phi = np.arange(0, 2 * np.pi, 0.01)  # угол phi - массив от от 0 до 2*pi с шагом 0.01
rho = 2 * phi  # расстояние от центра 2*phi
plt.plot(phi, rho, lw=2)  # график rho(phi), толщина линии (line width) 2
plt.show()
