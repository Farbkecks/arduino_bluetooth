import tkinter as tk

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

label_verbindung = tk.Label(root, text="bluetooth Verbindung", bg="red")
label_verbindung.pack(fill="both");
label_verbindung.config(width=400, height=100)

lable_w = tk.Label(root, text="Motor", bg="red")
lable_w.pack(expand=True, fill="both")
lable_w.config(width=400, height=100)

lable_a = tk.Label(root, text="drehung links", bg="red")
lable_a.pack(expand=True,side= "left", fill="both")
lable_a.config(width=400, height=100)

lable_d = tk.Label(root, text="drehung rechts", bg="red")
lable_d.pack(expand=True,side = "right", fill="both")
lable_d.config(width=400, height=100)


root.mainloop()