age = int(input("Enter the age :"))
day = input("Enter the day: ")

if(age<18 and day == "wednesday"):
    print("6$")
elif(age>18 and day == "wednesday"):
    print("8$")
elif(age>18):
    print("12$")
elif(age<18):
    print("8$")