from tkinter import *
from tkinter import messagebox
def displayMessage():
    messagebox.showinfo("welcome", "this is python GUI programming")


root = Tk()

root.geometry("500x500")
btnClick = Button(root, text="Click here",command=displayMessage)
btnClick.pack()

btnQuit = Button(root, text="Quit",command=root.quit)
btnQuit.pack()


root.mainloop()