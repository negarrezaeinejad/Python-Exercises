class Vector:
    def __init__(self,x,y):
        self.__x=0
        self.__y=0
        self.x=x
        self.y=y

    @property
    def x(self):
        return self.__x
    @x.setter
    def x(self,x):
        if isinstance(x,int):
            self.__x=x
        else:
            print("Error")
    @property
    def y(self):
        return self.__y
    @y.setter
    def y(self,y):
        if isinstance(y,int):
            self.__y=y
        else:
            print("Error")
            
    def __str__(self):
        return f"({self.x},{self.y})"
    def __repr__(self):
        return f"{self.x:+}i{self.y:+}j"
    def __neg__(self):
        return Vector(-self.x,-self.y)
    def __invert__(self):
        return Vector(self.y,self.x)
    def __abs__(self):
        return (self.x**2+self.y**2)**.5
    def __add__(self,w):
        return Vector(self.x+w.x,
                      self.y+w.y)
    def __mul__(self,w):
        return self.x*w.x+self.y*w.y
    def __sub__(self,w):
        return self+(-w)
    def __lt__(self,w):
        return abs(self)<abs(w)
    def __le__(self,w):
        return abs(self)<=abs(w)
    def __eq__(self,w):
        return self.x==w.x and\
               self.y==w.y
    
if __name__=="__main__":
    v=Vector(3.0,4)
    u=Vector(-5,4)
    z=Vector(3,4)
    print(f"v={v}")
    print(f"u={u}")
    print(f"-v={-v}")
    print(f"~v={~v}")
    print(f"abs(v)={abs(v)}")
    print(f"u+v = {u+v}")
    print(f"u*v = {u*v}")
    print(f"u-v = {u-v}")
    print(f"u<v = {u<v}")
    print(f"u<=v = {u<=v}")
    print(f"z==v = {z==v}")
    print(f"z==u = {z==u}")