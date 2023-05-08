x1=float(input("enter the weight of the x1: "))
x2=float(input("enter the weight of the x2: "))
x3=float(input("enter the weight of the x3: "))
x4=float(input("enter the weight of the x4: "))
x5=float(input("enter the weight of the x5: "))
if x1+x2==x3+x4:
    print(f"the different one is x5 = {x5}")
elif x1+x2!=x3+x4:
    if x1==x4:
        if x1==x3:
            print(f"the different one is x2 = {x2}")
        else:
            print(f"the different one is x3 = {x3}")
    elif x1!=x4:
        if x1==x3:
            print(f"the different one is x4 = {x4}")
        else:
            print(f"the different one is x1 = {x1}")