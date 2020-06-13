largest = None
smallest = None
while True:
    num = input("Enter a number: ")
    num = int(num)
    try:
        if smallest == None:
            smallest = num
        elif num<smallest:
            smallest = num
        if largest == None:
            largest = num
        elif num>largest:
            largest = num
    except:
    	if num == "done" :
            break
        else:
            print("Invalid input")


print("Maximum is ", largest)
print("Minimum is ",smallest)
