#graphical user interface
#using tkinter and widgets
from tkinter import *

#creating a main window
root = Tk()

root.title ("My First GUI program")
root.geometry("500x500")# specifies the size of the window (width x height)

lblMessage = Label(root, text="Welcome to python GUI programming",borderwidth=2, relief="solid")
lblMessage.pack(ipadx=20,ipady=10,padx=20,pady=20)# pack is used to add the widget to the window
#ipadx and ipady are used to add padding inside the widget
#padx and pady are used to add padding outside the widget
lblMessage2 = Label(root, text="using the tkinter module")
lblMessage2.pack()

txtName = Entry(root)
txtName.pack()

btnClickMe = Button(root, text="Click here")
btnClickMe.pack()
                    
root.mainloop()# for one to keep it running