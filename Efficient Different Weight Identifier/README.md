# Efficient Different Weight Identifier

This Python code is used to identify the weight which is different from the rest among six similar weights with minimum weighing steps.

## How it works

The code first takes inputs for the weights of six objects - `x1`, `x2`, `x3`, `x4`, `x5`. It then checks whether the sum of weights of the first two objects (`x1` and `x2`) is equal to the sum of the weights of the last two objects (`x3` and `x4`). If they are equal, then the different object is `x5`.

If the sums of weights are not equal, the code checks for three cases:

1. If `x1` and `x4` have the same weight, it checks whether `x1` and `x3` have the same weight. If they do, then the different object is `x2`. Otherwise, the different object is `x3`.
2. If `x1` and `x4` do not have the same weight, it checks whether `x1` and `x3` have the same weight. If they do, then the different object is `x4`. Otherwise, the different object is `x1`.

## Example

```python
enter the weight of the x1: 50
enter the weight of the x2: 35
enter the weight of the x3: 50
enter the weight of the x4: 50
enter the weight of the x5: 50
the different one is x2 = 35.0
```