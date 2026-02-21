# write a function that take variable  arguments and prints them in formate of key:value pair

def print_name(**kwargs):
    for key,value in kwargs.items():
        print(f"{key} : {value}")


# print_name(name="sahil",branch = "cse ai/ml")
# print_name(name="sahil",branch = "cse ai/ml", rollno = 10)
print_name(name="sahil",branch = "cse ai/ml", rollno = 10,section = "A")