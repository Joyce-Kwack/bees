import turtle as trtl
import time 

screen = trtl.Screen()
screen.tracer(0)  # Turn off automatic updates

t = trtl.Turtle()

def draw_bee(x, y):
    t.clear()  # Erase previous drawing
    t.penup()
    t.goto(x, y)
    t.pendown() # Draw body of bee
    t.pensize(10)
    t.fillcolor("yellow")
    t.begin_fill()
    t.circle(30)
    t.end_fill()
    t.penup()
    t.forward(10) # Draw stripes 
    t.left(90)
    t.forward(4)
    t.pendown()
    t.forward(55)
    t.left(180)
    t.forward(58)
    t.penup()
    t.right(90)
    t.forward(25)
    t.right(90)
    t.forward(3)
    t.pendown()
    t.forward(50)
    t.penup() # Draw wings
    t.right(90)
    t.forward(10)
    t.left(90)
    t.forward(5)
    t.right(90)
    t.pendown()
    t.left(40)
    t.circle(20,180)
    t.circle(25,110)
    t.penup()
    t.right(90)
    t.forward(12)
    t.left(120)
    t.pendown()
    t.circle(25,-110)
    t.circle(20,-45)
    t.left(155)


    screen.update()  # Refresh the screen

# Draw at the first position
draw_bee(0, 0)

# Ask user how many flowers they want to pollinate
flower = int(input("How many flowers do you want to pollinate?:"))
# Move and redraw after 0.1 seconds
# Use flower as the number of times the bee is redrawn
# Use flower as the distance
if flower == 0:
    print ("No flowers pollinated :(")
else:
    for step in range(0,flower):
        distance=(step*200)-280
        screen.ontimer(draw_bee(distance, 0), 100)

wn = trtl.Screen()
wn.mainloop()
