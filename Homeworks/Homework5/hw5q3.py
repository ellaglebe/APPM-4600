import numpy as np
import math
import time
from tabulate import tabulate

def driver():

    x0 = np.array([1,1,1])
    
    Nmax = 100
    tol = 1e-10
    F = lambda x: x[0]**2+4*x[1]**2+4*x[2]**2-16
    Fx = lambda x: 2*x[0]
    Fy = lambda x: 8*x[1]
    Fz = lambda x: 8*x[2]

    points = []

    for i in range(100):
        x1 = np.zeros(3)
        d = F(x0)/(Fx(x0)**2 + Fy(x0)**2 + Fz(x0)**2)

        x1[0] = x0[0] -d*Fx(x0)
        x1[1] = x0[1] - d*Fy(x0)
        x1[2] = x0[2] -d*Fz(x0)

        points.append(x1)

        x0=x1

    print(tabulate(points, headers = ["x","y","z"], tablefmt = "fancy_grid"))

    x = []
    y = []
    z = []
    
    for i in points:
        x.append(i[0])
        y.append(i[1])
        z.append(i[2])
        [alpha, constant] = orderofconvergence(1.09364,x)
     
driver()
    
