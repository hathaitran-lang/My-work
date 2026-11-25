while True:
    x=int(input("Enter a number: "))
    if x>0 and x%2==0:
        print("The number is even.")
    if x>0 and x%2!=0:
        print("The number is odd.")
    if x<=0:
        print("please enter another number.")
        continue