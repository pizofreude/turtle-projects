# Import necessary library.
from enum import auto
import turtle

# Set color.
colors = ['red', 'green', 'blue', 'silver', 'gold','indigo']

# Initialize turtle module.
t = turtle.Turtle()
screen = turtle.Screen()
screen.bgcolor('grey')
t.speed(10)

# Loop for design.
for i in range(100):
    t.color(colors[i % 6])
    t.fd(i * 5)
    t.left(200)
    t.width(2)

