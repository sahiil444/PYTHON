list = ["apple","banana","mango","orange"]
list2 = ["apple","banana","mango","orange","apple"]
unique_list = []

for element in list2:
    if(element in unique_list):
        print("Duplicate item ",element)
        continue
    else:
        unique_list.append(element)


print(unique_list)