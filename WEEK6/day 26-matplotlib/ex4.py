import matplotlib.pyplot as plt 
import numpy as np 

x=np.array([10,15,20,25,30.35])
y=np.array([2,10,6,4,5,3])

plt.hist(y,bins=6)
plt.show()