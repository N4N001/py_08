import turtle
turtle.speed(50000)
def ctverec(strana):
    for x in range(4):
        turtle.fd(strana)
        turtle.lt(90)
def lidlzid(strana):
    ctverec(strana)
    turtle.penup()
    turtle.lt(90)
    turtle.fd(strana / 2)
    turtle.lt(90)
    turtle.fd(strana / 4)
    turtle.lt(135)
    turtle.pendown()
    ctverec(strana)
lidlzid(int(input("Zadej délku strany: ")))
turtle.done()