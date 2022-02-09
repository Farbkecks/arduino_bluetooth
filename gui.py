import tkinter as tk
from time import sleep

# https://realpython.com/python-gui-tkinter/


def keydown(event):
    sleep(.01)
    if event.char == 'w':
        frame2.config(bg="green", relief=tk.SUNKEN)
        label_2.config(bg="green")
    elif event.char == 'a':
        frame3.config(bg="green", relief=tk.SUNKEN)
        label_3.config(bg="green")
    elif event.char == 'd':
        frame4.config(bg="green", relief=tk.SUNKEN)
        label_4.config(bg="green")

def keyup(event):
    sleep(.01)
    if event.char == 'w':
        frame2.config(bg="red", relief=tk.GROOVE)
        label_2.config(bg="red")
    elif event.char == 'a':
        frame3.config(bg="red", relief=tk.GROOVE)
        label_3.config(bg="red")
    elif event.char == 'd':
        frame4.config(bg="red", relief=tk.GROOVE)
        label_4.config(bg="red")

root = tk.Tk()

h= 300
w= 400
ws = root.winfo_screenwidth() # width of the screen
hs = root.winfo_screenheight() # height of the screen
# calculate x and y coordinates for the Tk root window
x = (ws/2) - (w/2)
y = (hs/2) - (h/2)
root.geometry('%dx%d+%d+%d' % (w, h, x, y-100))
root.resizable(width=False, height=False)

root.title("Steuerung für Arduino")

frame1 = tk.Frame(master=root, height=100, width=400, bg="red", relief=tk.RIDGE, borderwidth=5)
frame1.place(x=0)

frame2 = tk.Frame(master=root, height=100,width=400, bg="red", relief=tk.GROOVE, borderwidth=5)
frame2.place(y=100)

frame3 = tk.Frame(master=root, height=100,width=200, bg="red", relief=tk.GROOVE, borderwidth=5)
frame3.place(y=200)

frame4 = tk.Frame(master=root, height=100,width=200, bg="red", relief=tk.GROOVE, borderwidth=5)
frame4.place(y=200,x=200)


frame1.pack_propagate(0)
label_1 = tk.Label(frame1, text="Verbindung",bg="red", font=("Courier", 30))
label_1.pack(fill=tk.BOTH, expand=True)
frame2.pack_propagate(0)
label_2 = tk.Label(text="W", master=frame2,bg="red", font=("Courier", 30))
label_2.pack(fill=tk.BOTH, expand=True)
frame3.pack_propagate(0)
label_3 = tk.Label(text="A", master=frame3,bg="red", font=("Courier", 30))
label_3.pack(fill=tk.BOTH, expand=True)
frame4.pack_propagate(0)
label_4 = tk.Label(text="D", master=frame4,bg="red", font=("Courier", 30))
label_4.pack(fill=tk.BOTH, expand=True)

root.bind("<KeyPress>", keydown)
root.bind("<KeyRelease>", keyup)

label_1.config(bg="green")
frame1.config(bg="green")

root.mainloop()
