# PROVA 01

from turtle import *
# global colore
# colore = 'blue'
# color(colore)
speed("slowest")
# begin_fill()
global numero
numero = 0
global numero_passi
numero_passi = 1

for i in range(100):
    # print(numero_passi)
    global colore

    print(numero)
    colore = 'blue'
    color(colore)
    pensize(2)
    for i in range(2):
        # for i in (numero_passi):
        for i in range(numero_passi):
            if numero % 2 == 0:
                colore = 'blue'
            else:
                colore = 'red'
            color(colore)
            forward(10)
            numero += 1
        # forward(numero_passi*2)
        left(90)
        numero_passi += 1


# end_fill()
done()
