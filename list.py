list1=[]
list2=[]
n=int(input())
for i in range(n):
    num=int(input())
    list1.append(num)
for j in list1:
    if j>=5:
        list2.append(j)
list2.sort()
print(list2)
