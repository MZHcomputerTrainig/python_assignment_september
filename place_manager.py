import tkinter as tk

class PlaceManagerDemo:
    window=tk.Tk()
    window.title("Place Manager Demo 2")
    tk.Label(window,text="blue",bg="blue").place(x=20,y=20)
    tk.Label(window,text="red",bg="red").place(x=50,y=50)
    tk.Label(window,text="green",bg="green").place(x=80,y=80)
    window.mainloop()

PlaceManagerDemo()