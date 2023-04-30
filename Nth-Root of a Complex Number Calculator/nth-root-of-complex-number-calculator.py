x=float(input("please enter the real part: "))
y=float(input("please enter the imaginary part: "))
import math
if x!=0:
    f=float(math.atan2(y,x))
else:
    f=math.pi/2
p=math.sqrt(pow(x,2)+pow(y,2))
m=int(input('please enter your desired root: '))
r=pow(p,1/m)
for k in range(0,m):
    t = ((f + 2 * k * math.pi) / m)
    x1=(r*math.cos(t))
    y1=(r*math.sin(t))
    z=complex(x1,y1)
    print("root", k, "=",z)