# Personal Information Class

## Person Class

The `Person` class is a Python class that represents a person's information. It takes four parameters, `fname`, `lname`, `city`, and `year`, representing the person's first name, last name, city, and birth year, respectively.

The class has the following methods:

- `age()` - calculates the person's age based on their birth year.
- `__str__()` - returns a string with the person's information, including their name, age, and city.
- `__abs__()` - returns the absolute value of the person's age.
- `__lt__()` - compares the absolute values of two persons' ages and returns True if the first person is younger, False otherwise.
- `__le__()` - compares the absolute values of two persons' ages and returns True if the first person is younger or the same age, False otherwise.

The program creates two `Person` objects, `Micheal` and `Sarah`, and prints their information and whether `Micheal` is older than `Sarah`.

## Example

```python
if __name__=="__main__":
    Micheal=Person("Micheal","Jackson","Indiana",1958)
    Sarah=Person("Sarah","Dawson","New York",1997)
    print(Micheal)
    print(Sarah)
    print("Is Micheal older than Sarah?", Micheal>Sarah)
```

Output:

```python
I am Micheal Jackson.
I am from Indiana.
I am 65 years old.
I am the head of family.
I am Sarah Dawson.
I am from New York.
I am 26 years old.

Is Micheal older than Sarah? True
```