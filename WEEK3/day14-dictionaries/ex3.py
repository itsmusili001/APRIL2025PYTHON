rooms={"CS101":"3004",
"CS102":"4501",
"CS103":"6755",
"NT110":"1244",
"CM241":"1411"}

instructors={"CS101":"Haynes",
"CS102":"Alvarado", 
"CS103":"Rich",
"NT110":"Burke",
"CM241":"Lee"}

meetingTimes={"CS101":"8:00 a.m.", 
"CS102":"9:00 a.m.",
"CS103":"10:00 a.m.",
"NT110":"11:00 a.m.",
"CM241":"1:00 p.m."}

userInput=input("Enter the course number: ")
if userInput not in rooms:
    print("course number not found.")
else:
    print(f"Room number: {rooms[userInput]}")
    print(f"instructor: {instructors[userInput]}")
    print(f"meeting time: {meetingTimes[userInput]}")
