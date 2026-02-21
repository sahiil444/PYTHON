n = int(input("Enter the the number:"))
fact = 1
temp = n
while(n != 0):
    fact *= n
    n -= 1

print("factorial of ",temp,":",fact)