from tkinter import *
from tkinter import messagebox

t=Tk()
t.title("Calcy")
t.geometry("260x390")
e1=Text(t,height=2,width=27)
e1.place(x=20,y=30)

def Equal():
    s1 = e1.get('0.0',END)
    s1 = s1[0:len(s1)-1]
    s2 = s1
    s2 = s2.replace('+',',')
    s2 = s2.replace('-',',')
    s2 = s2.replace('*',',')
    s2 = s2.replace('/',',')
    L1 = s2.split(',')
    try:
        for i in range(len(L1)):
            L1[i] = float(L1[i])
    except:
        messagebox.showinfo("Error","Enter Value")
        return
    L2 = []
    for i in s1:
        if i=='+' or i=='-' or i=='*' or i=='/':
            L2.append(i)
    while L2.count('/')!=0:
        t = L2.index('/')
        if L1[t+1]==0:
            messagebox.showinfo("Zero Division Error","Can't Divide By 0")
            return
        ans = L1[t] / L1[t+1]
        L1[t] = ans
        L1.remove(L1[t+1])
        L2.remove('/')
    while L2.count('*')!=0:
        t = L2.index('*')
        ans = L1[t] * L1[t+1]
        L1[t] = ans
        L1.remove(L1[t+1])
        L2.remove('*')
    while L2.count('+')!=0:
        t = L2.index('+')
        ans = L1[t] + L1[t+1]
        L1[t] = ans
        L1.remove(L1[t+1])
        L2.remove('+')
    while L2.count('-')!=0:
        t = L2.index('-')
        ans = L1[t] - L1[t+1]
        L1[t] = ans
        L1.remove(L1[t+1])
        L2.remove('-')
    s1 = str(L1[0])
    L3 = s1.split('.')
    if L3[1].count('0') == len(L3[1]):
        s1 = L3[0]
        e1.delete('0.0',END)
        e1.insert(INSERT,s1)
    else:
        e1.delete('0.0',END)
        e1.insert(INSERT,s1)

def Plus():
    s1 = e1.get('0.0',END)
    if len(s1)>1 and s1[len(s1)-2]!='+' and s1[len(s1)-2]!='-' and s1[len(s1)-2]!='/' and s1[len(s1)-2]!='*' and s1[len(s1)-2]!='.':
        e1.insert(INSERT,'+')

def Minus():
    s1 = e1.get('0.0',END)
    if len(s1)>1 and s1[len(s1)-2]!='+' and s1[len(s1)-2]!='-' and s1[len(s1)-2]!='/' and s1[len(s1)-2]!='*' and s1[len(s1)-2]!='.':
        e1.insert(INSERT,'-')

def Mult():
    s1 = e1.get('0.0',END)
    if len(s1)>1 and s1[len(s1)-2]!='+' and s1[len(s1)-2]!='-' and s1[len(s1)-2]!='/' and s1[len(s1)-2]!='*' and s1[len(s1)-2]!='.':
        e1.insert(INSERT,'*')

def Div():
    s1 = e1.get('0.0',END)
    if len(s1)>1 and s1[len(s1)-2]!='+' and s1[len(s1)-2]!='-' and s1[len(s1)-2]!='/' and s1[len(s1)-2]!='*' and s1[len(s1)-2]!='.':
        e1.insert(INSERT,'/')

def Cancel():
    e1.delete('0.0',END)

def Back():
    s1 = e1.get('0.0',END)
    s1 = s1[0:len(s1)-2]
    e1.delete('0.0',END)
    e1.insert(INSERT,s1)

def Percent():
    s1 = e1.get('0.0',END)
    num = float(s1)
    num = num/100
    s1 = str(round(num,6))
    e1.delete('0.0',END)
    e1.insert(INSERT,s1)

def One():
    s1 = e1.get('0.0',END)
    if len(s1)==1:
        e1.insert(INSERT,'1')
    elif s1[0]=='0' and len(s1)==2:
        e1.delete('0.0',END)
        e1.insert(INSERT,'1')
    else:
        e1.insert(INSERT,'1')

def Two():
    s1 = e1.get('0.0',END)
    if len(s1)==1:
        e1.insert(INSERT,'2')
    elif s1[0]=='0' and len(s1)==2:
        e1.delete('0.0',END)
        e1.insert(INSERT,'2')
    else:
        e1.insert(INSERT,'2')

def Three():
    s1 = e1.get('0.0',END)
    if len(s1)==1:
        e1.insert(INSERT,'3')
    elif s1[0]=='0' and len(s1)==2:
        e1.delete('0.0',END)
        e1.insert(INSERT,'3')
    else:
        e1.insert(INSERT,'3')

