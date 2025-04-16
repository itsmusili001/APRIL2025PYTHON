marks=[]
for counter in range(1,6):
    mark=int(input(f"enter mark {counter}-"))
    marks.append(mark)

highest=max(marks)
lowest=min(marks)
average_marks=sum(marks)/5

print(f"marks entered= {marks}")
print(f"highest mark= {highest}")
print(f"lowest mark= {lowest}")
print(f"average marks entered {average_marks}")
