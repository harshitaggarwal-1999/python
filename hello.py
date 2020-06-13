from tkinter import* 
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

m.title('aao khelein')
t=Text(m,height=10,width=30)
Label(m,text='First Name').grid(row=0)
Label(m,text='Last Name').grid(row=1)
e1=Entry(m)
e2=Entry(m)
e1.grid(row=0,column=1)
e2.grid(row=1,column=1)
b1=Button(m,text='1',height=10,width=10,bg='red',fg="yellow",activebackground='grey',command=fun1)
b3=Button(m,text='2',height=10,width=10,bg='blue',fg='yellow',activebackground='grey',command=fun2)
b4=Button(m,text='3',height=10,width=10,bg='green',fg='yellow',activebackground='grey',command=fun3)
b2=Button(m,text='4',height=10,width=10,bg='pink',fg='yellow',activebackground='grey',command=fun4)

t.insert(END,'lets see how much u win.......!!!')
b1.pack(side=TOP)
b2.pack(side=BOTTOM)
b3.pack(side=LEFT)
b4.pack(side=RIGHT)
m.mainloop()
