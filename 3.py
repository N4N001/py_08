import turtle
turtle.speed(50000)
def ctverec(strana):
    for i in range(4):
        turtle.pendown()
        turtle.fd(strana)
        turtle.lt(90)
        turtle.penup()
def pressebe(strana, pocet):
        for i in range(pocet):
            ctverec(strana)
            turtle.goto((i*strana / 2)+(strana / 2), (i*strana / 2)+(strana / 2))
pressebe(int(input("Zadej délku strany: ")), int(input("Zadej počet čtverců: ")))
turtle.done()