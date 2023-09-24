#animal is class
class animal:
    number_of_legs = 0

    def __init__(self, legs = 4):
        self.number_of_legs = legs

dog = animal()

print ("Dog has {} legs".format(dog.number_of_legs))

spider = animal(8)

print ("Spider has {} legs".format(spider.number_of_legs))