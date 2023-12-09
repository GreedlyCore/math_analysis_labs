# import libraries
import math

import numpy as np
import matplotlib.pyplot as plt
import matplotlib.patches as patches
import matplotlib.animation as animation

# ignore warnings
import warnings

warnings.filterwarnings("ignore")

# set a random seed for random generator
np.random.seed(42)


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


f = lambda x: (math.e) ** x

a, b = 0, 1  # the intervals of integration
N = 200  # number of points to generate
factor = 1  # increase num of rectangles every iteration

X = np.linspace(a, b, N + 1)  # generate more points on the x-axis
Y = f(X)  # generate more function values

fig = plt.figure(figsize=(21, 14))  # make a new figure


# animation function
def animate(i):
    plt.cla()  # clear all previous axes objects
    ax = plt.axes(xlim=(a, b), ylim=(0, 4))  # make a new axes object

    ax.set_xticks(np.linspace(a, b, 11))  # format the x-axis
    ax.set_xlabel('X-axis', fontsize=30)

    ax.set_yticks(np.linspace(0, 4, 11))  # format the y-axis
    ax.set_ylabel('Y-axis', fontsize=30)

    ax.tick_params(labelsize=22)  # make the ticks larger

    num_rectangles = (i + 1) * factor  # calculate the number of rectangles

    x = np.linspace(a, b, num_rectangles + 1)  # generate the intervals on the x-axis
    y = f(x)  # generate the function values

    y_int = calculate_integral(f, a, b, num_rectangles, "left")  # calculate the integral
    err = np.abs(np.pi - y_int)  # calculate the absolute error

    # take the left end-points
    x_left = x[:-1]
    y_left = y[:-1]

    ax.plot(x_left, y_left, c='#2CBDFE', marker='.', markersize=10)  # plot the left points
    ax.plot(X, Y, c='#2CBDFE')  # plot the smoother line

    bar = ax.bar(x, y, width=1.0 * (b - a) / num_rectangles, alpha=0.3, align='edge', color='#47DBCD',
                 edgecolor='#2CBDFE', lw=2)
    ax.set_title('Riemann Sum for $ \int_{{0}}^{{1}} e^x \,dx$. \n' +
                 '{0} trapezoids: Value: {1:.9f} Approx. err. {2:.9f}'.format(num_rectangles, y_int, err), fontsize=30)

    return bar


# call the animator
anim = animation.FuncAnimation(fig, animate, frames=40, interval=120, blit=True)
anim.save('riemann_sum.mp4', writer=animation.FFMpegWriter(fps=60) )
