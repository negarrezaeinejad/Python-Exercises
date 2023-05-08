import math
x=tuple([eval(x) for x in input('Enter the 1st point:').split(',')])
y=tuple([eval(x) for x in input('Enter the 2nd point:').split(',')])
z=tuple([eval(x) for x in input('Enter the 3rd point:').split(',')])
a=math.sqrt((x[0]-y[0])**2+(x[1]-y[1])**2)
b=math.sqrt((x[0]-z[0])**2+(x[1]-z[1])**2)
c=math.sqrt((y[0]-z[0])**2+(y[1]-z[1])**2)
ep=10**-10
#print (a,b,c)
if a+b>c and a+c>b and b+c>a:
    #print('three points construct a triangle')
    if a>=b-ep and b>=a-ep and b>=c-ep and c>=b-ep:
        print('three points construct an equilateral triangle')
    elif (a>=b-ep and b>=a-ep and c**2>=a**2+b**2-ep and a**2+b**2>=c**2-ep)\
        or (a>=c-ep and c>=a-ep and b**2>=a**2+c**2-ep and a**2+c**2>=b**2-ep)\
        or (b>=c-ep and c>=b-ep and a**2>=b**2+c**2-ep and b**2+c**2>=a**2-ep):
        print('three points construct a right-angled and isosceles triangle')
    elif (a>=b-ep and b>=a-ep) or (b>=c-ep and c>=b-ep) or (a>=c-ep and c>=a-ep):
        print('three points construct an isosceles triangle')
    else:
        print('three points construct a scalene triangle')
else:
    print('three points do not construct triangle')