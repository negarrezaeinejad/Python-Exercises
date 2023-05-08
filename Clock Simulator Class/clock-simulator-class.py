class Clock:
    def __init__(self,hour=10,minute=10,second=23,op=1):
        self.__hour, self.__minute, self.__second=0,0,0
        if op==1:
            self.hour=hour
            self.minute=minute
            self.second=second
        if op==0:
            import datetime
            now=datetime.datetime.now()
            self.hour=now.hour
            self.minute=now.minute
            self.second=now.second
            

    @property
    def hour(self):
        return self.__hour
    @hour.setter
    def hour(self,hour):
        if 0<=hour<24:
            self.__hour=hour
        else:
            print("Error! invalid hour entry.")
    @hour.deleter
    def hour(self):
        print("self.hour is deleted.")
        del self.__hour

    @property
    def minute(self):
        return self.__minute
    @minute.setter
    def minute(self,minute):
        if 0<=minute<60:
            self.__minute=minute
        else:
            print("Error! invalid minute entry.")
    @minute.deleter
    def minute(self):
        del self.__minute

    def getSecond(self):
        return self.__second
    def setSecond(self,second):
        if 0<=second<60:
            self.__second=second
        else:
            print("Error! invalid second entry.")
    def delSecond(self):
        del self.__second
    second=property(getSecond,setSecond,delSecond)
    def __str__(self):
        return f"{self.hour:02}:{self.minute:02}:{self.second:02}"
    def __repr__(self):
        if self.__hour<12:
            return self.__str__()+" AM"
        elif self.__hour==12:
            return self.__str__()+" PM"
        else:
            return f"{self.hour-12:02}:{self.minute:02}:{self.second:02} PM"
            
    def tik(self):
        self.__second=(self.__second+1)%60
        if not self.__second:
            self.__minute=(self.__minute+1)%60
            if not self.__minute:
                self.__hour=(self.__hour+1)%24
    def __next__(self):
        self.tik()
        self.ring()
        return self
    def isMidnight(self):
        return self.hour==0 and self.minute==0 and\
               self.second==0
    def ring(self):
        import winsound
        import random
        if self.isMidnight():
            print("ding"*12)
            for i in range(10):
                winsound.Beep(
                    random.randrange(500,2500),
                    500
                    )
    def run(self):
        import time
        from os import system
        while True:
            print(self)
            time.sleep(1)
            system('cls')
            next(self)
        
if __name__=="__main__":
    c=Clock(minute=59,hour=23,op=1)
    for i in range(60):
        print(next(c))