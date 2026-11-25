from unittest import case


while True:
    a, b=map(int,input("Enter your input (month/year): ").split("/"))
    match a:
        case 1:
            print(31)
        case 2:
            if (b%4==0 and b%100!=0) or (b%400==0):
                print(29)
            else:
                print(28)
        case 3:
            print(31)
        case 4:
            print(30)
        case 5:
            print(31)
        case 6:
            print(30)
        case 7:
            print(31)
        case 8:
            print(31)
        case 9:
            print(30)
        case 10:
            print(31)
        case 11:
            print(30)
        case 12:
            print(31)
    if a<=0 or b<=0:
        print("invalid numbers")