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
    print("Is Micheal older than Sarah?", Micheal>Sarah)