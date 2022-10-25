# Import necessary library.
import turtle as t

# Initialize turtle module. Hint: https://www.eg.bucknell.edu/~hyde/Python3/TurtleDirections.html
# t.position()
# t.goto(0, -100)
t.sety(-300)
screen = t.Screen()
screen.bgcolor('grey')
t.tracer(25)
t.pensize(7)
colors = ['gold','blue']
# t.rt(4)

# Loop for design.
for i in range(300):
    t.color(colors[i % 2])
    t.up()
    t.circle(300-i, -92)
    t.down()
    t.circle(300-i, -92)

# This function is used to starts event loop – calling Tkinter’s main loop
## function. It does not require any argument.
## Must be the last statement in a turtle graphics program.
## Must NOT be used if a script is run from within IDLE in -n mode 
# (No subprocess) – for interactive use of turtle graphics.
t.done()


