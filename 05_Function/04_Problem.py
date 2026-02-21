# calculate area and circumfarance

import math
def Area_And_Perimeter(r):
    area = math.pi*r*r
    peri = 2*math.pi*r
    return area,peri

area,perimeter = Area_And_Perimeter(3)
print("Area of circle :",area,"Circumferance of circle: ",perimeter)


# How to print value upto 3 digit

print("Area of circle :",round(area,3),"Circumferance of circle: ",round(perimeter,3))

print("Area of circle :",format(area,".3f"),"Circumferance of circle: ",format(perimeter,".3f"))

print("Area of circle :",f"{area:.3f}","Circumferance of circle: ",f"{perimeter:.3f}")

