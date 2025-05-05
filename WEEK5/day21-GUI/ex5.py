from tkinter import *
from tkinter import messagebox
def convert_to_celsius():
        fahrenheit = float(txtfar.get())
        celsius = (fahrenheit - 32) * 5 / 9
        result=f"Temperature in Celsius: {celsius:.2f}°C"
        messagebox.showinfo("converted temp:",result)
    
root = Tk()
root.title("Fahrenheit to Celsius Converter")

lblfar=Label(root, text="Enter Temperature in Fahrenheit:")
lblfar.pack()
txtfar = Entry(root)
txtfar.pack()

btnconvert=Button(root, text="Convert", command=convert_to_celsius)
btnconvert.pack()


root.mainloop()
