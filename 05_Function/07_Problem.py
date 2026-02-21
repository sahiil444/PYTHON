# write a function that take variable  arguments in single parameter and return thier sum
def sum_all(*args):
    return sum(args)

def sum(*args):
    print(*args)  # print 1 2 3 4 5
    print(args)   # print as a tuple (1,2,3,4,5)
    for i in args: # we can treverse using this args bcz it is in tuple
        print(i*10)

print(sum_all(1,2,3,4))
# sum(1,2,3,4,5)



