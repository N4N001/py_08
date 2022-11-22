import turtle
turtle.speed(50000)
def ctverec(strana):
    for x in range(4):
        turtle.pendown()
        turtle.fd(strana)
        turtle.lt(90)
        turtle.penup()
def rotace(strana, pocet):
    for x in range(pocet):
        ctverec(strana)
        turtle.goto(strana / 4 * (-1), strana / 2)
        turtle.rt(90 / pocet)
        ctverec(strana)
rotace(int(input("Zadej délku strany: ")), int(input("Zadej počet čtverců: ")))
turtle.done()