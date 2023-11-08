import numpy as np
import numpy.linalg as la
import matplotlib.pyplot as plt


def driver():

    f = lambda x: x**3
      
    a= -5
    b = 5
    n = 20
    
    xint =np.linspace(a,b)
    yint = f(xint)
    h = xint[1]-xint[0]
    xint2 = np.linspace(a,b,(n*2)+1)
    yint2 = f(xint2)
    h2 = xint2[1]-xint2[0]
    
    N =len(xint) -2
    N2 = len(xint2) -2

    Tn = trap(xint,yint,N,h)
    Sn = simp(xint2,yint2,N2,h2)
    print(Tn,Sn)
    
    # test the different evaluation methods
    Neval = 1000
    xeval = np.linspace(a,b,N)     
def trap(xint,yint,N,h):
    Tn =0
    for i in range(N+1):
        Tn += (h/2)*(yint[i]+yint[i+1])
    return Tn
def simp(xint,yint,N,h):
    Sn = 0
    for i in range(0,N,2):
        Sn += (h/3)*(yint[i]+4*yint[i+1]+yint[i+2])
    return Sn

    


    
driver()    
       
