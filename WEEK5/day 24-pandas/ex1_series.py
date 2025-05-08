#a series is one dimension eg only column or only row
#a data frame has like rows and columns
import numpy as numpy
import pandas as pd

hundreds=pd.Series(100,range(10))
grades = pd.Series([87,100,94])
#print(grades[0])
# print(grades.count())
#print(grades.mean())
#print(grades.max())
#print(grades.min())
#print(grades.std())
#print(grades.var())
#print(grades.describe())#gives a summary of everything
grades2 = pd.Series([90,77,94],index=["Tom","Mary","Joseph"])
#print(grades2)
#print(grades2["Tom"])
dictGrade={"java":87,"python":93,"c#":79}
grades3=pd.Series(dictGrade)
print(grades3)
