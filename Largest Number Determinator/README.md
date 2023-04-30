# Largest Number Determinator

This is a Python code that finds the maximum number among three input numbers.

## Installation

This code does not require any external library, and can be executed using Python 3.

## Usage

To use this code, follow these steps:

1. Open a terminal and navigate to the directory containing the code file.
2. Run the code by typing:

```python
python find_maximum.py
```

1. The code will prompt you to enter three numbers.
2. Enter the three numbers and press Enter.
3. The code will find the maximum of the three numbers, and display a message indicating what the maximum number is.

You can also redirect the output to a file using the following command:

```python
python find_maximum.py > output.txt
```

This will save the output to a file called "output.txt".

## Example

For example, let's say you want to find the maximum number among 3, 5, and 2. You would run the code and enter the following numbers at the prompt:

```
Please Enter Number 1: 3
Please Enter Number 2: 5
Please Enter Number 3: 2
```

The output would be:

```
Max number between 3, 5 and 2 is 5
```

There is also another way to find the maximum number in Python, which is using the `max()` function. You can use the following code instead:

```python
num1 = int(input("Please Enter Number 1: "))
num2 = int(input("Please Enter Number 2: "))
num3 = int(input("Please Enter Number 3: "))

result = max(num1,num2,num3)
print("Max number between %d, %d and %d is %d" %(num1, num2,num3, result))
```

This code will produce the same output as the previous one.