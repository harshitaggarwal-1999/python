from tkinter import*
def fun():
    global ent1,ent2
    
    ent1=int(e1.get())
    ent2=int(e2.get())
    s=ent1+ent2
    messagebox.showinfo("sum=",str(s))
m=Tk()
m.title('good')
button=Button(m,text='10',command=fun)
button1=Button(m,text='20',command=fun)
button2=Button(m,text='+',command=fun)
button.pack()
button1.pack()
button2.pack()
