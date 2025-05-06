from tkinter import *
from tkinter import messagebox
root=Tk()

root.title("calculating miles per gallon")
root.geometry("400x400")


def calculate_MPG():
    gallons_of_gas=float(txtgallons.get())
    miles_driven=float(txtmiles.get())
    mpg=miles_driven/gallons_of_gas
    result=f"calculated MPG: {mpg:.2f}"
    messagebox.showinfo("caluculated mpg:",result)


lblGallon=Label(root, text="Gallons of Gas held:")
lblGallon.pack()
txtgallons = Entry(root)
txtgallons.pack()

lblMiles=Label(root, text="Miles Driven on full tank:")
lblMiles.pack()
txtmiles = Entry(root)
txtmiles.pack()


btncalc=Button(root, text="Calculate MPG", command=calculate_MPG)
btncalc.pack()



root.mainloop()