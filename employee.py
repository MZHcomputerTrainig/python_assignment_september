class Employees():
    def __init__ (self, Name, Salary):
        self.Name =Name
        self.Salary =Salary

    def details(self):
        print ("Employee Name:" , self.Name)
        print ("Employee Salary:" , self.Salary)
        print("\n")

first = Employees("John", 100000)
Second = Employees("Doe", 200000)
Third = Employees("John", 100000)

first.details()
Second.details()
Third.details()
     