n= int(input("enter the number which has to reversed :"))
rem=0
summ=0
while(n!=0):
    rem=n%10
    n=n//10
    summ=summ*10+rem
print(summ)
