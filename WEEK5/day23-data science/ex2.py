import numpy as np
marks=np.array([[45,56,78,65,90],[41,54,63,77,18],[69,81,57,67,48]])
#print(marks.ndim)#prints the number of dimensions
#print(marks.sum())
#print(marks.sum(axis=0))
#print(marks.sum(axis=1))

#print(np.sqrt(marks))

#print(marks.flatten())#it turns a two dimensional list into one

numbers=np.arange(1,11)
numbers2=np.arange(11,21)
numbers3=np.add(numbers,numbers2)
print(numbers3)
print(numbers*2)
print(marks[[0,2],3])#slicing and indexing in numpy


