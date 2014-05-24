from Tkinter import *
import random

root = Tk()
root.wm_title("This is a test")

canvas = Canvas(root,width=300, height=300, bg="white")
canvas.pack()

def draw_stuff():
    x=random.randint(5,250)
    y=random.randint(5,250)
    d=random.randint(10,100)
    r=random.randint(0,9)
    g=random.randint(0,9)
    b=random.randint(0,9)
    col="#" + str(r) + str(b) + str(g)
    canvas.create_oval(x,y, x+d,y+d, fill=col)
    canvas.after(500, func=draw_stuff)

canvas.after(500, func=draw_stuff)

root.mainloop()
