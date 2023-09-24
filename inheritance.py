#parent class (base class)
class Person:
    def __init__(self, fname, lname):
        self.firstname = fname
        self.lastname = lname

    def printname(self):
        print(self.firstname, self.lastname)
#Use the Person class to create an object, and then execute the printname method:  x = Person("John", "Doe")
x = Person("John", "Doe")

x.printname()

#Child class (derived class)
class Student(Person):
    def __init__ (self, fname, lname, year): 
        super().__init__(fname, lname)
        self.graduationyear = year 

    def printname(self):
        super().printname()
        print('year',  self.graduationyear)

    def welcome(self):
        print("Welcome", self.firstname, self.lastname, "to the class of",  self.graduationyear)


x = Student("Mike", "Olsen",2023)  
x.printname()
x.welcome()
