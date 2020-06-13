a=int(input())
b=int(input())
flag=0
list1=[]
list1.append(a)
list1.append(b)
while(flag!=2):
    sum=a+b
    sum=sum%10
    a=b
    b=sum
    if(sum==1):
        flag=flag+1
        list1.append(sum)
    else:
        list1.append(sum)
print(list1)
list2=[]
x=len(list1)
for i in range(x):
    if(i%2==0):
        list2.append(list1[i])
print(list2)
list3=[]
m=len(list2)
for j in range(m):
    if(j%2==0):
        list3.append(list2[j])
print(list3)




