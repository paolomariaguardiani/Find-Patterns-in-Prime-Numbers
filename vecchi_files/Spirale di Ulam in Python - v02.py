# PROVA 03

from turtle import *
# global colore
# colore = 'blue'
# color(colore)
speed(0)
# begin_fill()
global numero
numero = 0
global numero_passi
numero_passi = 0
global numero_lati
numero_lati = 4
bgcolor('black')




# Questa funzione l'ho trovata sul sito:
# http://www.batmath.it/js/primo/primo.htm
# L'ho poi rielaborata per farla fuznionare in python
def trova_numeri_primi(numero):
    global numeroPrimo
    if numero == 0:
        numeroPrimo = False
    elif numero == 1:
        numeroPrimo = True
    if numero == 2:
        numeroPrimo = True
    for i in range(2, numero):
        if numero % i == 0:
            numeroPrimo = False
            break
        if numero % i != 0:
            numeroPrimo = True
    return numeroPrimo

global numeroPrimo
numeroPrimo = 0
num = 0



for i in range(10):
    # print(numero_passi)
    global colore
    colore = 'blue'
    color(colore)
    pensize(10)
    for i in range(7 - 2):  # numero_lati - 2
        # for i in (numero_passi):
        for i in range(1, numero_passi):
            print(f"{numero}: {trova_numeri_primi(numero)}")
            if trova_numeri_primi(numero):
                colore = 'yellow'
            else:
                colore = 'grey'
            color(colore)
            forward(10)
            numero += 1
        # forward(numero_passi*2)
        left(360 / 7)
        numero_passi += 1


# end_fill()
done()