def Four():
    s1 = e1.get('0.0',END)
    if len(s1)==1:
        e1.insert(INSERT,'4')
    elif s1[0]=='0' and len(s1)==2:
        e1.delete('0.0',END)
        e1.insert(INSERT,'4')
    else:
        e1.insert(INSERT,'4')

def Five():
    s1 = e1.get('0.0',END)
    if len(s1)==1:
        e1.insert(INSERT,'5')
    elif s1[0]=='0' and len(s1)==2:
        e1.delete('0.0',END)
        e1.insert(INSERT,'5')
    else:
        e1.insert(INSERT,'5')

def Six():
    s1 = e1.get('0.0',END)
    if len(s1)==1:
        e1.insert(INSERT,'6')
    elif s1[0]=='0' and len(s1)==2:
        e1.delete('0.0',END)
        e1.insert(INSERT,'6')
    else:
        e1.insert(INSERT,'6')
        
def Seven():
    s1 = e1.get('0.0',END)
    if len(s1)==1:
        e1.insert(INSERT,'7')
    elif s1[0]=='0' and len(s1)==2:
        e1.delete('0.0',END)
        e1.insert(INSERT,'7')
    else:
        e1.insert(INSERT,'7')
        
def Eight():
    s1 = e1.get('0.0',END)
    if len(s1)==1:
        e1.insert(INSERT,'8')
    elif s1[0]=='0' and len(s1)==2:
        e1.delete('0.0',END)
        e1.insert(INSERT,'8')
    else:
        e1.insert(INSERT,'8')
        
def Nine():
    s1 = e1.get('0.0',END)
    if len(s1)==1:
        e1.insert(INSERT,'9')
    elif s1[0]=='0' and len(s1)==2:
        e1.delete('0.0',END)
        e1.insert(INSERT,'9')
    else:
        e1.insert(INSERT,'9')
        
def Zero():
    s1 = e1.get('0.0',END)
    if len(s1)==1:
        e1.insert(INSERT,'0')
    elif s1[0]!='0' or s1.count('.')==1:
        e1.insert(INSERT,'0')

def Dot():
    s1 = e1.get('0.0',END)
    if len(s1)==1:
        e1.insert(INSERT,'0.')
    elif s1[len(s1)-2]=='+' or s1[len(s1)-2]=='-' or s1[len(s1)-2]=='*' or s1[len(s1)-2]=='/':
        e1.insert(INSERT,'0.')
    elif s1.rfind('.')<s1.rfind('+') or s1.rfind('.')<s1.rfind('*') or s1.rfind('.')<s1.rfind('/') or s1.rfind('.')<s1.rfind('-'):
        e1.insert(INSERT,'.')
    elif s1.count('.')==0:
        e1.insert(INSERT,'.')

cancel=Button(t,text='C',height=2,width=4,command=Cancel)
cancel.place(x=20,y=80)
back=Button(t,text='<',height=2,width=4,command=Back)
back.place(x=80,y=80)
div=Button(t,text='/',height=2,width=4,command=Div)
div.place(x=140,y=80)
mult=Button(t,text='*',height=2,width=4,command=Mult)
mult.place(x=200,y=80)

one=Button(t,text='1',height=2,width=4,command=One)
one.place(x=20,y=140)
two=Button(t,text='2',height=2,width=4,command=Two)
two.place(x=80,y=140)
three=Button(t,text='3',height=2,width=4,command=Three)
three.place(x=140,y=140)
minus=Button(t,text='-',height=2,width=4,command=Minus)
minus.place(x=200,y=140)

four=Button(t,text='4',height=2,width=4,command=Four)
four.place(x=20,y=200)
five=Button(t,text='5',height=2,width=4,command=Five)
five.place(x=80,y=200)
six=Button(t,text='6',height=2,width=4,command=Six)
six.place(x=140,y=200)
plus=Button(t,text='+',height=2,width=4,command=Plus)
plus.place(x=200,y=200)

seven=Button(t,text='7',height=2,width=4,command=Seven)
seven.place(x=20,y=260)
eight=Button(t,text='8',height=2,width=4,command=Eight)
eight.place(x=80,y=260)
nine=Button(t,text='9',height=2,width=4,command=Nine)
nine.place(x=140,y=260)
equal=Button(t,text='=',height=6,width=4,command=Equal)
equal.place(x=200,y=260)

percent=Button(t,text='%',height=2,width=4,command=Percent)
percent.place(x=20,y=320)
zero=Button(t,text='0',height=2,width=4,command=Zero)
zero.place(x=80,y=320)
dot=Button(t,text='.',height=2,width=4,command=Dot)
dot.place(x=140,y=320)

t.mainloop()
