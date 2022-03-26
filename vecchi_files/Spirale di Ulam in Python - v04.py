# SPIRALE DI ULAM E ALTRE SPIRALI PER PATTERN IN PRIME NUMBERS!!!

#################################
# Author: Paolo Maria Guardiani #
#                               #
# Deo Gratias!                  #
#################################

# Ho trovato la funzione per trovare numeri primi sul sito:
# http://www.batmath.it/js/primo/primo.htm
# L'ho poi rielaborata per utilizzarla in Python

from turtle import *
# tracer(0,0) e alla fine update() permettono di disegnare tutto in una volta sola!!!
tracer(0,0)
speed(0)
# numero è il numero di partenza
global numero
numero = 29
global numero_passi
numero_passi = 0
global numero_lati
numero_lati = 3
bgcolor('white')


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


# global numeroPrimo
# numeroPrimo = 0

for i in range(200):
    # print(numero_passi)
    global colore
    colore = 'blue'
    color(colore)
    pensize(1)
    for i in range(numero_lati - 2):  # numero_lati - 2
        for i in range(1, numero_passi):
            print(f"{numero}: {trova_numeri_primi(numero)}")
            if trova_numeri_primi(numero):
                colore = 'black'
            else:
                colore = 'white'
            color(colore)
            forward(1)
            numero += 1
        left(360 / numero_lati)
    numero_passi += 1

# end_fill()
# tracer(0,0) e alla fine update() permettono di disegnare tutto in una volta sola!!!

update()
done()

"""
Funzione del programma in javascript

function trovaNumeriPrimi(numero) {
    if (numero == 0) {
        numeroPrimo = false;
    } else if (numero == 1) {
        numeroPrimo = true;
    }
    if (numero == 2) {
        numeroPrimo = true;
    }
    for (var i=2;i < numero;i++) {
        if (numero % i == 0) {
            numeroPrimo = false;
            break;
        }
        if (numero % i != 0) {
            numeroPrimo = true;
        }
    }
}

"""
