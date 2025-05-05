#framework: tkinter
from tkinter import *

root = Tk()

root.title ("My First GUI program")
root.geometry("500x500")

topFrame = Frame(root)
bottomFrame = Frame(root)


lblMessage = Label(topFrame, text="Welcome to python GUI programming",borderwidth=2, relief="solid")
lblMessage.pack(ipadx=20,ipady=10,padx=20,pady=20,side="top")

lblMessage2 = Label(topFrame, text="using the tkinter module")
lblMessage2.pack(side="right")

txtName = Entry(bottomFrame)
txtName.pack()

btnClickMe = Button(bottomFrame, text="Click here")
btnClickMe.pack()
topFrame.pack(side="top")
bottomFrame.pack(side="top")

chkTickMe = Checkbutton(bottomFrame, text=" on/off")
chkTickMe.pack()
                    
root.mainloop()