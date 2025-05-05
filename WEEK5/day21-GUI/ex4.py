from tkinter import *
from tkinter import messagebox
root = Tk()

root.title("Rectangle Area")
root.geometry("500x500")

def getArea():
    side1=float(txtSide1.get())
    side2=float(txtSide2.get())
    area = side1*side2
    Message=f"the area is:{area:.2f} sq units"
    messagebox.showinfo("rectangle area",Message)


lblSide1= Label(root, text="enter side 1")
lblSide1.pack()
txtSide1=Entry(root)
txtSide1.pack()

lblSide2= Label(root, text="enter side 2")
lblSide2.pack()
txtSide2=Entry(root)
txtSide2.pack()

btncalculateArea = Button(root, text="Calculate area",command=getArea)
btncalculateArea.pack()

btnQuit = Button(root, text="Quit",command=root.quit)
btnQuit.pack()


root.mainloop()