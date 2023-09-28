# import libraries
import numpy as np
import scipy.special as special
        
def driver():
#f = lambda x: (x-2)**3
#fp = lambda x: 3*(x-2)**2
#p0 = 1.2
  

  f = lambda x: np.exp(x**2+7*x-30)-1
  fp = lambda x:2*x+7*np.exp(x**2+7*x-30)
  p0 = 4.5
  a = 2
  b = 4.5

  Nmax = 100
  tol = 1.e-13

  (p,pstar,info,it) = newton(f,fp,p0,tol, Nmax)
  print('the approximate root is', '%16.16e' % pstar)
  print('the error message reads:', '%d' % info)
  print('Number of iterations:', '%d' % it)


def newton(f,fp,p0,tol,Nmax):
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
  p[0] = p0
  c = (a+b)/2
  if a<c-(f(c)/fp(c))<b:
    for it in range(Nmax):
        p1 = p0-f(p0)/fp(p0)
        p[it+1] = p1
        if (abs(p1-p0) < tol):
            pstar = p1
            info = 0
            return [p,pstar,info,it]
        p0 = p1
  else:
    fa = f(a)
    fb = f(b);
    if (fa*fb>0):
       ier = 1
       astar = a
       return [astar, ier]
    if (fa == 0):
      astar = a
      ier =0
      return [astar, ier]

    if (fb ==0):
      astar = b
      ier = 0
      return [astar, ier]

    count = 0
    d = 0.5*(a+b)
    while (abs(d-a)> tol):
      fd = f(d)
      if (fd ==0):
        astar = d
        ier = 0
        return [astar, ier]
      if (fa*fd<0):
         b = d
      else: 
        a = d
        fa = fd
      d = 0.5*(a+b)
      count = count +1
#      print('abs(d-a) = ', abs(d-a))
    print('count is', count) 
      
    astar = d
    ier = 0
    return [astar, ier]

        
driver()
