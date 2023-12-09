import numpy as np
from numpy import exp
import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d import Axes3D
from matplotlib import cm
from numpy import linalg as LA

# Не актуально, так как точки слишком простые оказались, были ошибки в вычислениях...

def gessian(x,y):
    return np.array([
        (x**2 -x*y + 2*y**2 +2*x -y) + (2*x-y+2), # xx
        (2*x**2 -2*x*y + 4*y**2 +3*x +2*y-1), # xy
        (2*x**2 -2*x*y + 4*y**2 +3*x +2*y-1), # yx
        (4*x**2 -4*x*y + 8*y**2 -4*x +16*y+4), # yy
        
    ])

def get_minor1(m):
    return m[0]

def get_minor2(m):
    return m[0]*m[3] - m[1]*m[2]

def get_extr(x,y):
    print(f"point is {x} {y}")
    print(gessian(x,y))
    print(get_minor1(gessian(x,y)))
    print(get_minor2(gessian(x,y)))
    print("----")

get_extr(0,0)
# get_extr(0,0.5)
# get_extr(0,-1)
# get_extr(-105/143,-0.98)
# get_extr(-105/143,1.11)