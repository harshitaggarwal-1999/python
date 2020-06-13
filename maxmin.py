largest = None
smallest = None
while True:
    num = input("Enter a number: ")

    try:
        num = int(num)
        if smallest == None:
            smallest = num
        elif num < smallest:
            smallest = num
        if largest == None:
            largest = num
        elif num > largest:
            largest = num
    except:
        if num == "done":
            break
        else:
            print("Invalid input")
            continue

print("Maximum is ", largest)
print("Minimum is ", smallest)

