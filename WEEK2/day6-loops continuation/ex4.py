for i in range (1,5):
    print(f"enter marks for student #{i}")
    total=0
    for j in range(1,4):
        marks=int(input(f"enter marks for test#- {j}-"))
        total=total+marks
    average_marks=total/3
    print(f"average marks={average_marks:.2f}")