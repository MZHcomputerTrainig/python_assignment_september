import tkinter as tk

class GridManagerDemo:
    window = tk.Tk()
    window.title("Grid Manager Demo")
    message = tk.Message(window,text='This message widget occupies three rows and two columns')
    message.grid(row=1,column=1,rowspan=3,columnspan=2)

    tk.Label(window,text="First Name:").grid(row=1,column=3)
    tk.Entry(window).grid(row=1,column=4,padx=5,pady=5)

    tk.Label(window,text="Last Name:").grid(row=2,column=3)
    tk.Entry(window).grid(row=2,column=4,padx=5,pady=5)

    tk.Button(window,text="Get Name").grid(row=3,column=3,padx=5,pady=5,sticky="S")
    
    window.mainloop()

GridManagerDemo()