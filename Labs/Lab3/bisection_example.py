# import libraries
import numpy as np

def driver():

# use routines    
    f = lambda x: np.sin(x)
    a = 0.5
    b = 3*np.pi/4

#    1) For the first and last intervals there was sucess
#    this makes sence because the intervals contain x=1 which is a root.
#    For the second interval the roots are at x = and x =0
#    since x =1 is outside the interval it won't pick up the x =1 interval and
#    when x =0 f(a)*f(b) won't change signs it will just be zero so it can't pick
#    up the root


#    2) No because the last root for sin(x) is at x =0 and it didn't give an error
#    message, but we were expecting b) to give a root 1 since it's in the interval, but it gave
#    the root as zero and an error message it could be due to the squared on the (x-1)


    tol = 1e-7

    [astar,ier] = bisection(f,a,b,tol)
    print('the approximate root is',astar)
    print('the error message reads:',ier)
    print('f(astar) =', f(astar))




# define routines
def bisection(f,a,b,tol):
    
#    Inputs:
#     f,a,b       - function and endpoints of initial interval
#      tol  - bisection stops when interval length < tol

#    Returns:
#      astar - approximation of root
#      ier   - error message
#            - ier = 1 => Failed
#            - ier = 0 == success

#     first verify there is a root we can find in the interval 

    fa = f(a)
    fb = f(b);
    if (fa*fb>0):
       ier = 1
       astar = a
       return [astar, ier]

#   verify end points are not a root 
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
      
    astar = d
    ier = 0
    return [astar, ier]
      
driver()               

