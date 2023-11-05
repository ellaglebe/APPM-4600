import numpy as np
import numpy.linalg as la
import matplotlib.pyplot as plt

def driver():

    f = lambda x: np.sin(x)
    # Taylor
    t = lambda x: x-(x**3)/6+(x**5)/120-(x**7)/5040
   # pade rational approx
    r = lambda x: (x-7/60*x**3)/(1 + 1/20*x**2)
      
    a= 0
    b = 5
    
    Nint = 3
    # create chebychev nodes
    xint = np.zeros(Nint+1)
    for j in range(1,Nint+2):
       xint[j-1] = np.cos(np.pi*(2*j-1)/(2*(Nint+1)))
    # scale  for the interval
    m = (b-a)/2 
    c = (a+b)/2
    xint = m*xint+c
    xint = xint[::-1]
    
    yint = f(xint)


    # test the different evaluation methods
    Neval = 1000
    xeval = np.linspace(a,b,Neval+1)     

    # compare the errors
    fex = f(xeval)
    f_rat = r(xeval)
    ft = t(xeval)
  
    plt.figure() 
    
    plt.semilogy(xeval,abs(fex-f_rat),'bs--',label='rational')
    plt.semilogy(xeval,abs(fex-ft),'gs--',label='Taylor')
    plt.legend()
    plt.show()
     

    
driver()    
       
