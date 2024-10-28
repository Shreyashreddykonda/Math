import turtle
import math

s1 = turtle.Screen()
s1.setup(800, 800)
s1.bgcolor("light green")

t1 = turtle.Turtle()
t2 = turtle.Turtle()
t3 = turtle.Turtle()
t1.color("blue")
t2.color("yellow")
t1.shape('circle')
t3.shape('circle')

t1.goto(0, 0)
t2.goto(0, 0)
t2.begin_fill()
t2.circle(30)
t2.end_fill()
t1.pendown()

theta = 0
theta1 = 0
phi = 30
phi2 = 120
a = 150
b = 75

theta1 = math.radians(theta)
x1 = a*math.cos(theta1)
y1 = b*math.cos(theta1)
t1.penup()

while True:
    for theta in range(0, 360, 1):
        theta1 = math.radians(theta)
        phi1 = math.radians(phi)
        phi21 = math.radians(phi2)
        x1 = a*math.cos(theta1)
        y1 = b*math.sin(theta1)
        x11 = x1*math.cos(phi1) - y1*math.sin(phi1)
        y11 = y1*math.cos(phi1) + x1*math.sin(phi1)
        x21 = x1*math.cos(phi21) - y1*math.sin(phi21)
        y21 = y1*math.cos(phi21) + x1*math.sin(phi21)

        t1.goto(x11, y11)
        t3.goto(x21, y21)
