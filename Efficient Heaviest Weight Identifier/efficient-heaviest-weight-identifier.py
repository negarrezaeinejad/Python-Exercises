x1=float(input("enter the weight of the x1: "))
x2=float(input("enter the weight of the x2: "))
x3=float(input("enter the weight of the x3: "))
x4=float(input("enter the weight of the x4: "))
x5=float(input("enter the weight of the x5: "))
if x1+x2==x3+x4:
    print(f"the heavier one is x5 = {x5}")
elif x1+x2>x3+x4:
    if x1>x2:
        print(f"the heavier one is x1 = {x1}")
    else:
        print(f"the heavier one is x2 = {x2}")
elif x1+x2<x3+x4:
    if x3>x4:
        print(f"the heavier one is x3 = {x3}")
    else:
        print(f"the heavier one is x4 = {x4}")
