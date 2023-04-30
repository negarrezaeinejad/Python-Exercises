# Efficient Heaviest Weight Identifier

This Python program efficiently identifies the heaviest weight among six given weights with a minimum number of steps. It takes input from the user for the weights of six items and compares them to identify the heaviest weight.

## Example Usage

```python
enter the weight of the x1: 15
enter the weight of the x2: 18
enter the weight of the x3: 15
enter the weight of the x4: 15
enter the weight of the x5: 15
the heavier one is x2 = 18.0
```

## How it works

The program first takes input from the user for the weights of six items - `x1`, `x2`, `x3`, `x4`, and `x5`. It then uses a series of comparisons to efficiently identify the heaviest weight among the six.

First, it checks if the sum of `x1` and `x2` is equal to the sum of `x3` and `x4`. If this is the case, it determines that `x5` is the heaviest weight.

If the sum of `x1` and `x2` is greater than the sum of `x3` and `x4`, it then compares `x1` and `x2` to determine which one is heavier. Similarly, if the sum of `x1` and `x2` is less than the sum of `x3` and `x4`, it compares `x3` and `x4` to determine which one is heavier.

The program then prints the result indicating which item is the heaviest and its weight.