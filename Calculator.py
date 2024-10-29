from tkinter import *


def button_press(num):
    global equation_text
    
    equation_text = equation_text + str(num)

    equation_label.set(equation_text)

def equals():
    try:
        global equation_text 

        total = str(eval(equation_text))

        equation_label.set(total)

        equation_text = total

    except SyntaxError:
        equation_label.set("SyntaxError")

        equation_text =""

    except ZeroDivisionError:
        equation_label.set("ZeroDivisionError")

        equation_text =""

def clear():

    global equation_text
    
    equation_label.set("")

    equation_text=""

root = Tk()
root.title("Calculator App")
root.geometry("500x500")

equation_text = ""

equation_label = StringVar()

label = Label(root, textvariable=equation_label,font=('consolas',20),bg="white",width=24,height=2)
label.pack()

frame =Frame(root)
frame.pack()

Button1 = Button(frame,text=1,height=4,width=9,font=35,
                 command=lambda:button_press(1))
Button1.grid(row=0,column=0)

Button2 = Button(frame,text=2,height=4,width=9,font=35,
                 command=lambda:button_press(2))
Button2.grid(row=0,column=1)

Button3 = Button(frame,text=3,height=4,width=9,font=35,
                 command=lambda:button_press(3))
Button3.grid(row=0,column=2)

Button4 = Button(frame,text=4,height=4,width=9,font=35,
                 command=lambda:button_press(4))
Button4.grid(row=1,column=0)

Button5 = Button(frame,text=5,height=4,width=9,font=35,
                 command=lambda:button_press(5))
Button5.grid(row=1,column=1)

Button6 = Button(frame,text=6,height=4,width=9,font=35,
                 command=lambda:button_press(6))
Button6.grid(row=1,column=2)

Button7 = Button(frame,text=7,height=4,width=9,font=35,
                 command=lambda:button_press(7))
Button7.grid(row=2,column=0)

Button8 = Button(frame,text=8,height=4,width=9,font=35,
                 command=lambda:button_press(8))
Button8.grid(row=2,column=1)

Button9 = Button(frame,text=9,height=4,width=9,font=35,
                 command=lambda:button_press(9))
Button9.grid(row=2,column=2)

Button0= Button(frame,text=0,height=4,width=9,font=35,
                 command=lambda:button_press(0))
Button0.grid(row=3,column=1)

decimal = Button(frame,text='.',height=4,width=9,font=35,
                 command=lambda:button_press('.'))
decimal.grid(row=3,column=0)

Button_equal = Button(frame,text="=",height=4,width=9,font=35,
                 command=equals)
Button_equal.grid(row=3,column=2)

plus = Button(frame,text="+",height=4,width=9,font=35,
                 command=lambda:button_press("+"))
plus.grid(row=0,column=3)

subtract = Button(frame,text="-",height=4,width=9,font=35,
                 command=lambda:button_press("-"))
subtract.grid(row=1,column=3)

multiple = Button(frame,text="*",height=4,width=9,font=35,
                 command=lambda:button_press("*"))
multiple.grid(row=2,column=3)

division = Button(frame,text="/",height=4,width=9,font=35,
                 command=lambda:button_press("/"))
division.grid(row=3,column=3)

clear = Button(root,text="clear",height=4,width=9,font=35,
                 command=clear)
clear.pack()




root.mainloop()

