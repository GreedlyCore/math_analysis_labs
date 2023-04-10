import math
import numpy as np
import matplotlib.pyplot as plt


# INPUT: отрезок, число точек разбиения, способ выбора оснащения (левые, правые, средние)
# Разбиение равномерное

f = lambda x : (math.e**x)
a = 0; b = 1;
N = 10 # count of rectangles


def calculate_integral(f, a, b, n, type):
    '''Calculates the integral based on the composite trapezoidal rule
    relying on the Riemann Sums.

    :param function f: the integrand function
    :param int a: lower bound of the integral
    :param int b: upper bound of theintergal
    :param int n: number of rectangles of equal width
    :param String type: вид оснащения - левое(right) правое(left) среднее(mid)
    :return float: the integral of the function f between a and b
    '''
    w = (b - a) / n
    if type == "left":
        result = sum([f(a + i * w) for i in range(1, n + 1)])
    if type == "right":
        result = sum([f(a + (i + 1) * w) for i in range(1, n)])
    if type == "mid":
        result = sum([(f(a + i * w) + f(a + (i + 1) * w)) / 2 for i in range(1, n)])
    result *= w
    return result

def calculate_err(value):
    return np.abs((math.e - 1) - value)


print("compare: left mid right")
for i in [100, 200, 400, 800]:
    print("count of point is ", i)
    left = calculate_integral(f, a, b, i, "left")
    mid = calculate_integral(f, a, b, i, "mid")
    right = calculate_integral(f, a, b, i, "right")
    print(left, calculate_err(left))
    print(mid, calculate_err(mid))
    print(right, calculate_err(right))
    print()






for N in [30, 100, 800]:
    n = 10  # Use n*N+1 points to plot the function smoothly
    x = np.linspace(a, b, N + 1)
    y = f(x)
    X = np.linspace(a, b, n * N + 1)
    Y = f(X)
    plt.figure(figsize=(15,5))

    plt.subplot(1,3,1)
    plt.plot(X,Y,'b')
    x_left = x[:-1] # Left endpoints
    y_left = y[:-1]
    plt.plot(x_left,y_left,'b.',markersize=10)
    plt.bar(x_left,y_left,width=(b-a)/N,alpha=0.2,align='edge',edgecolor='b')
    integral_sum = round(calculate_integral(f, a, b, N, "left"), 7)
    plt.title('Left, N = {}, int sum ={}'.format(N, integral_sum))

    plt.subplot(1,3,2)
    plt.plot(X,Y,'b')
    x_mid = (x[:-1] + x[1:])/2 # Midpoints
    y_mid = f(x_mid)
    plt.plot(x_mid,y_mid,'b.',markersize=10)
    plt.bar(x_mid,y_mid,width=(b-a)/N,alpha=0.2,edgecolor='b')
    integral_sum = round(calculate_integral(f, a, b, N, "mid"), 7)
    plt.title('Midpoint, N = {}, int sum ={}'.format(N, integral_sum))

    plt.subplot(1,3,3)
    plt.plot(X,Y,'b')
    x_right = x[1:] # Left endpoints
    y_right = y[1:]
    plt.plot(x_right,y_right,'b.',markersize=10)
    plt.bar(x_right,y_right,width=-(b-a)/N,alpha=0.2,align='edge',edgecolor='b')
    integral_sum = round(calculate_integral(f, a, b, N, "right"), 7)
    plt.title('Right, N = {}, int sum ={}'.format(N, integral_sum))

    plt.show()