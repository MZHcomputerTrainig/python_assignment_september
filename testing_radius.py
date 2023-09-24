from circle_class import Circle

def main():
    # Create a cirle-1 with radus 1
    circle1 = Circle()
    print("The area of the circle 1  of radius",circle1.radius,
        "is", circle1.getArea()  )
    
     # Create a cirle-2 with radus 25
    circle2 = Circle(25)
    print("The area of the circle 2  of radius",circle2.radius,
        "is", circle2.getArea()  )
    
      # Create a cirle-3 with radus 125
    circle3 = Circle(125)
    print("The area of the circle 3 of radius",circle3.radius,
        "is", circle3.getArea()  )
    
      # Modify  cirle-2 with radus 100
    circle2.radius = 100
    print("The area of the circle 2 of radius",circle2.radius,
        "is", circle2.getArea()  )


main() #call the main function