#!/usr/bin/env python
#
# A demo of drawing on the canvas widget
# using Tkinter.
#
# by Joseph Maruschek (joe.maruschek@gmail.com)
#
from Tkinter import *
import random

root = Tk()  # this represents our main window
root.wm_title("Canvas Demo")

drawing = False  # a flag to see if we are drawing
id = 0           # an id so we can stop the timer
v = IntVar()     # a variable to use with the radio buttons
v.set(1)         # let's initialize it to 1 (circles)
# 
# Let's first place a canvas widget in the window
canvas = Canvas(root,width=400, height=400, bg="white")
canvas.pack()

# This is where we do all the drawing.  We will create some random
# coordinates and a random color, then draw circles, ovals, or rectangles.
def draw_stuff():
    global id
    x=random.randint(0,350)
    y=random.randint(0,350)
    d=random.randint(10,200)
    d2=random.randint(10,200)
    r=random.randint(0,255)
    g=random.randint(0,255)
    b=random.randint(0,255)
    col="#{0:02x}{1:02x}{2:02x}".format(r,g,b)
    if v.get()==1:  
        canvas.create_oval(x,y, x+d,y+d, fill=col)
    elif v.get()==2:
        canvas.create_oval(x,y, x+d,y+d2, fill=col)
    elif v.get()==3:
        canvas.create_rectangle(x,y, x+d,y+d2, fill=col)
    # This will call this same function again after .25 seconds.
    id = canvas.after(250, func=draw_stuff) 

# This lets us toggle between drawing and not drawing.
def start_stop():
    global drawing
    if drawing:
        draw_btn['text']="Start Drawing"  # This is how to change the options on the widget
        clear_btn['state']=NORMAL
        canvas.after_cancel(id)  # this stops the timer
        drawing = False
    else:
        draw_btn['text']="Stop Drawing"
        clear_btn['state']=DISABLED
        drawing=True
        draw_stuff()  # start drawing!

def clear_canvas():
    canvas.delete(ALL)

# Here are some button widgets.
draw_btn = Button(root,text="Start Drawing", command=start_stop)
draw_btn.pack(pady="5")  # pady is padding in the y direction, so that the buttons
                         # are not that close together.
clear_btn = Button(root,text="Clear Canvas", command=clear_canvas)
clear_btn.pack(pady="5")

# I'm going to use a loop to create the radio buttons using the data
# in this array (of arrays).
radio_btn_info = [
    ["Circles", 1 ],
    ["Ovals", 2 ],
    ["Rectangles", 3 ]  ]
# To make the radio buttons line up, we will place them inside 
# a Frame widget, which is an invisible container we can put other
# widgets in.
frame=Frame(root)
for txt, val in radio_btn_info:
    rbtn = Radiobutton(frame,text=txt, value=val, variable=v)
    rbtn.pack(anchor="w")  # this places the widget to the "west" or left side
frame.pack(pady="5")  # we still need to place the frame into the window

# To finish things off, we call the required mainloop function to keep
# the window shown and to process events.
root.mainloop()
