import scipy.special as special 
import numpy as np
import matplotlib.pyplot as plt

alpha = 0.138 * 10**-6
t = 3600*60*24

x = np.linspace(0, 2, 100)
#bound = np.array([i/(2*np.sqrt(t*alpha)) for i in x])

#tempF = []
#for i in bound:
    #temp, _ = integrate.quad(lambda s: np.exp(-s**2), 0 ,i)
    #tempF.append(temp)

f =  (15/35 - special.erf(x/(2*np.sqrt(alpha*t))))                              


plt.plot(x,f)
plt.show()

