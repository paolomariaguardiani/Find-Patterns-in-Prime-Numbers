# SPIRALE DI ULAM E ALTRE SPIRALI PER PATTERN IN PRIME NUMBERS!!!

#################################
# Author: Paolo Maria Guardiani #
#                               #
# Deo Gratias!                  #
#################################

# todo: pulsante per riposizionare al centro del canvas la tartaruga
# todo: entry per inserire il numero di lati del poligono
# todo: entry per inserire il numero di partenza
# todo: eliminare la seconda finestra di turtle


# Ho trovato la funzione per trovare numeri primi sul sito:
# http://www.batmath.it/js/primo/primo.htm
# L'ho poi rielaborata per utilizzarla in Python
from tkinter import *
from tkinter import colorchooser
import turtle
from turtle import *

# tracer(0,0) e alla fine update() permettono di disegnare tutto in una volta sola!!!
# tracer(0,0)


# Creo la finestra del programma
root = Tk()
root.title("Find Patterns in Prime Numbers")
root.geometry("800x800")

# numero è il numero di partenza
global numero
numero = 29
global numero_passi
numero_passi = 0
global numero_lati
numero_lati = 3
global bg_color
bg_color = 'white'
global colore
colore = 'green'

# Creo il canvas
w = 600
h = 400
my_canvas = Canvas(root, width=w, height=h, bg=bg_color)
my_canvas.pack(pady=20)

# creo una istanza di turtle che si colleghi a my_canvas
t = turtle.RawTurtle(my_canvas)
t.pencolor("blue")


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


def change_color():
    global colore
    # colore = 'orange'
    # color=colore imposta il colore di partenza a quello impostato
    # colore = colorchooser.askcolor(color=colore)[1]
    colore = colorchooser.askcolor()[1]


def clear_canvas():
    my_canvas.delete(ALL)


def start_animation():
    global numero, numero_passi, numero_lati, colore, bg_color
    for i in range(20):
        # print(numero_passi)
        t.pensize(3)
        for i in range(numero_lati - 2):  # numero_lati - 2
            for i in range(1, numero_passi):
                print(f"{numero}: {trova_numeri_primi(numero)}")
                if trova_numeri_primi(numero):
                    t.pencolor(colore)
                else:
                    t.pencolor(bg_color)
                # t.pencolor(colore)
                t.forward(3)
                numero += 1
            t.left(360 / numero_lati)
        numero_passi += 1


def change_canvas_color():
    global bg_color
    bg_color = colorchooser.askcolor(color='white')[1]
    my_canvas.config(bg=bg_color)


# We create the commands
frame_comandi = Frame(root)
frame_comandi.pack()
# Button to change the color of the turtle
change_color_button = Button(frame_comandi, text="Change Color", command=change_color)
change_color_button.grid(row=0, column=0, padx=10, pady=10)

# Button to start animation
start_animation_button = Button(frame_comandi, text="Start Animation", command=start_animation)
start_animation_button.grid(row=0, column=1, padx=10, pady=10)

# Button to Clear the Canvas
clear_canvas_button = Button(frame_comandi, text="Clear Canvas", command=clear_canvas)
clear_canvas_button.grid(row=0, column=2, padx=10, pady=10)

# Button To Change The Canvas Color
change_canvas_color_button = Button(frame_comandi, text="Change Canvas Color", command=change_canvas_color)
change_canvas_color_button.grid(row=1, column=0, padx=50, pady=50)

# update() insieme a tracer(0,0) vedi le prime righe permette di visualizzare l'immagine in una sola volta senza animazioni
# importante: devo eliminare done() alla fine, altrimenti apre un'altra finestra di turtle

# done()

root.mainloop()

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
