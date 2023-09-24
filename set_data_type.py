#Let's create a set of your favourite fruits
favourite_fruits = {"apple", "banana", "orange"}

#Now, let's print the set
print(favourite_fruits)

#Adding a new fruit to the set
favourite_fruits.add("grapes")
print(favourite_fruits)

#Trying to add a duplicate fruit (apple)
favourite_fruits.add("apple")
print(favourite_fruits)

#Removing a fruit from the set
favourite_fruits.remove("apple")
print(favourite_fruits)

#Checking if the fruit is in the
print("apple" in favourite_fruits)# This will print False

#Checking the number length of fruits in the set
print(len(favourite_fruits)) #This will print the number of fruits in the set