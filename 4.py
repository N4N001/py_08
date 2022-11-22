import turtle    
turtle.speed(50000)
def nekolikactverec(strana, pocet):
        for x in range(pocet):
            turtle.fd(strana / 2)
            for x in range(3):
                turtle.lt(90)
                turtle.fd(strana)
            turtle.lt(90)
            turtle.fd(strana / 2)
            turtle.rt(360 / pocet)
nekolikactverec(int(input("Zadej velikost strany: ")), int(input("Zadej počet čtverců: ")))
turtle.done()