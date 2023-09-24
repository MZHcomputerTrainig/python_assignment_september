#animal is class
class animal:
    number_of_legs = 0
    def sleep(self):
        print("zzzzzzzzzzzzzz")
    
    def bark(self):
        print ("woff  woff")

#dog is object of animal class
dog = animal()

dog.number_of_legs = 4


#print("Dog has" + str(dog.number_of_legs) + "legs")

print ("Dog has {} legs".format(dog.number_of_legs))

dog.bark()
dog.sleep()

#dog is object of animal class
chicken = animal()

chicken.number_of_legs = 4

#print("Dog has" + str(dog.number_of_legs) + "legs")

print ("Chicken has {} legs".format(chicken.number_of_legs))
