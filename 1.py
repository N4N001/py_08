import turtle
turtle.speed(50000)
def ctverec(strana):
    for x in range(4):
        turtle.fd(strana)
        turtle.lt(90)
def ctverecvectverci(strana):
    ctverec(strana)
    turtle.penup()
    turtle.fd(strana / 100 * 20)
    turtle.lt(90)
    turtle.fd(strana / 100 * 20)
    turtle.rt(90)
    turtle.pendown()
    ctverec(strana / 100 * 60)
ctverecvectverci(int(input("Zadej délku strany: ")))
turtle.done()