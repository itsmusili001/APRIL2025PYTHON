# two dimensional list- is a list in another list consisting of rows and columns
marks=[[70,60,80],
[83,74,95],
[57,76,87],
[62,78,90]]
#print(marks[1][2]) 
#print(marks[3][2])

#average of all marks
sum=0
for i in range(0,4):
    for j in range(0,3):
        sum=sum+marks[i][j]
print("sum of all marks is: " + str(sum))   
average=sum/12
print("average of all marks is: " + str(average))


#alternatively, 
total=0
for row in marks:
    for mark in row:
        total+=mark
print(f"the total marks is: {total}")
print(f"the average marks is: {total/12}")

#average for each student
for i in range(0,4):
    sum=0
    for j in range(0,3):
        sum=sum+marks[i][j]
    print("average of student " + str(i) + " is: " + str(sum/3))

#average for each subject
for i in range(0,3):
    sum=0
    for j in range(0,4):
        sum=sum+marks[j][i]
    print("average of subject " + str(i) + " is: " + str(sum/4))
    

