import numpy as np
import numpy.linalg as la
import matplotlib.pyplot as plt
from scipy import integrate

def driver():

    f = lambda x: 1/(1+x**2)
      
    a= -5
    b = 5
    n1 = 205
    n2 =61
    
    
    xint =np.linspace(a,b,n1)
    yint = f(xint)
    h = xint[1]-xint[0]
    xint2 = np.linspace(a,b,n2)
    yint2 = f(xint2)
    h2 = xint2[1]-xint2[0]
    
    N =len(xint) -2
    N2 = len(xint2) -2

    Tn = trap(xint,yint,N,h)
    Sn = simp(xint2,yint2,N2,h2)
    print(Tn,Sn)

    print(integrate.quad(f,a,b))
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
       
