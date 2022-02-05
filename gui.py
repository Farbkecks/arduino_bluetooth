import tkinter as tk

# https://realpython.com/python-gui-tkinter/

root = tk.Tk()

w= 400
ws = root.winfo_screenwidth() # width of the screen
hs = root.winfo_screenheight() # height of the screen
# calculate x and y coordinates for the Tk root window
x = (ws/2) - (w/2)
y = (hs/2) - (w/2)
root.geometry('%dx%d+%d+%d' % (w, w, x, y-100))
root.resizable(width=False, height=False)

root.title("Steuerung für Arduino")

frame1 = tk.Frame(master=root, height=100, width=400, bg="green", relief=tk.RIDGE, borderwidth=5)
frame1.pack_propagate(0)

frame1.place(x=0)

frame2 = tk.Frame(master=root, height=200,width=400, bg="yellow", relief=tk.GROOVE, borderwidth=5)
frame2.place(y=100)

frame3 = tk.Frame(master=root, height=100,width=200, bg="blue", relief=tk.SUNKEN, borderwidth=5)
frame3.place(y=300)

frame4 = tk.Frame(master=root, height=100,width=200, bg="green", relief=tk.GROOVE, borderwidth=5)
frame4.place(y=300,x=200)

label1 = tk.Label(text="Verbindung", master=frame1)
label1.config(bg="green", font=("Courier", 30))
label1.pack(fill=tk.BOTH, expand=True)


root.mainloop()