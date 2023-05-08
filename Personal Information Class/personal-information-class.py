class Person:
    def __init__(self,fname,lname,city,year):
        self.fname=fname
        self.lname=lname
        self.year=year
        self.city=city
    def age(self):
        import datetime
        now=datetime.datetime.now()
        return now.year-self.year
    def __str__(self):
        s1=f"I am {self.fname} {self.lname}.\n"
        s2=f"I am from {self.city}.\n"
        s3=f"I am {self.age()} years old.\n"
        s4=""
        if self.fname=='Micheal' and self.lname=='Jackson':
            s4="I am the head of family."
        return s1+s2+s3+s4
    def __abs__(self):
        return self.age()
    def __lt__(self,w):
        return abs(self)<abs(w)
    def __le__(self,w):
        return abs(self)<=abs(w)
if __name__=="__main__":
    Micheal=Person("Micheal","Jackson","Indiana",1958)
    Sarah=Person("Sarah","Dawson","New York",1997)
    print(Micheal)
    print(Sarah)
    print(Micheal>Sarah)


























##class Rect:
##    def __init__(abc,tol,arz):
##        abc.tol=tol
##        abc.arz=arz
##    def ms(self):
##        return self.tol*self.arz
##    def mh(self):
##        return (self.tol+self.arz)*2
##    def __str__(self):
##        print('salam')
##        return f"masahat = {self.ms()} mohit = {self.mh()}"
##    def __repr__(self):
##        return str(self)
##    def __abs__(self):
##        return self.ms()
##    def __lt__(self,w):
##        return abs(self)<abs(w)
##    def __le__(self,w):
##        return abs(self)<=abs(w)
##    
##if __name__=="__main__":
##    m=Rect(5,6)
##    m1=Rect(2,10)
##    
##    print(m)
##    print(m1)
##    print(abs(m))
##    
    
























##class Circle:
##    def __init__(self,r=0):
##        self.r=r
##        self.pi=3.1415
##    def ms(r,pi):
##        return pi*r**2
##    def ms_(xodesh):
##        return xodesh.pi*xodesh.r**2
##    def __str__(self):
##        return f"r={self.r} masahat={self.ms_()}"
##    def __repr__(self):
##        return f"r={self.r} masahat={self.ms_()}"
##        
##
##if __name__=="__main__":
##    c=Circle()
##    c1=Circle(100)
##    print(c.r,c.ms_())
##    c.r=10
##    print(c.r,c.ms_())
##    print(c)





##class Car:
##    speed=100#static property
##
##if __name__=="__main__":
##    pride=Car()
##    p405=Car()
##    print(Car.speed,pride.speed,
##          p405.speed)
##    Car.speed=200
##    print(Car.speed,pride.speed,
##          p405.speed)
##    pride.speed=300
##    print(Car.speed,pride.speed,
##          p405.speed)
##    
##    Car.speed=400
##    print(Car.speed,pride.speed,
##          p405.speed)
    
    

##    print(pride)
##    print(Car)
