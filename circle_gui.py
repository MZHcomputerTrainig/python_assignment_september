import math
import tkinter as tk
from tkinter import Label, Entry, Button

class Circle:
    def __init__(self, radius=1):
        self.radius = radius

    def getPerimeter(self):
        return 2 * self.radius * math.pi
    
    def getArea(self):
        return self.radius * self.radius * math.pi
    
    def setRadius(self, radius):
        self.radius = radius

def calculate():
    radius = float(radius_entry.get())
    c1 = Circle(radius)
    perimeter = c1.getPerimeter()
    area = c1.getArea()
    perimeter_label.config(text=f"Perimeter: {perimeter}")
    area_label.config(text=f"Area: {area}")

# Create a GUI window
root = tk.Tk()
root.title("Circle Calculator")
root.geometry("500x500")  # Set window width and height

# Create an input entry for radius
radius_label = Label(root, text="Enter Radius:")
radius_label.pack()
radius_entry = Entry(root)
radius_entry.pack()

# Create a button to calculate
calculate_button = Button(root, text="Calculate", command=calculate)
calculate_button.pack()

# Create labels to display the results
perimeter_label = Label(root, text="Perimeter:")
area_label = Label(root, text="Area:")

# Pack labels into the window
perimeter_label.pack()
area_label.pack()

# Start the GUI main loop
root.mainloop()
