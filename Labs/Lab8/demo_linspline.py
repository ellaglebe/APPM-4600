import matplotlib.pyplot as plt
import numpy as np
import math
from numpy.linalg import inv 


def driver():
    
    f = lambda x: 1/(1+(10*x)**2)
    a = -1
    b = 1
   
    
    ''' create points you want to evaluate at'''
    Neval = 1000
    xeval =  np.linspace(a,b,Neval)
    
    
    ''' number of intervals'''
    Nint = 20
    xint = np.linspace(a,b,Nint+1)
    
    '''evaluate the linear spline'''
    yeval = eval_lin_spline(xeval,Neval,a,b,f,Nint)
    Mi = eval_Mi(Nint, a, b,f)
    S = eval_cubic(a,b,Mi,f,xeval,Nint, Neval)

    

    ''' evaluate f at the evaluation points'''
    fex = np.zeros(Neval)
    for j in range(Neval):
      fex[j] = f(xeval[j]) 
      
    
    plt.figure()
    plt.plot(xeval,fex,'ro-')
    plt.plot(xeval,yeval,'bs-')
    plt.legend()

    plt.figure()
    plt.plot(xeval,fex)
    plt.plot(xeval,S,'o')
    plt.legend()
     
    err = abs(yeval-fex)
    plt.figure()
    plt.plot(xeval,err,'ro-')
    plt.show()

    
    
    

def line_eval(x0,fx0,x1,fx1, xeval):
    m = (fx1-fx0)/(x1-x0)
    return m*(xeval-x0)+fx0
    
def  eval_lin_spline(xeval,Neval,a,b,f,Nint):

    '''create the intervals for piecewise approximations'''
    xint = np.linspace(a,b,Nint+1)
   
    '''create vector to store the evaluation of the linear splines'''
    yeval = np.zeros(Neval)
    


    for jint in range(Nint):
        ind = np.where((xint[jint]<xeval) & (xint[jint+1]>xeval))
        n = len(ind[0])
        '''find indices of xeval in interval (xint(jint),xint(jint+1))'''
        '''let ind denote the indices in the intervals'''
        '''let n denote the length of ind'''
        
        '''temporarily store your info for creating a line in the interval of 
         interest'''
        a1= xint[jint]
        fa1 = f(a1)
        b1 = xint[jint+1]
        fb1 = f(b1)
        
        for kk in range(n):
            yeval[ind[0][kk]] = line_eval(a1,fa1,b1,fb1,xeval[ind[0][kk]])
 
        '''use your line evaluator to evaluate the lines at each of the points in the interval'''
        '''yeval(ind(kk)) = call your line evaluator at xeval(ind(kk)) with the points (a1,fa1) and (b1,fb1)'''
    return yeval
def eval_Mi(Nint, a, b,f):
    xint = np.linspace(a,b,Nint+1)
    hi = (b-a)/Nint
    V = np.zeros([Nint-1,Nint-1])
    for i in range(Nint-1):
        for j in range(Nint-1):
            if i==j:
                V[i][j] = 1/3
            elif abs(i-j) ==1:
                V[i][j] = 1/12
    V_inv = inv(V)
    y = np.zeros([Nint-1,1])
    for k in range(Nint-1):
        y[k] = (f(xint[k+1]) -2*f(xint[k])+f(xint[k-1]))/(2*hi**2)
    Mi = V_inv.dot(y)
    return Mi


def eval_cubic(a,b,Mi, f, xeval, Nint, Neval):
    xint = np.linspace(a,b,Nint+1)
    S = np.zeros([Nint-1,1])
    C = np.zeros([Nint-1,1])
    D = np.zeros([Nint-1,1])
    for c in range(Nint-2):
        hi = xint[c+1]-xint[c]
        C = f(xint[c])/hi-(hi*Mi[c])/6
        D = f(xint[c+1])/hi-(hi*Mi[c+1])/6
        S[c] = Mi[c]*(xint[c+1]-xeval**3)/(6*hi)+Mi[c+1]*((xeval-xint[c])**3)/(6*hi)+C*(xint[c+1]-1)+D*(xeval-xint[c])
    return S
    

           
if __name__ == '__main__':
      # run the drivers only if this is called from the command line
      driver()               
