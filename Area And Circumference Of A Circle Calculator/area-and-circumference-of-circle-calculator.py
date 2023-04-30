'''
r(radius) 
s(area/side) 
p(circumference/perimeter)
'''
from math import pi
r=int(input("Plesase enter your desired Radius: "))
s=pi*(r**2)
p=2*pi*r
print("Area of a circle with radius of ",r," is ",s )
print("Circumference of a circle with radius of ",r," is ",p )