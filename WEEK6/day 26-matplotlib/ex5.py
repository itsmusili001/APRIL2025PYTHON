import matplotlib.pyplot as plt 
import numpy as np 

y=np.array([15,45,20,15,25])
months = ['jan', 'feb', 'mar', 'apr', 'may']

plt.pie(y)
plt.legend(months)
#plt.pie(y, labels=months)
plt.show()
