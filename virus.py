from tkinter import * 
from tkinter import messagebox

root = Tk()
root.geometry("200X200")

def msg():
    messagebox.showwarning("Alert","Stop! Virus Found.")

button = Button(root, text= "Scan for virus", command=msg)
button.palce(x=40, y=80)

root.mainloop()