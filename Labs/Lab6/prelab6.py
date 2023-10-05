import numpy as np


f = lambda x: np.cos(x)
h = 0.01*2.**(-np.arange(0,10))
x = np.pi/2
fp = (f(x+h)-f(x))/h
print(fp)
fp1 = (f(x+h)-f(x-h))/(2*h)
print(fp1)


#Both techniques converge linaerly 
