import tkinter
from tkinter import *
import re

root = Tk()
root.geometry('300x415')
root.title("Mbula Layola")
rootlabel = Label(root, text='Standard Calculator', width='300', fg='white', bg='Dark blue', font=("Times",15,'bold'))
rootlabel.pack(side=TOP)
root.config(background='Dark blue')

entryNum = StringVar()
operator = ""

entry1 = Entry(root, font=("Times",18), textvar=entryNum, bd=1, bg='white')
entry1.pack(ipadx=30, pady=12, ipady=16)

def btnClick(number):
     global operator
     operator=operator+str(number)
     entryNum.set(operator)
     

def equlbut():
     global operator
     add=str(eval(operator))
     entryNum.set(add)
     operator=''
     
     
def equlbut():
     global operator
     sub=str(eval(operator))
     entryNum.set(sub)
     operator=''  
     
        
def equlbut():
     global operator
     mul=str(eval(operator))
     entryNum.set(mul)
     operator=''
     
     
def equlbut():
     global operator
     div=str(eval(operator))
     entryNum.set(div)
     operator=''    


def clrbut():
     entryNum.set('')


# BUTTONS
btn1 = Button(root, padx=22, pady=14, bg='white', command=lambda:btnClick(1), text="1", font=("Times",10, 'bold'))
btn1.place(x=35,y=230)
btn2 = Button(root, padx=22, pady=14, bg='white', command=lambda:btnClick(2), text="2", font=("Times",10, 'bold'))
btn2.place(x=100,y=230)
btn3 = Button(root, padx=22, pady=14, bg='white', command=lambda:btnClick(3), text="3", font=("Times",10, 'bold'))
btn3.place(x=165,y=230)

btn4 = Button(root, padx=22, pady=14, bg='white', command=lambda:btnClick(4), text="4", font=("Times",10, 'bold'))
btn4.place(x=35,y=175)
btn5 = Button(root, padx=22, pady=14, bg='white', command=lambda:btnClick(5), text="5", font=("Times",10, 'bold'))
btn5.place(x=100,y=175)
btn6 = Button(root, padx=22, pady=14, bg='white', command=lambda:btnClick(6), text="6", font=("Times",10, 'bold'))
btn6.place(x=165,y=175)

btn7 = Button(root, padx=22, pady=14, bg='white', command=lambda:btnClick(7), text="7", font=("Times",10, 'bold'))
btn7.place(x=35, y=120)
btn8 = Button(root, padx=22, pady=14, bg='white', command=lambda:btnClick(8), text="8", font=("Times",10, 'bold'))
btn8.place(x=100,y=120)
btn9 = Button(root, padx=22, pady=14, bg='white', command=lambda:btnClick(9), text="9", font=("Times",10, 'bold'))
btn9.place(x=165,y=120)

btn0 = Button(root, padx=22, pady=14, bg='white', command=lambda:btnClick(0), text="0", font=("Times",10, 'bold'))
btn0.place(x=100,y=286)
btndot = Button(root, padx=24, pady=14, bg='white', command=lambda:btnClick("."), text=".")
btndot.place(x=165,y=286)
btnClear = Button(root, padx=18, pady=14, bg='white', text="CE", command=clrbut,font=("Times",10, 'bold'))
btnClear.place(x=35,y=286)

# ADD_SUB_MUL_DIV
btnAdd = Button(root, padx=10, pady=14, bg='white',command=lambda:btnClick("+"), text="+",font=("Times",10, 'bold'))
btnAdd.place(x=230,y=120)

btnSub = Button(root, padx=12, pady=14, bg='white',command=lambda:btnClick("-"), text="-",font=("Times",10, 'bold'))
btnSub.place(x=230,y=175)

btnMul = Button(root, padx=10, pady=14, bg='white',command=lambda:btnClick("*"), text="*",font=("Times",10, 'bold'))
btnMul.place(x=230,y=230)

btnDiv = Button(root, padx=12, pady=14, bg='white',command=lambda:btnClick("/"), text="/",font=("Times",10, 'bold'))
btnDiv.place(x=230,y=286)

# EQUAL
btnEqual = Button(root, padx=108, pady=8, bg='white', command=equlbut, text="=",font=("Times",10, 'bold'))
btnEqual.place(x=35,y=345)


root.mainloop()