file = open("file.txt", "r")  
print (file.read(5))
file = open('file.txt','w') 
file.write("This is the write command") 
file.write("It allows us to write in a particular file") 
file.close()
file = open("file.txt", "r")  
print (file.read())
file=open('file.txt','a')
file.write("hi friend")
file.close()
file= open('file.txt','r')
print(file.read())
with open('file.txt') as file:
    data= file.readlines()
for line in data:
    word = line.split()
    print(word)
