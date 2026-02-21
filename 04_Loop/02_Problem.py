num = int(input("Enter the given number:"))

sum = 0
for i in range(1,num+1):
    if(i%2 == 0):
        sum += i
print("The total Sum of Even number ",sum)