import tkinter as tk

def fun_ok():
    print ("Your name is", name.get())

window = tk.Tk()

label = tk.Label(window,text="Enter your Name:")
name = tk.StringVar()

entry = tk.Entry(window,textvariable=name)

btn = tk.Button(window,text="OK", command=fun_ok)
label.pack()
entry.pack()
btn.pack()
window.mainloop()