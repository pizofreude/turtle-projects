# Import necessary library.
import turtle as t

# Initialize turtle module.
screen = t.Screen()
screen.bgcolor('grey')
t.tracer(500)
t.pensize(10)
colors = ['red','yellow','blue']
t.rt(4)

# Loop for design.
for i in range(150):
    t.color(colors[i % 3])
    t.up()
    t.circle(150-i, -100)
    t.down()
    t.circle(150-i, -100)

# This function is used to starts event loop – calling Tkinter’s main loop
## function. It does not require any argument.
## Must be the last statement in a turtle graphics program.
## Must NOT be used if a script is run from within IDLE in -n mode 
# (No subprocess) – for interactive use of turtle graphics.
t.done()


