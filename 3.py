import turtle
turtle.speed(50000)
def ctverec(strana):
    for i in range(4):
        turtle.fd(strana)
        turtle.lt(90)
def pressebe(strana, pocet):
        for i in range(pocet):
            ctverec(strana)
            turtle.penup()
            x=turtle.pos()
            turtle.goto(x[1]+strana / 2,x[2]+strana / 2)
            turtle.pendown()
pressebe(int(input("Zadej délku strany: ")), int(input("Zadej počet čtverců: ")))
turtle.done()