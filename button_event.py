import tkinter as tk

def processOk():
    print("Ok button is clicked!!!")

def processCancel():
    print("Cancel button is clicked!!!")

window = tk.Tk()
window.geometry("300x300")

btnOk = tk.Button(window, text="Ok", fg="red", command=processOk)
btncancel = tk.Button(window, text="Cancel", bg="orange", command=processCancel)

btnOk.pack()
btncancel.pack()



window.mainloop() #Create an event loop