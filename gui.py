import tkinter as tk
from time import sleep

# https://realpython.com/python-gui-tkinter/


class GUI:
    def __init__(self, root):
        self.root = root
        self.h= 300
        self.w= 400
        self.ws = root.winfo_screenwidth() # width of the screen
        self.hs = root.winfo_screenheight() # height of the screen
        # calculate x and y coordinates for the Tk root window
        self.x = (self.ws/2) - (self.w/2)
        self.y = (self.hs/2) - (self.h/2)
        self.root.geometry('%dx%d+%d+%d' % (self.w, self.h, self.x, self.y-100))
        self.root.resizable(width=False, height=False)
        
        self.root.title("Steuerung für Arduino")

        self.frame1 = tk.Frame(master=self.root, height=100, width=400, bg="red", relief=tk.RIDGE, borderwidth=5)
        self.frame1.place(x=0)
        
        self.frame2 = tk.Frame(master=self.root, height=100,width=400, bg="red", relief=tk.GROOVE, borderwidth=5)
        self.frame2.place(y=100)
        
        self.frame3 = tk.Frame(master=self.root, height=100,width=200, bg="red", relief=tk.GROOVE, borderwidth=5)
        self.frame3.place(y=200)
        
        self.frame4 = tk.Frame(master=self.root, height=100,width=200, bg="red", relief=tk.GROOVE, borderwidth=5)
        self.frame4.place(y=200,x=200)
        
        
        self.frame1.pack_propagate(0)
        self.label_1 = tk.Label(self.frame1, text="Verbindung",bg="red", font=("Courier", 30))
        self.label_1.pack(fill=tk.BOTH, expand=True)
        self.frame2.pack_propagate(0)
        self.label_2 = tk.Label(text="W", master=self.frame2,bg="red", font=("Courier", 30))
        self.label_2.pack(fill=tk.BOTH, expand=True)
        self.frame3.pack_propagate(0)
        self.label_3 = tk.Label(text="A", master=self.frame3,bg="red", font=("Courier", 30))
        self.label_3.pack(fill=tk.BOTH, expand=True)
        self.frame4.pack_propagate(0)
        self.label_4 = tk.Label(text="D", master=self.frame4,bg="red", font=("Courier", 30))
        self.label_4.pack(fill=tk.BOTH, expand=True)

        self.root.bind("<KeyPress>", self.keydown)
        self.root.bind("<KeyRelease>", self.keyup)

    def keydown(self, event):
        # sleep(.01)
        if event.char == 'w':
            self.frame2.config(bg="green", relief=tk.SUNKEN)
            self.label_2.config(bg="green")
        elif event.char == 'a':
            self.frame3.config(bg="green", relief=tk.SUNKEN)
            self.label_3.config(bg="green")
        elif event.char == 'd':
            self.frame4.config(bg="green", relief=tk.SUNKEN)
            self.label_4.config(bg="green")

    def keyup(self, event):
        # sleep(.01)
        if event.char == 'w':
            self.frame2.config(bg="red", relief=tk.GROOVE)
            self.label_2.config(bg="red")
        elif event.char == 'a':
            self.frame3.config(bg="red", relief=tk.GROOVE)
            self.label_3.config(bg="red")
        elif event.char == 'd':
            self.frame4.config(bg="red", relief=tk.GROOVE)
            self.label_4.config(bg="red")

def send():
    print("Sending")


root = tk.Tk()
gui = GUI(root)

gui.label_1.config(bg="green")
gui.frame1.config(bg="green")

root.mainloop()
