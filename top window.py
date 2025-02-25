from tkinter import *

root = Tk()
root.geometry('400x300')
root.title('main')

def topwin():
    top = Toplevel()
    top.geometry('180x100')
    top.title ('top level')
    12 = Label(top, text = 'This is top level window')
    12.pack()

    top.mainloop 

l = Label(root, text = 'This is the root window')
btn = Button(root, text = 'Click here to open another window', command = topwin)

l.pack()
btn.pack()