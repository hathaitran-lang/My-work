#wrte a program to find the sum of all real number from 1 to n
def sum_of_real_numbers(n):
    total=0
    for i in range(1,n+1):
        total+=i        
    
n=int(input("Enter a number: "))
print("The sum of all real numbers from 1 to",n,"is:",sum_of_real_numbers(n))