import tkinter as tk

class PackManagerDemo:
    def __init__(self) :
        window=tk.Tk()
        window.title("Pack Manager Demo 1")

        l1 = tk.Label(window,text="red",bg="red")
        l1.pack()

        l2 = tk.Label(window,text="blue",bg="blue")
        l2.pack(fill="both",expand=1)
        
        l3 = tk.Label(window,text="green",bg="green")
        l3.pack(fill="both")
        
        window.mainloop()

PackManagerDemo()
