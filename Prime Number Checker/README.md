# Prime Number Checker

This is a Python program that checks whether a given integer entered by the user is prime or not. A prime number is a positive integer greater than 1 that has no positive integer divisors other than 1 and itself.

## Example

```python
Please enter an integer: 17
17 is prime.
```

In this example, the program prompts the user to enter an integer, and then checks whether the number entered is prime or not. It does this by iterating over all the integers from 2 to half of the number (`x // 2`), and checking whether the number is divisible by any of these integers. If it is, the program prints that the number is not prime and exits the loop. If no divisors are found, the program prints that the number is prime.