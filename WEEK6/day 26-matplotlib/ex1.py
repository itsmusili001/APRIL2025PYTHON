import matplotlib.pyplot as plt
import numpy as np

xpoint=np.array([0,2,4,6,8])
ypoint=np.array([3,7,0,12,14])

xpoint1=np.array([1,3,5,7,9])
ypoint1=np.array([6,10,3,15,17])

plt.plot(xpoint,ypoint,marker="o")
plt.plot(xpoint1,ypoint1,'*:g')# the marker is a star the colour is green and line is dotted
plt.show()