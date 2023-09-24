# Function to prepare the dough
def prepare_dough():
    print("Preparing the dough...")

# Function to add toppings
def add_toppings():
    print("Adding toppings...")

# Function to bake the pizza
def bake_pizza():
    print("Baking the pizza...")


#calling function

prepare_dough()
add_toppings()
bake_pizza()

print("*********************************")

def printHello(val):
    print("Hello",val)

printHello("World")
printHello("Tr Autumn")
print("*********************************")

def sum(num1,num2):
    return num1+num2
print("Sum:", sum(5,10))
print("*********************************")


def max(lst):
    maxnumber = lst[0]
    for x in lst:
        if maxnumber <x:
            maxnumber = x
    return maxnumber

list = [1000,99,1020]
list1 = [1,2,3,4,5,6,7,8,9]
print("Maxmium number in array list is",max(list))
print("Maxmium number in array list1 is",max(list1))
