n =int(input())
x =int(input())
y =int(input())
sum = 0
for i in range(0,n):
    sum = x + y
    x=y
    y= sum
    print(sum)
