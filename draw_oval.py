import tkinter as tk
def draw_oval():
    canvas.create_oval(100, 100, 250, 150, outline='blue', fill='yellow', width=2)
    # Create the main window
window = tk.Tk()
window.title("Oval Canvas Example")
# Create a Canvas widget
canvas = tk.Canvas(window, width=300, height=200)
canvas.pack()
# Create an Oval on the Canvas
draw_oval()
# Start the main event loop
window.mainloop()
