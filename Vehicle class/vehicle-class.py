class Vehicle:
    def __init__(self,color,doors,tires,type):
        self.color=color
        self.doors=doors
        self.tires=tires
        self.type=type
    def brake(self):
        return '%s braking'%self.type
    def drive(self):
        return 'I am driving a %s %s' %(self.color,self.type)