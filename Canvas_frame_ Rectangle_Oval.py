import tkinter as tk

class CanvasDemo:
    def __init__(self):
        window = tk.Tk()
        window.title("Canvas Demo")
        self.canvas= tk.Canvas(window, width=200, height=200)
        self.canvas.pack()
        frame =  tk.Frame(window)
        frame.pack()
        btnRectangle = tk.Button(frame,text="Rectangle",command= self.displayRect)
        btnOval = tk.Button(frame,text="Oval",command= self.displayOval)
       
        btnRectangle.pack()
        btnOval.pack()
        window.mainloop()

    def displayRect(self):
        self.canvas.create_rectangle(8,8,120,60,fill='red',tags='rect')
    
    def displayOval(self):
        self.canvas.create_oval(10,10,190,90,fill='red',tags='oval')

CanvasDemo()


