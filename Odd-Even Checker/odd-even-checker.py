# function definition
def odd_even(num):
    result = num % 2
    if (result == 0):
        print("%d is even!" %(num))
    else:
        print("%d is odd!" %(num))
  

# function call
num = int(input("Please Enter A Number: "))
odd_even(num)5