# write a function that greet a user with name and if no name is provided it should greet with default user name 

def greet(name = "User"):
    return "Hello " + name + "!"

print(greet("sahil"))
print(greet())