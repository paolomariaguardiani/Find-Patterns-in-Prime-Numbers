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
from tkinter import ttk
from tkinter import colorchooser
import turtle
from turtle import *

# tracer(0,0) e alla fine update() permettono di disegnare tutto in una volta sola!!!
# tracer(0,0)


# Creo la finestra del programma
root = Tk()
root.title("Find Patterns in Prime Numbers")
root.geometry("800x800")

# scrivo le variabili globali
global updated_starting_number
updated_starting_number = 29
global starting_number
starting_number = 29

global numero_passi
numero_passi = 0
global numero_lati
numero_lati = 3
global bg_color
bg_color = 'white'
global colore
colore = 'green'
global canvas_width
canvas_width = 600
global canvas_height
canvas_height = 400
global turtle_pen_size
turtle_pen_size = 3
global turtle_forward
turtle_forward = 3

# Creo il canvas
my_canvas = Canvas(root, width=canvas_width, height=canvas_height, bg=bg_color)
my_canvas.pack(pady=20)

# creo una istanza di turtle che si colleghi a my_canvas
global t
t = turtle.RawTurtle(my_canvas)
t.pencolor("blue")
t.speed(0)
t.goto(0, 0)  # per turtle 0, 0 è il centro dello schermo (non è come il canvas normale
t.shape('triangle')


def trova_numeri_primi(numero):
    numero_primo = False
    if numero == 0:
        numero_primo = False
    elif numero == 1:
        numero_primo = True
    if numero == 2:
        numero_primo = True
    for i in range(2, numero):
        if numero % i == 0:
            numero_primo = False
            break
        if numero % i != 0:
            numero_primo = True
    return numero_primo


def change_color():
    global colore
    # colore = 'orange'
    # color=colore imposta il colore di partenza a quello impostato
    # colore = colorchooser.askcolor(color=colore)[1]
    colore = colorchooser.askcolor()[1]


def clear_canvas():
    global t, canvas_width, canvas_height, numero_passi, starting_number, updated_starting_number
    my_canvas.delete(ALL)
    # riposiziono la tartaruga al centro del canvas
    t.goto(0, 0)
    t.home()
    # t.mode('standard')  # 'standard' = to the right (east); 'logo = upward (north)
    # t.right(90)
    # t.reset()
    # t.setheading(0)
    numero_passi = 0
    starting_number = updated_starting_number
    t.shape('triangle')
    print(t.heading())
    print(numero_passi)
    print(starting_number)
    print(updated_starting_number)


def start_animation():
    global starting_number, numero_passi, numero_lati, colore, bg_color
    for i in range(20):
        # print(numero_passi)
        t.pensize(turtle_pen_size)
        t.penup()
        for i in range(numero_lati - 2):  # numero_lati - 2
            for i in range(1, numero_passi):
                # print(f"{starting_number}: {trova_numeri_primi(starting_number)}")
                if trova_numeri_primi(starting_number):
                    t.pencolor(colore)
                    t.dot(turtle_pen_size, colore)
                else:
                    t.pencolor(bg_color)
                # t.pencolor(colore)
                t.forward(turtle_forward)
                starting_number += 1
            t.left(360 / numero_lati)
        numero_passi += 1


def change_canvas_color():
    global bg_color
    bg_color = colorchooser.askcolor(color='white')[1]
    my_canvas.config(bg=bg_color)


def change_pen_size(event):
    global turtle_pen_size, turtle_forward
    turtle_pen_size = int(pen_slider.get())
    turtle_forward = int(pen_slider.get())
    slider_label.config(text=int(pen_slider.get()))


def change_num_size(event):
    global numero_lati
    numero_lati = int(num_side_slider.get())
    slider_label2.config(text=int(num_side_slider.get()))


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
change_canvas_color_button.grid(row=1, column=0, padx=10, pady=10)

# Slider for pensize
pen_slider = ttk.Scale(frame_comandi, from_=1, to=30, command=change_pen_size, orient=HORIZONTAL, value=3)
pen_slider.grid(row=1, column=1, padx=10, pady=10)
slider_label = Label(frame_comandi, text=pen_slider.get(), font=("Helvetica", 12))
slider_label.grid(row=1, column=2, padx=10, pady=10)

# Slider per il numero lati del poligono
num_side_slider = ttk.Scale(frame_comandi, from_=1, to=30, command=change_num_size, orient=HORIZONTAL, value=3)
num_side_slider.grid(row=2, column=1, padx=10, pady=10)
slider_label2 = Label(frame_comandi, text=num_side_slider.get(), font=("Helvetica", 12))
slider_label2.grid(row=2, column=2, padx=10, pady=10)

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
