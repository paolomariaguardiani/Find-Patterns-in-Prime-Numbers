# PROVA 03

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




# Questa funzione l'ho trovata sul sito:
# http://www.batmath.it/js/primo/primo.htm
# L'ho poi rielaborata per farla fuznionare in python
def trova_numeri_primi(numero):
    global numeroPrimo
    if numero == 0:
        numeroPrimo = False
        print("False")
    elif numero == 1:
        numeroPrimo = True
        print("False")
    if numero == 2:
        numeroPrimo = True
        print("False")
    for i in range(2, numero):
        if numero % i == 0:
            numeroPrimo = False
            break
        if numero % i != 0:
            numeroPrimo = True
    return numeroPrimo

global numeroPrimo
numeroPrimo = 0
num = 2



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
            if trova_numeri_primi(numero):
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
