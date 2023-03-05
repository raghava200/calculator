from tkinter import *
c=Tk()
c.title("CALCULATOR")
e=Entry(c,width=40)
e.grid(row=0,column=0,columnspan=3)
def button_click(n):
    current=e.get()
    e.delete(0,END)
    e.insert(0,str(current)+str(n))
def button_clear():
    e.delete(0,END)
def button_add():
    f=e.get()
    global f1
    global math 
    math="add"
    f1=int(f)
    e.delete(0,END)
def button_equal():
    second_number=e.get()
    e.delete(0,END)
    if math=="add":
         e.insert(0,f1 + int(second_number))
    elif math=="sub":
         e.insert(0,f1 - int(second_number))
    elif math=="mul":
         e.insert(0,f1 * int(second_number))
    else:
         e.insert(0,f1 / int(second_number))     
def button_sub():
    f=e.get()
    global f1
    global math 
    math="sub"
    f1=int(f)
    e.delete(0,END)
def button_mul():
    f=e.get()
    global f1
    global math 
    math="mul"
    f1=int(f)
    e.delete(0,END)
def button_div():
    f=e.get()
    global f1
    global math 
    math="div"
    f1=int(f)
    e.delete(0,END)
button_1=Button(c,text="1",padx=40,pady=20,command=lambda : button_click(1)).grid(row=3,column=0)
button_2=Button(c,text="2",padx=40,pady=20,command=lambda:button_click(2)).grid(row=3,column=1)
button_3=Button(c,text="3",padx=40,pady=20,command=lambda:button_click(3)).grid(row=3,column=2)
button_4=Button(c,text="4",padx=40,pady=20,command=lambda:button_click(4)).grid(row=2,column=0)
button_5=Button(c,text="5",padx=40,pady=20,command=lambda:button_click(5)).grid(row=2,column=1)
button_6=Button(c,text="6",padx=40,pady=20,command=lambda:button_click(6)).grid(row=2,column=2)
button_7=Button(c,text="7",padx=40,pady=20,command=lambda:button_click(7)).grid(row=1,column=0)
button_8=Button(c,text="8",padx=40,pady=20,command=lambda:button_click(8)).grid(row=1,column=1)
button_9=Button(c,text="9",padx=40,pady=20,command=lambda:button_click(9)).grid(row=1,column=2)
button_0=Button(c,text="0",padx=40,pady=20,command=lambda:button_click(0)).grid(row=4,column=0)
button_add=Button(c,text="+",padx=40,pady=20,command=button_add).grid(row=5,column=0)
button_sub=Button(c,text="-",padx=40,pady=20,command=button_sub).grid(row=6,column=0)
button_mul=Button(c,text="*",padx=40,pady=20,command=button_mul).grid(row=6,column=1)
button_div=Button(c,text="/",padx=40,pady=20,command=button_div).grid(row=6,column=2)
button_clear=Button(c,text="clear",padx=80,pady=20,command=button_clear).grid(row=4,column=1,columnspan=2)
button_equal=Button(c,text="=",padx=80,pady=20,command=button_equal).grid(row=5,column=1,columnspan=2)
c.mainloop()