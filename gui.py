import tkinter as tk
import threading
from time import sleep
import serial

# https://realpython.com/python-gui-tkinter/

class GUI:
    def __init__(self, root, iterate):
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

        self.w = False
        self.a = False
        self.d = False

        self.iterate = iterate
        self.port = "COM5"

    def keydown(self, event):
        if event.char == 'w':
            self.frame2.config(bg="green", relief=tk.SUNKEN)
            self.label_2.config(bg="green")
            self.w = True
        elif event.char == 'a':
            self.frame3.config(bg="green", relief=tk.SUNKEN)
            self.label_3.config(bg="green")
            self.a = True
        elif event.char == 'd':
            self.frame4.config(bg="green", relief=tk.SUNKEN)
            self.label_4.config(bg="green")
            self.d = True

    def keyup(self, event):
        if event.char == 'w':
            self.frame2.config(bg="red", relief=tk.GROOVE)
            self.label_2.config(bg="red")
            self.w = False
        elif event.char == 'a':
            self.frame3.config(bg="red", relief=tk.GROOVE)
            self.label_3.config(bg="red")
            self.a = False
        elif event.char == 'd':
            self.frame4.config(bg="red", relief=tk.GROOVE)
            self.label_4.config(bg="red")
            self.d = False

    def send(self):
        print("Sending")

        info = [0,0]
        if self.a:
            info[0] = 1
        elif self.d:
            info[0] = 2
        if self.w:
            info[1] = 1
        sleep(.1)
        self.bluetooth.write(str.encode(f"{info[0]}{info[1]}"))

        self.root.after(self.iterate, self.send)

    def verbindung_on(self):
        sleep(1)

        self.bluetooth=serial.Serial(self.port, 9600)
        self.bluetooth.flushInput() #This gives the bluetooth a little kick

        self.label_1.config(bg="green")
        self.frame1.config(bg="green")

        self.root.after(self.iterate, gui.send)

if __name__ == "__main__":
    root = tk.Tk()
    gui = GUI(root, 100)
    x = threading.Thread(target=gui.verbindung_on, daemon=True)
    x.start()

    root.mainloop()
