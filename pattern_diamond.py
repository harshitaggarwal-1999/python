n=int(input())
for i in range(0,n):
    for k in range(n-1-i):
        print(" ",end ="")
    for j in range(0,i+1):
        print("* ",end  = " ")
    print()
for l in range(1,n):
    for m in range(0,l):
        print(" ",end = "")
    for b in range(n-l):
        print("* ",end =" ")
    print()
    
