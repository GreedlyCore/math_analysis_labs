import numpy as np
from numpy import exp
import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d import Axes3D
from matplotlib import cm
from numpy import linalg as LA

def f(X):
    x,y = X
    return (x**2 - x*y + 2*y**2)*exp(x+2*y)

# calculated derivatives before...
def grad(X):
    x,y = X
    return np.array([
        ( (x**2 - x*y + 2*y**2) + 2*x - y )*exp(x+2*y),
        ( 2*(x**2 - x*y + 2*y**2) + 4*y - x )*exp(x+2*y)
    ])

x = np.linspace(-0.6, 0.6, 80)
y = np.linspace(-0.6, 0.6, 80)
x, y = np.meshgrid(x, y)
z = f((x, y))

# start_point
X = [0.5,0.5]
# “learning rate” coeff
gamma = 0.08 
# max iterations of algorithm
max_iter = 50
# small value to stop it...
eps = 0.0001

# first stop condition
# |deltaF| < eps
def grad_descent_1():
    i = 0
    X_old = [10000, 10000]
    X_now = X
    f1 = plt.figure("method1")
    sp1 = f1.add_subplot(projection='3d') # subplot
    sp1.scatter(X_now[0],X_now[1],f(X_now), s=20, marker='o')
    while abs(f(X_old)-f(X_now)) > eps and i < max_iter:
        i +=1
        X_old = X_now
        X_now = X_old - gamma*grad(X_old)
        sp1.scatter(X_now[0],X_now[1],f(X_now), s=20, marker='o')
        print(abs(f(X_old)-f(X_now)))
    if i == max_iter:
        print("max iter achieved - 1st")
    elif i < max_iter:
        print(f"converged in {i} steps - 1st")
    sp1.set_title(f"1st stop condition --> |$\Delta$ f|<$\epsilon$\nconverged in {i} steps to {np.round(X_now,4)}")
    sp1.set_xlabel('X')
    sp1.set_ylabel('Y')
    sp1.set_zlabel('Z')
    sp1.plot_surface(x, y, z, cmap='viridis', alpha=0.6)
    f1.show()

# second stop condition
# ||(deltaX_K, deltaY_K)|| < Delta
# took Euclidean norm
def grad_descent_2():
    i = 0
    X_old = [10000, 10000]
    X_now = X
    f2 = plt.figure("method2")
    sp2 = f2.add_subplot(projection='3d') # subplot
    sp2.scatter(X_now[0],X_now[1],f(X_now), s=20, marker='o')
    while LA.norm(np.abs(np.array(X_now)-np.array(X_old)),2) > eps and i < max_iter:
        i +=1
        X_old = X_now
        X_now = X_old - gamma*grad(X_old)
        sp2.scatter(X_now[0],X_now[1],f(X_now), s=20, marker='o')
        print(abs(f(X_old)-f(X_now)))
    sp2.set_title(f"2nd stop condition --> ||($\Delta x_k$,$\Delta y_k$||<$\delta$\nconverged in {i} steps to {np.round(X_now,4)}")

    if i == max_iter:
            print("max iter achieved - 2st")
    elif i < max_iter:
        print(f"converged in {i} steps - 2st")
    sp2.set_xlabel('X')
    sp2.set_ylabel('Y')
    sp2.set_zlabel('Z')
    sp2.plot_surface(x, y, z, cmap='viridis', alpha=0.6)
    f2.show()

grad_descent_1()
grad_descent_2()

plt.figure("level set")
# show Level set - линии уровня нашей поверхности
cs = plt.contour(x, y, z)
plt.clabel(cs)
plt.xlim([-0.7, 0.7])
plt.ylim([-0.7, 0.7])
# after all plots only
plt.title("$Level\;set\;for\;z(x,y)=(x^2-xy+2y^2)e^{x+2y}$")
plt.show()