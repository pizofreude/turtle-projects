# Import necessary modules.
import turtle as t
import colorsys

# Tracer config.
t.bgcolor('grey')
t.tracer(100)
t.width(5)  # Try 7.

# Initialize.
h = 0
n = 88  # Try 87.

# Loop for graphic design.
for i in range(2000):
    cs = colorsys.hsv_to_rgb(h, 1, .9)
    h += 1/n
    t.setposition(0, 0)  # Try (0, 100).
    t.pencolor(cs)
    t.left(50)
    t.circle(10)
    t.backward(42)
    t.rt(56)
    t.fd(i)
    t.bk(575)

# Execute design process.
t.done()