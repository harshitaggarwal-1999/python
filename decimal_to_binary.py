N=int(input())
sum1=0
pr=1
pr2=1
x=0
while(N!=0):
    if (2**x>N):
        N=N-2**(x-1)
        sum1=sum1+pr2
        x=0
        pr=1
        pr2=1
    if (2**x==N):
        N=N-2**(x)
        sum1=sum1+pr     
        x=0
        pr=1
        pr2=1
    else :
        pr2=pr
        x=x+1
        pr=10*pr2
print(sum1)
        
