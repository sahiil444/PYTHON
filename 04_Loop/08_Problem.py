import math
n = int(input("Enter the number: "))
flage = 0

if(n<=1):
    print(n,"is not a Prime Number")
else:
    # for i in range(2,n//2):
    for i in range(2,int(math.sqrt(n)+1)):
        if(n%i == 0):
            flage = 1
            break
    if(flage == 0):
        print(n,"is prime number")
    else:
        print(n,"is not a prime number")

