import tkinter as tk

class PackManagerDemoWithSide:
    window=tk.Tk()
    window.title("Pack Manager Demo 2")
    tk.Label(window,text="blue",bg="blue").pack(side="left")
    tk.Label(window,text="red",bg="red").pack(side="left",fill="both",expand=1)
    tk.Label(window,text="green",bg="green").pack(side="left",fill="both")
    window.mainloop()

PackManagerDemoWithSide()