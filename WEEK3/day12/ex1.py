# Multiple choice questions related to my hobby
qns= ["What is your favorite hobby? \nA. Reading \nB. Traveling \nC. Cooking", "what is your favorite color? \nA. Blue \nB. Green \nC. Red", 
"What is your favorite food? \nA. Pizza \nB. Sushi \nC. Pasta", "what is your favorite movie? \nA. Inception \nB. Titanic \nC. The Matrix", 
"what is your favorite sport? \nA. Soccer \nB. Basketball \nC. Tennis"]

CorrectAns = ["A", "B", "B", "A", "A"]
points = 0
for counter in range(len(qns)):
    print(qns[counter])
    givenAns=input()
    while givenAns.upper()!="A" and givenAns.upper()!="B" and givenAns.upper()!="C":
        print("Please enter a valid answer (A, B, or C)")
        givenAns=input()
    if givenAns.upper()==CorrectAns[counter]:
            print("Correct")
            points += 1
    else:
        print("Incorrect")
        print(f"The correct answer is {CorrectAns[counter]}")
print(f"You scored {points} out of {len(qns)}")

