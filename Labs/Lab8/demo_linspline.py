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
    
    '''evaluate the linear spline'''
    yeval = eval_lin_spline(xeval,Neval,a,b,f,Nint)
    
    ''' evaluate f at the evaluation points'''
    fex = np.zeros(Neval)
    for j in range(Neval):
      fex[j] = f(xeval[j]) 
      
    
    plt.figure()
    plt.plot(xeval,fex,'ro-')
    plt.plot(xeval,yeval,'bs-')
    plt.legend()
    plt.show 
     
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
           
if __name__ == '__main__':
      # run the drivers only if this is called from the command line
      driver()               
