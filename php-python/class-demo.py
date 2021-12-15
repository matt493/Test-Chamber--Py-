class Person:
    def _init_(self,fname,lname):
        self.firstname=fname
        self.lastname=lname
    def printname(self):
        print(self.firstname,self.lastname)
    pass
x=Person("John","Doe")
x.printname()
class Student(Person):
    def _init_(self,fname,lname,year):
        super()._init_(fname,lname)
        self.gyear=year
    def welcome(self):
        print("Welcome ",self.firstname,"to the class ",self.gyear)
    pass
    
x=Student("Mathew", "Reji", 1997)
x.printname()
x.welcome()