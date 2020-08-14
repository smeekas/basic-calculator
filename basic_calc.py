from tkinter import *
import math
from math import factorial,sqrt
root=Tk()
root.configure(bg="white")
root.title("calculator")
first=None
math=None
def numbers(num):
    global inputs
    inputs.insert(END,str(num))

def clr():
    global inputs
    inputs.delete(0,END)
def back():
    global  inputs
    data = inputs.get()

    if data=="cant / by 0":
        inputs.delete(0,END)
    elif data.__contains__("e"):
        inputs.delete(0, END)
    else:
        data=int(data)
        data=str(data//10)

        inputs.delete(0,END)
        inputs.insert(0,data)


def add():
    global inputs
    global first
    first=inputs.get()
    global math
    math="+"
    inputs.delete(0,END)

def subtract():
    global inputs
    global first
    global math
    math="-"
    first = inputs.get()
    inputs.delete(0, END)

def multiply():
    global inputs
    global first
    global math
    math = "*"
    first=inputs.get()
    inputs.delete(0,END)

def division():
    global inputs
    global first
    global math
    math = "/"
    first = inputs.get()
    inputs.delete(0, END)

def average():
    global inputs
    global first
    global math
    math="%"
    first=inputs.get()
    inputs.delete(0,END)
def square():
    global inputs
    global first
    first=float(inputs.get())
    inputs.delete(0,END)
    inputs.insert(0,str(first**2))
def cube():
    global inputs
    global first
    num = float(inputs.get())
    inputs.delete(0, END)
    inputs.insert(0, str(num ** 3))
def sqrut():
    global inputs
    global first
    num = float(inputs.get())
    inputs.delete(0, END)
    inputs.insert(0, str(sqrt(num)))
def inverse():
    global inputs
    global first
    first = float(inputs.get())
    inputs.delete(0, END)
    inputs.insert(0, str(1/first))
def fact():
    global inputs
    global first
    global math

    first = float(inputs.get())
    first_fact=factorial(first)
    inputs.delete(0, END)
    if first_fact>100000000:
        inputs.insert(0,"{:e}".format(first_fact))
    else:
        inputs.insert(0, str(factorial(first)))
def equals():
    global inputs
    second=inputs.get()
    print(second)
    inputs.delete(0,END)

    if math=="+":
        inputs.insert(0,str(float(first)+float(second)))
    elif math=="-":
        inputs.insert(0, str(float(first) - float(second)))
    elif math=="*":
        inputs.insert(0, str(float(first) * float(second)))
    elif math=="/":
        try:
            inputs.insert(0, str(round(float(first) / float(second),4)))
        except:
            inputs.insert(0,"cant / by 0")

    elif math=="%":
        inputs.insert(0,str(float(first)*float(second)/100))


inputs=Entry(root,width=25,font=("Arial",22))
inputs.grid(row=0,column=0,columnspan=6,sticky="news")


btn_square=Button(root,text="x²",padx=45,pady=20,command=square)
btn_cube=Button(root,text="x³",padx=45,pady=20,command=cube)
btn_inverse=Button(root,text="1/x",padx=41,pady=20,command=inverse)
btn_sqrt=Button(root,padx=47,text="√x",pady=20,command=sqrut)
btn_fact=Button(root,padx=49,text="n!",pady=20,command=fact)




btn_7=Button(root,text="7",padx=47,pady=20,command=lambda:numbers(7))
btn_8=Button(root,text="8",padx=47,pady=20,command=lambda:numbers(8))
btn_9=Button(root,text="9",padx=47,pady=20,command=lambda:numbers(9))
btn_clear=Button(root,padx=47,text="CE",pady=20,command=clr)
btn_back=Button(root,padx=46,text="<=",pady=20,command=back)

btn_4=Button(root,text="4",padx=47,pady=20,command=lambda:numbers(4))
btn_5=Button(root,text="5",padx=47,pady=20,command=lambda:numbers(5))
btn_6=Button(root,text="6",padx=47,pady=20,command=lambda:numbers(6))
btn_add=Button(root,text="+",padx=50,pady=20,command=add)
btn_sub=Button(root,text="-",padx=53,pady=20,command=subtract)

btn_1=Button(root,text="1",padx=47,pady=20,command=lambda:numbers(1))
btn_2=Button(root,text="2",padx=47,pady=20,command=lambda:numbers(2))
btn_3=Button(root,text="3",padx=47,pady=20,command=lambda:numbers(3))
btn_mul=Button(root,text="*",padx=52,pady=20,command=multiply)
btn_div=Button(root,text="÷",padx=51,pady=20,command=division)


btn_0=Button(root,text="0",padx=47,pady=20,command=lambda:numbers(0))
btn_dec=Button(root,text=".",padx=49,pady=20,command=lambda:numbers("."))
btn_avg=Button(root,text="%",padx=45,pady=20,command=average)
btn_equals=Button(root,text="=",padx=111,pady=20,command=equals)

btn_square.grid(row=1,column=1)
btn_cube.grid(row=1,column=2)
btn_inverse.grid(row=1,column=3)
btn_sqrt.grid(row=1,column=4)
btn_fact.grid(row=1,column=5)

btn_7.grid(row=2,column=1)
btn_8.grid(row=2,column=2)
btn_9.grid(row=2,column=3)
btn_clear.grid(row=2,column=4)
btn_back.grid(row=2,column=5)

btn_4.grid(row=3,column=1)
btn_5.grid(row=3,column=2)
btn_6.grid(row=3,column=3)
btn_add.grid(row=3,column=4)
btn_sub.grid(row=3,column=5)

btn_1.grid(row=4,column=1)
btn_2.grid(row=4,column=2)
btn_3.grid(row=4,column=3)
btn_mul.grid(row=4,column=4)
btn_div.grid(row=4,column=5)

btn_0.grid(row=5,column=1)
btn_dec.grid(row=5,column=2)
btn_avg.grid(row=5,column=3)
btn_equals.grid(row=5,column=4,columnspan=2)

root.mainloop()