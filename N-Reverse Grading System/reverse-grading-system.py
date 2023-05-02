x=str(input("please enter your score: "))
if  x=="A"or x=="a":
    print("You got a score between 18 and 20")
elif x=="B"or x=="b":
    print("You got a score between 16 and 17.9999...")
elif  x=="C" or x=="c":
    print("You got a score between 14 and 15.9999...")
elif  x=="D"or x=="d":
    print("You got a score between 12 and 13.9999...")
elif   x=="E"or x=="e":
    print("You got a score between 10 and 11.9999...")
elif   x=="F"or x=="f":
    print("You got a score between 0 and 9.9999... and failed")
else:
    print("Your score is not correctly entered.")