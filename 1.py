import turtle
turtle.speed(50000)
def ctverec(strana):
    for x in range(4):
        turtle.pendown()
        turtle.fd(strana)
        turtle.lt(90)
        turtle.penup()
def ctverecvectverci(strana):
    ctverec(strana)
    turtle.goto(strana / 100 * 20, strana / 100 * 20)
    ctverec(strana / 100 * 60)
ctverecvectverci(int(input("Zadej délku strany: ")))
turtle.done()