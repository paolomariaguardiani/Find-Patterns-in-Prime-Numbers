# PROVA 01

from turtle import *
# global colore
# colore = 'blue'
# color(colore)
speed("fastest")
# begin_fill()

numero_passi = 0
for i in range(100):
    print(numero_passi)
    global colore
    colore = 'blue'
    color(colore)
    if numero_passi % 2 == 0:
        colore = 'blue'
    else:
        colore = 'red'
    color(colore)
    for i in range(2):
        forward(numero_passi*2)
        left(90)
    numero_passi += 1


# end_fill()
done()
