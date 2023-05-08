# Quadratic Equation Solver

This Python program takes the parameters of a quadratic equation as input and prints the equation in the output. If the coefficient of x^2 is 1, it will not be shown, and if it is 0, the parameter related to it would be omitted. After printing the equation, the program proceeds to solve the equation and print the results.

## Usage

To run the program, simply execute the Python script using a Python interpreter, and follow the prompts to enter the parameters of the quadratic equation.

```python
python quadratic_equation_solver.py
```

When prompted, enter the values of a, b, and c for your quadratic equation. The program will then print the equation and the solution(s) (if any). If the quadratic equation has two real solutions, the program will output both solutions. If the equation has only one solution, the program will output the single solution. If the equation has no real solutions, the program will output an error message.

## Example

Let's say we want to solve the quadratic equation 2x^2 + 3x + 1 = 0. To do this, we can run the program and enter the following values:

```python
please enter a: 2
please enter b: 3
please enter c: 1
```

The program will then print the equation and the solution(s):

```python
P=2x^2+3x+1
delta= 1
The equation has two answers:
-2.0 -4.0
```

In this example, the program has correctly calculated the two real solutions of the equation.

As another example, let's say we want to solve the linear equation 5x + 1 = 0. To do this, we can run the program and enter the following values:

```python
please enter a: 0
please enter b: 5
please enter c: 1
```

The program will then print the equation and the solution(s):

```python
5x+1
The equation only has one answer: -0.2
```

In this example, the program has correctly calculated the single solution of the equation.

Note that in this example, the coefficient of x^2 is 0, so the program omits it in the equation output.