import turtle
screen = turtle.Screen()
trt1 = turtle.Turtle()
screen.setup(620, 620)
screen.bgcolor('black')
clr = ['red', 'green', 'blue', 'yellow', 'purple']
trt1.pensize(4)
trt1.shape('turtle')
trt1.penup()
trt1.pencolor('red')
m = 0

for i in range(12):
    m = m + 1
    trt1.penup()
    trt1.setheading(-30*i+60)
    trt1.forward(150)
    trt1.pendown()
    trt1.forward(25)
    trt1.penup()
    trt1.forward(20)
    trt1.write(str(m), align = "center", font = ("Arial", 12, "normal"))

    if m == 12:
        m = 0

    trt1.home()

trt1.home()
trt1.setpos(0, -250)
trt1.pendown()
trt1.pensize(10)
trt1.pencolor('blue')
trt1.circle(250)
trt1.penup()
trt1.setpos(150, -270)
trt1.pendown()
trt1.pencolor('olive')
trt1.ht()
