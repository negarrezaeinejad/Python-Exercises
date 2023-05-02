import numpy as np
import matplotlib.pyplot as plt

ax=plt.axes(projection='3d')
z=np.linspace(0,30,201)
x=np.cos(z)
y=np.sin(z)

ax.plot3D(x,y,z)
plt.show()