from tkinter import *
rt = Tk()
rt.title("calc")

men = Entry(rt, width=23 , borderwidth=20)
men.grid(row=0,column=0 , columnspan=4, padx=10, pady=10)

def click(number):
    cur = men.get()
    men.delete(0, END)
    men.insert(0, str(cur) + str(number))
   
def clear():
    men.delete(0, END)

def button_add():
         first_number = men.get()
         global f_num
         global math
         math = "addition"
         f_num = int(first_number)
         men.delete(0, END)
            
def subtract():
         first_number= men.get()
         global f_num
         global math
         math = "subtraction"
         f_num = int(first_number)
         men.delete(0, END)
         
def multiply():
         first_number= men.get()
         global f_num
         global math
         math = "multiply"
         f_num = int(first_number)
         men.delete(0, END)
          
def divide():
        first_number= men.get()
        global f_num
        global math
        math = "divide"
        f_num = int(first_number)
        men.delete(0, END)

def equal():
         second_number = men.get()
         men.delete(0, END)
         if math == "addition":
             men.insert(0, f_num + int(second_number))
         elif math == "subtraction":
             men.insert(0, f_num - int(second_number))
         elif math == "multiply":
             men.insert(0, f_num * int(second_number))
         elif math == "divide":
             men.insert(0, f_num / int(second_number))
         
bot1 = Button(rt, text="1", padx=75, pady=65, command=lambda: click(1))
bot2 = Button(rt, text="2", padx=75, pady=65, command=lambda: click(2))
bot3 = Button(rt, text="3", padx=75, pady=65, command=lambda: click(3))
bot4 = Button(rt, text="4", padx=75, pady=65, command=lambda: click(4))
bot5 = Button(rt, text="5", padx=75, pady=65, command=lambda: click(5))
bot6 = Button(rt, text="6", padx=75, pady=65, command=lambda: click(6))
bot7 = Button(rt, text="7", padx=75, pady=65, command=lambda: click(7))
bot8 = Button(rt, text="8", padx=75, pady=65, command=lambda: click(8))
bot9 = Button(rt, text="9", padx=75, pady=65, command=lambda: click(9))
bot0 = Button(rt, text="0", padx=75, pady=65, command=lambda: click(0))

botadd = Button(rt, text="+", padx=75, pady=65, command=button_add)
botequ = Button(rt, text="=", padx=75, pady=66, command=equal)
botclr = Button(rt, text="clear", padx=38, pady=70, command=clear)

botsub = Button(rt, text="-", padx=80, pady=65, comman=subtract)
botmul = Button(rt, text="x", padx=76, pady=65, comman=multiply)
botdiv = Button(rt, text="÷", padx=75, pady=65, comman=divide)

bot1.grid(row=3 , column=0)
bot2.grid(row=3 , column=1)
bot3.grid(row=3 , column=2)

bot4.grid(row=2 , column=0)
bot5.grid(row=2 , column=1)
bot6.grid(row=2 , column=2)

bot7.grid(row=1 , column=0)
bot8.grid(row=1 , column=1)
bot9.grid(row=1 , column=2)

bot0.grid(row=4 , column=0)
botadd.grid(row=4, column=1)
botequ.grid(row=4, column=2)
botclr.grid(row=4, column=3)

botsub.grid(row=3, column=3)
botmul.grid(row=2, column=3)
botdiv.grid(row=1, column=3)

rt.mainloop()