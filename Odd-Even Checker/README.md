# Odd-Even Checker

This is a Python code that checks whether a given integer is odd or even. It contains a single function called `odd_even` that takes an integer as an argument and prints whether the number is odd or even.

## Function Description

### `odd_even(num)`

This function takes an integer `num` as input and checks whether it is odd or even. If the number is even, it prints that the number is even. If the number is odd, it prints that the number is odd.

## Usage

To use the `odd_even` function, you need to call it with an integer as input. For example:

```python
num = int(input("Please Enter A Number: "))
odd_even(num)
```

This will prompt the user to enter a number, then call the `odd_even` function to check whether the number is odd or even.

## Example

Suppose you want to check whether the number 7 is odd or even. You can call the `odd_even` function like this:

```python
odd_even(7)
```

The output will be:

```python
7 is odd!
```

## Output

To print the output to a file, you can use the `print` function with the `file` parameter to specify the output file. For example, to print the output of the `odd_even` function to a file called `output.txt`, you can do the following:

```python
num = int(input("Please Enter A Number: "))
output_file = open('output.txt', 'w')
print(odd_even(num), file=output_file)
output_file.close()
```

This will prompt the user to enter a number, call the `odd_even` function with the input number, print the output to the `output.txt` file, and close the file.