from tkinter import *
win = Tk()
#win.geometry("300x400")
win.title("Calculator")
win.config(bg="#000035")
win.resizable(False,False)

def btn_click(item):
    global expression
    expression = expression + str(item)
    e.set(expression)

def btn_clear(): 
    global expression 
    expression = "" 
    e.set("")
 
def btn_equal():
    global expression
    result = str(eval(expression))
    e.set(result)
    expression = ""

expression = ""
e = StringVar()
input_frame = Frame(win,width=250,height=50,bg="#000027")
input_frame.pack(side=TOP)


input = Entry(input_frame,text="", width=300,font=24, borderwidth=5,textvariable=e,justify=RIGHT)
input.place(x=0,y=0,width=250,height=50)

btns_frame = Frame(win, bg="#000020")
btns_frame.pack()

button_1 = Button(btns_frame, text="1", padx=20, pady=10, command=lambda: btn_click(1))
button_2 = Button(btns_frame, text="2", padx=20, pady=10, command=lambda: btn_click(2))
button_3 = Button(btns_frame, text="3", padx=20, pady=10, command=lambda: btn_click(3))
button_4 = Button(btns_frame, text="4", padx=20, pady=10, command=lambda: btn_click(4))
button_5 = Button(btns_frame, text="5", padx=20, pady=10, command=lambda: btn_click(5))
button_6 = Button(btns_frame, text="6", padx=20, pady=10, command=lambda: btn_click(6))
button_7 = Button(btns_frame, text="7", padx=20, pady=10, command=lambda: btn_click(7))
button_8 = Button(btns_frame, text="8", padx=20, pady=10, command=lambda: btn_click(8))
button_9 = Button(btns_frame, text="9", padx=20, pady=10, command=lambda: btn_click(9))
button_0 = Button(btns_frame, text="0", padx=20, pady=10, command=lambda: btn_click(0))
button_dot = Button(btns_frame, text=".", padx=20, pady=10, command=lambda: btn_click("."))
button_add = Button(btns_frame, text="+", padx=19, pady=36, command=lambda: btn_click("+"))
button_sub = Button(btns_frame, text="-", padx=20, pady=10, command=lambda: btn_click("-"))
button_equal = Button(btns_frame, text="=", padx=19, pady=36,bg="#3333ff", command=lambda: btn_equal())
button_clear = Button(btns_frame, text="Clear", padx=42, pady=10, command=lambda: btn_clear())
button_multiply= Button(btns_frame, text="*", padx=20 , pady=10,command=lambda: btn_click("*"))
button_divide= Button(btns_frame, text="÷", padx=20 , pady=10,command=lambda: btn_click("/"))
button_1.grid(row=3, column=0,padx=5,pady=5)
button_2.grid(row=3, column=1,padx=5,pady=5) 
button_3.grid(row=3, column=2,padx=5,pady=5)
button_4.grid(row=2, column=0,padx=5,pady=5) 
button_5.grid(row=2, column=1,padx=5,pady=5) 
button_6.grid(row=2, column=2,padx=5,pady=5)
button_7.grid(row=1, column=0,padx=5,pady=5) 
button_8.grid(row=1, column=1,padx=5,pady=5) 
button_9.grid(row=1, column=2,padx=5,pady=5)
button_0.grid(row=4, column=0,padx=5,pady=5)
button_clear.grid(row=5, column=1, columnspan=2,padx=5,pady=5)
button_add.grid(row=1, column=3, rowspan=2,padx=5,pady=5)
button_equal.grid(row=4, column=3,rowspan=2,padx=5,pady=5)
button_multiply.grid(row=4,column=1,padx=5,pady=5)
button_divide.grid(row=4,column=2,padx=5,pady=5)
button_sub.grid(row=3,column=3,padx=5,pady=5)
button_dot.grid(row=5,column=0,padx=5,pady=5) 
win.mainloop()
