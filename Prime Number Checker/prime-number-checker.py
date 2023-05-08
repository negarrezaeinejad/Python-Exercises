x=int(input("Please enter an integer: "))
for i in range(2,x//2):
    if x%i==0:
        print(f"{x} is not prime.")
        break
else:
    print(f"{x} is prime.")