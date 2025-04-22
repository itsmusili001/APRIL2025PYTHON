qns=["when did kenya gain independence? \n A. 1963 \n B. 2025","What is your favpurite hobby? \n A. python programming \n B. reading "]
CorrectAns=["A","A"]
points=0
for counter in range(len(qns)):
    print(qns[counter])
    givenAns=input()
    while givenAns.upper() != givenAns!="A"and givenAns.upper!="B":
        print("Please enter a valid answer (A or B)")
        givenAns=input()

    if givenAns.upper()==CorrectAns[counter]:
        print("Correct")
        points += 1
    else:
        print("Incorrect")
        print(CorrectAns[counter] + " is the correct answer")
print(f"You scored {points} out of {len(qns)}")
            
