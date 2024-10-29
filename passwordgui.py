import random
import string
from tkinter import *

def selection():
    selection = choice.get()

def callback():
    password = passegn()
    isum.config(text=password)


    


root=Tk()
root.title("Password generator")
root.geometry("400x400")

title = StringVar()
label = Label(root,textvariable=title)
label.pack()
title.set("password length")


choice = IntVar()
R1=Radiobutton(root,text="Poor",variable=choice,value=1,command=selection).pack(anchor=CENTER)
R2=Radiobutton(root,text="Average",variable=choice,value=2,command=selection).pack(anchor=CENTER)
R3=Radiobutton(root,text="Advanced",variable=choice,value=3,command=selection).pack(anchor=CENTER)

lenlabel = StringVar()
lenlabel.set("Password Length:")
label = Label(root,textvariable=lenlabel).pack()

val = IntVar()
spinglen = Spinbox(root,from_=8,to_=20,textvariable=val)
spinglen.pack()

button1 =Button(root,text="Generate Password",height=2,bd=5,command=callback,pady=3)
button1.pack()


isum = Label(root,text="")
isum.pack(side=BOTTOM)

#logic

poor = string.ascii_uppercase + string.ascii_lowercase
average = string.ascii_uppercase + string.ascii_lowercase + string.digits
symbols = "@#$%&)({}[]"

advance = poor + average + symbols

def passegn():
    if choice.get() == 1:
        return ''.join(random.sample(poor,val.get()))
    elif choice.get() == 2:
        return ''.join(random.sample(average,val.get()))
    elif choice.get() == 3:
        return ''.join(random.sample(advance,val.get()))



root.mainloop()