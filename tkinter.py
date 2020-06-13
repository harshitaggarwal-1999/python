from tkinter import *
from tkinter import messagebox
def fun():
    messagebox.showinfo("bhootni ke","welcome to harshit's world")
r=Tk()
r.title('counting seconds')
button=Button(r,text='stop',width=25,fg='yellow',bg='red',activebackground='blue',command=fun)
b2=Button(r,text='hi',command=r.destroy)
b3=Button(r,text='yo',command=r.destroy)
b4=Button(r,text='hello',command=r.destroy)
button.pack(side=LEFT)
b2.pack(side=TOP)
b3.pack(side=BOTTOM)
b4.pack(side=RIGHT) 
r.mainloop()

