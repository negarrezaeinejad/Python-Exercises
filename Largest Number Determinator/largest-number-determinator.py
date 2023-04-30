# function definition
def print_maximum(num1, num2, num3):
    if num1 > num2 and num1 > num3:
        result = num1
    elif num2 > num1 and num2 > num3:
        result = num2
    else:
        result = num3

    print("Max number between %d, %d and %d is %d" %(num1, num2,num3, result))

# function call
num1 = int(input("Please Enter Number 1: "))
num2 = int(input("Please Enter Number 2: "))
num3 = int(input("Please Enter Number 3: "))

print_maximum(num1, num2, num3)


//////////////////////////////////
#second way
num1 = int(input("Please Enter Number 1: "))
num2 = int(input("Please Enter Number 2: "))
num3 = int(input("Please Enter Number 3: "))

result = max(num1,num2,num3)
print("Max number between %d, %d and %d is %d" %(num1, num2,num3, result))