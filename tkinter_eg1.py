import tkinter as tk
root = tk.Tk() #Create a window
root.geometry('300x300') 

# Use root.geometry to set the window size
label = tk.Label(root, text="Hello, tkinter!")#Create Label
button = tk.Button(root, text="Click Me")#Create a Button


label.pack() #Place the label in the window
button.pack() #Place the button in the window


root.mainloop() #Create an event loop
