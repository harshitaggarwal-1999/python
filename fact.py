n = int(input())
x = 0
y = 1
for i in range(n-2):
    s = x+y
    print(s)
    x = y
    y = s
