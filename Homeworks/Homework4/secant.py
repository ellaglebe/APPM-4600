# import libraries
import numpy as np
import matplotlib.pyplot as plt
        
def driver():
#f = lambda x: (x-2)**3
#fp = lambda x: 3*(x-2)**2
#p0 = 1.2
  
 
  f = lambda x: x**6-x-1
  
  p0 = 2
  p1 = 1

  Nmax = 100
  tol = 1.e-13

  (p,pstar,info,it) = secant(f,p0,p1,tol,Nmax)
  print('the approximate root is', '%16.16e' % pstar)
  print('the error message reads:', '%d' % info)
  print('Number of iterations:', '%d' % it)
  print(abs(p-pstar)[0:it])
  xk =abs(p-pstar)[0:it-1]
  xk1=abs(p-pstar)[1:it]
  print('Slope=', (xk[5]-xk[1])/(xk1[5]-xk1[1]))
  plt.plot(xk,xk1)
  plt.xscale('log')
  plt.yscale('log')
  plt.show()


def secant(f,p0,p1,tol,Nmax):
  """
  Newton iteration.
  
  Inputs:
    f,fp - function and derivative
    p0   - initial guess for root
    tol  - iteration stops when p_n,p_{n+1} are within tol
    Nmax - max number of iterations
  Returns:
    p     - an array of the iterates
    pstar - the last iterate
    info  - success message
          - 0 if we met tol
          - 1 if we hit Nmax iterations (fail)
     
  """
  p = np.zeros(Nmax+1);
  if abs(f(p0)) == 0:
    pstar = p0
    info = 0
    return [p,pstar,info,it+1]
  if abs(f(p1))==0:
    pstar =p1
    info = 0
    return [p,pstar,info,it+1]
  fp1=f(p1)
  fp0=f(p0)
  for it in range(Nmax):
      
    if abs(fp1-fp0)==0:
      info = 1
      pstar = p1
      return [p,pstar,info,it+1]
    p2 = p1-(fp1*(p1-p0)/(fp1-fp0))
    if abs(p2-p1)<tol:
      pstar=p1
      info = 0
      return [p,pstar,info,it+1]
    p0 =p1
    fp0=fp1
    p1 = p2
    fp1 = f(p2)
    p[it+1] =p0
  pstar = p2
  info=1
  return [p,pstar,info,it+1]
        
driver()
