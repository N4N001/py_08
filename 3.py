import turtle
turtle.speed(50000)
def ctverec(strana):
    for x in range(4):
        turtle.fd(strana)
        turtle.lt(90)
def pressebe(strana, pocet):
        for x in range(pocet):
            ctverec(strana)
            turtle.penup()
            turtle.fd(strana / 2)
            turtle.lt(90)
            turtle.fd(strana / 2)
            turtle.rt(90)
            turtle.pendown()
pressebe(int(input("Zadej délku strany: ")), int(input("Zadej počet čtverců: ")))
turtle.done()