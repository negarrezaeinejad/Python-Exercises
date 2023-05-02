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