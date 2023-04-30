x=float(input("please enter your score: "))
if  18<=x<=20:
    print("You got an A.")
elif   16<=x<18:
    print("You got a B")
elif   14<=x<16:
    print("You got a C")
elif   12<=x<14:
    print("You got a D")
elif   10<=x<12:
    print("You got an E")
elif   0<=x<10:
    print("You failed.")
else:
    print("Your score is not in the correct internal.")