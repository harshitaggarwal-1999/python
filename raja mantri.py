from tkinter import * 
from tkinter import messagebox

m=Tk()
def fun1():
    messagebox.showinfo('raja','prize earned = $1000')
def fun2():
    messagebox.showinfo('mantri','prize earned = $500')
def fun3():
    messagebox.showinfo('chor','prize earned = $0')
def fun4():
    messagebox.showinfo('sipahi','prize earned = $100')    
def func():
    tk=Tk()
    b1=Button(tk,text='1',height=10,width=10,bg='red',fg="yellow",activebackground='grey',command=fun1)
    b3=Button(tk,text='2',height=10,width=10,bg='blue',fg='yellow',activebackground='grey',command=fun2)
    b4=Button(tk,text='3',height=10,width=10,bg='green',fg='yellow',activebackground='grey',command=fun3)
    b2=Button(tk,text='4',height=10,width=10,bg='pink',fg='blue',activebackground='grey',command=fun4)
    t=Text(tk,height=10,width=30)
    t.pack()
    t.insert(END,'lets see how much u win.......!!!')
    b1.pack(side=TOP)
    b2.pack(side=BOTTOM)
    b3.pack(side=LEFT)
    b4.pack(side=RIGHT)
    tk.mainloop()
    
m.title('aao khelein')
Label(m,text='First Name').grid(row=0)
Label(m,text='Last Name').grid(row=1)
e1=Entry(m)
e2=Entry(m)
e1.grid(row=0,column=1)
e2.grid(row=1,column=1)
button=Button(m,text="submit",activebackground='black',activeforeground='yellow',command=func)
button.grid(row=3,column=1)
m.mainloop

