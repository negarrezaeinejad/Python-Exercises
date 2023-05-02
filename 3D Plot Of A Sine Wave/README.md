# 3D Plot Of A Sine Wave

This is a simple Python code that uses NumPy and Matplotlib to generate a 3D plot of a sine wave.

## Dependencies

- NumPy
- Matplotlib

## Installation

You can install NumPy and Matplotlib using pip.

```python
pip install numpy matplotlib
```

## Usage

```python
import numpy as np
import matplotlib.pyplot as plt

ax=plt.axes(projection='3d')
z=np.linspace(0,30,201)
x=np.cos(z)
y=np.sin(z)

ax.plot3D(x,y,z)
plt.show()
```

## Output

The code generates a 3D plot of a sine wave, with the x and y coordinates being the cosine and sine of the z coordinate respectively. The plot is displayed using Matplotlib's `plt.show()` function.