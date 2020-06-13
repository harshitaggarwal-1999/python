n=int(input())
for i  in range(2,n):
    for j in range(1,i):
        flag=0
        if i%j==0:
            flag=flag+1
        samay=flag
        if samay==1:
            print(i)
            flag=0
