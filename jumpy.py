#!/usr/bin/env python
#
# Jumpy!  
# A simple example of a game made with the pyglet library.
#
import pyglet
from pyglet.window import key

# Let's create a window with all the defaults
window = pyglet.window.Window()

# Pyglet has a nice helper function to keep track of the keyboard:
keys = key.KeyStateHandler()
window.push_handlers(keys)

# Pyglet can do sound!  Let's load in a sound to use later.
sound = pyglet.resource.media('ball.wav', streaming=False)

# Let's set up some variables
dy = 0  # speed in the y direction
dx = 0  # speed in the x direction
a  = 10  # acceleration due to "gravity"
left = False  # is the player going left
right= False  # is the player going right

# Pylget draws on the screen with "sprites" which use images
# loaded from files.  You can have many sprites using the same
# image.
ball_image = pyglet.resource.image('ball.png')
ball_sprite= pyglet.sprite.Sprite(ball_image)

# Here is where we handle keyboard events
#@window.event
#def on_key_press(symbol, modifiers):
#    global dy, dx, left, right
#    if symbol == key.SPACE and ball_sprite.y == 0:
#        dy = 150  # jump up!
#        sound.play()
#    elif symbol == key.ESCAPE:
#        window.has_exit = True

# This is where all the drawing occurs
@window.event
def on_draw():
    window.clear()
    ball_sprite.draw()
    
# This routine gets called repeatedly to do all our motion calculations.
def update(dt):
    global dx, dy
    if keys[key.SPACE] and ball_sprite.y == 0:
        dy = 150
        sound.play()
    if ball_sprite.y > 0:
        dy -= a
    if ball_sprite.y == 0: 
        if keys[key.RIGHT]:  # if the right arrow key is down
            dx = 200
        elif keys[key.LEFT]:  # if the left arrow key is down
            dx = -200
        else:
            dx = 0
    ball_sprite.x += dx * dt
    ball_sprite.y += dy * dt
    if ball_sprite.y < 0: ball_sprite.y = 0
    if ball_sprite.x < 0: ball_sprite.x = 0
    if ball_sprite.x > (window.width-ball_sprite.width):
        ball_sprite.x = window.width-ball_sprite.width
    
# Let's call the update function every 1/20 of a second
pyglet.clock.schedule_interval(update, 1/30.)
    
# This statement is a requirement to keep the window open and receiving events.
# Hit the ESC key to quit the program.    
pyglet.app.run()
