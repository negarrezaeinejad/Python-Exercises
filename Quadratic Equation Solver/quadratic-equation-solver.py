a=float(input("please enter a: "))
b=float(input("please enter b: "))
c=float(input("please enter c: "))
print(f"P={a}(x^2)+{b}x+{c}")
if a==0:
    if b==0:
        if c==0:
            print("p=0")
        else:
            print(f"P={c}")
    elif b==1:
        if c==0:
            print(f"P=x")
        else:
            print(f"P=x+{c}")
    else:
        if c==0:
            print(f"P={b}x")
        else:
            print(f"{b}x+{c}")
elif a==1:
    if b==0:
        if c==0:
            print("p=x^2")
        else:
            print(f"P=x^2+{c}")
    elif b==1:
        if c==0:
            print(f"p=x^2+x")
        else:
            print(f"P=x^2+x+{c}")
    else:
        print(f"x^2+{b}x+{c}")
else:
    if b==0:
        if c==0:
            print(f"p={a}x^2")
        else:
            print(f"P={a}x^2+{c}")
    elif b==1:
        if c==0:
            print(f"p={a}^2+x")
        else:
            print(f"P={a}x^2+x+{c}")
    else:
        print(f"P={a}x^2+{b}x+{c}")
#حل معادله
if a==0:
    if b==0:
        if c==0:
            print("The equation has infinite answers.")
        else:
            print("The equation doesn't have an answer.")
    else:
        if c==0:
            print("The equation has an answer:",0)
        else:
            print("The equation only has one answer: ",-c/b)
else:
    delta = b ** 2 - 4 * a * c
    print("delta=", delta)
    if delta < 0:
        print("The equation doesn't have an answer.")
    elif delta == 0:
        print("The equation only has one answer: ")
        x = (-b) / (2 * a)
        print(x)
    else:
        print("The equation has two answers: ")
        x1 = (-b + (delta) ** (0.5)) / 2 * a
        x2 = (-b - (delta) ** (0.5)) / 2 * a
        print(x1,x2)