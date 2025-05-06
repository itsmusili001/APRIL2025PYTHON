#1.question label ,2.answer text box,3.message box to output correct or incorrect,4.a button to generate a new question 
# 5. button to check if answer is correct

from random import randint
from tkinter import *
from tkinter import messagebox

countries= ["Algeria","Angola","Benin","Botswana","Burundi","Burkina Faso","Cameroon",
"Cape Verde","Central African Republic","Chad","Comoros","Cote d’Ivoire","DR Congo","Djibouti",
"Egypt","Equatorial Guinea","Eritrea","Ethiopia","Gabon","Gambia","Ghana","Guinea",
"Guinea-Bissau","Kenya","Lesotho","Liberia","Libya","Madagascar","Malawi","Mali","Mauritania",
"Mauritius","Morocco","Mozambique","Namibia","Niger","Nigeria","Republic of the Congo","Réunion",
"Rwanda","São Tomé and Principe","Senegal","Seychelles","Sierra Leone","Somalia","South Africa","South Sudan",
"Sudan","Swaziland","Tanzania","Togo","Tunisia","Uganda","Zambia","Zimbabwe"]

cities= ["Algiers","Luanda","Porto-Novo","Gaborone","Bujumbura","Ouagadougou","Yaoundé",
"Praia","Bangui","N’Djamena","Moroni","Yamoussoukro","Kinshasa","Djibouti City",
"Cairo","Malabo","Asmara", "Addis Ababa","Libreville","Banjul","Accra","Conakry",
"Bissau","Nairobi","Maseru","Monrovia","Tripoli","Antananarivo","Lilongwe","Bamako","Nouakchott", 
"Port Louis","Rabat","Maputo","Windhoek","Niamey", "Abuja","Brazzaville","Saint-Denis",
"Kigali","Sao Tome","Dakar","Victoria","Freetown","Mogadishu","Pretoria","Juba",
"Khartoum","Mbabane","Dodoma","Lome","Tunis","Kampala","Lusaka","Harare"]


root = Tk()
question=StringVar()
root.title("Country Capitals Quiz")
root.geometry("500x500")

lblQuestion=Label(root,textvariable=question)
lblQuestion.grid(row=0,column=0)

lblAnswer=Label(root,text="enter your answer here")
lblAnswer.grid(row=1, column=0)

txtAnswer=Entry(root)
txtAnswer.grid(row=1,column=1)

def generate_question():
    rand = randint(0, len(countries) - 1)
    question.set(f"What is the capital of {countries[rand]}?")
    lblQuestion.current_random_country = rand

def check_answer():
    user_answer = txtAnswer.get()
    correct_answer = cities[lblQuestion.current_random_country]
    if user_answer.upper() == correct_answer.upper():
        messagebox.showinfo("Result", "Correct!")
    else:
        messagebox.showinfo("Result", f"Incorrect! The correct answer is {correct_answer}.")

btnGenerateQuestion = Button(root, text="Generate another question", command=generate_question)
btnGenerateQuestion.grid(row=2, column=0 ,pady=10)

btnCheckAnswer = Button(root, text="Check Answer", command=check_answer)
btnCheckAnswer.grid(row=2, column=1 ,pady=10)


generate_question()


root.mainloop()

