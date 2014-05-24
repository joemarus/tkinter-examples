from Tkinter import *
import random

root = Tk()  # This represents our main window.
root.wm_title("This is a test")

canvas = Canvas(root,width=300, height=300, bg="white")
canvas.pack()
x1=random.randint(5,250)
y1=random.randint(5,250)
x2=random.randint(5,250)
y2=random.randint(5,250)
dx1=random.randint(-10,10)
dy1=random.randint(-10,10)
dx2=random.randint(-10,10)
dy2=random.randint(-10,10)

def draw_stuff():
    #col="#" + str(r) + str(b) + str(g)
    global x1, y1, x2, y2, dx1, dx2, dy1, dy2
    canvas.create_line(x1,y1, x2, y2)
    x1=x1+dx1
    y1=y1+dy1
    x2=x2+dx2
    y2=y2+dy2
    if x1<=0:
        dx1=-dx1
        x1=1
    if x1>=300:
        dx1=-dx1
        x1=299
    if x2<=0:
        dx2=-dx2
        x2=1
    if x2>=300:
        dx2=-dx2
        x2=299
    if y1<=0:
        dy1=-dy1
        y1=1
    if y1>=300:
        dy1=-dy1
        y1=299
    if y2<=0:
        dy2=-dy2
        y2=1
    if y2>=300:
        dy2=-dy2
        y2=299
    canvas.after(100, func=draw_stuff)

canvas.after(100, func=draw_stuff)

root.mainloop()
