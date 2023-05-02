# 3D surface plot of the function

This Python code generates a 3D surface plot of the function sin(sqrt(x^2+y^2)). It makes use of the `numpy` and `matplotlib` libraries for numerical computation and visualization.

## Usage

1. Ensure you have the required libraries `numpy` and `matplotlib` installed in your environment.
2. Copy the code into a Python script or notebook.
3. Run the script/notebook to see the 3D surface plot.

```python
import numpy as np
import matplotlib.pyplot as plt

ax=plt.axes(projection='3d')

def f_func(x,y):
    return np.sin(np.sqrt(x**2+y**2))

x=np.linspace(-15,15,201)
y=np.linspace(-15,15,201)
xx,yy=np.meshgrid(x,y)
zz=f_func(xx,yy)

ax.plot_surface(xx,yy,zz)

plt.show()
```

## Example Output

The above code produces a 3D surface plot of the function sin(sqrt(x^2+y^2)). The output shows the shape of the function as a surface in 3D space.