# SPIRALE DI ULAM E ALTRE SPIRALI PER PATTERN IN PRIME NUMBERS!!!

#################################
# Author: Paolo Maria Guardiani #
#                               #
# Deo Gratias!                  #
#################################

# todo: pulsante per riposizionare al centro del canvas la tartaruga
# fatto: slider per selezionare il numero di lati del poligono
# todo: aggiungere labels per gli sliders
# todo: entry per inserire il numero di partenza
# todo: inserire bottone per salvare in formato png
# todo: aggiungere la possibilit√† di colorare in modo diverso i twin prime numbers
# fatto: eliminare la seconda finestra di turtle


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
root.geometry("1980x1080")

# scrivo le variabili globali
global updated_starting_number
updated_starting_number = 29
global starting_number
starting_number = 29
global iterations_number
iterations_number = 10
global numero_passi
numero_passi = 0
global numero_lati
numero_lati = 3

global canvas_color
canvas_color = 'white'
global color_prime
color_prime = 'green'
global color_pen
color_pen = 'grey'
global color_normal_number
color_normal_number = "yellow"
global is_pen_up_down
is_pen_up_down = True

global canvas_width
canvas_width = 900
global canvas_height
canvas_height = 700
global turtle_pen_size
turtle_pen_size = 7
global turtle_forward
turtle_forward = 7

# Creo il canvas
my_canvas = Canvas(root, width=canvas_width, height=canvas_height, bg=canvas_color)
my_canvas.pack(pady=20)

# creo una istanza di turtle che si colleghi a my_canvas
global t
t = turtle.RawTurtle(my_canvas)
t.pencolor("blue")
t.speed(0)
t.goto(0, 0)  # per turtle 0, 0 √® il centro dello schermo (non √® come il canvas normale
t.shape('arrow')


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


def change_prime_color():
    global color_prime
    color_prime = colorchooser.askcolor()[1]

def change_normal_color():
    global color_normal_number, canvas_color
    color_normal_number = colorchooser.askcolor(color=canvas_color)[1]


def change_pen_color():
    global color_pen, canvas_color
    color_pen = colorchooser.askcolor(color=canvas_color)[1]

def change_pen_up_down():
    global is_pen_up_down
    if is_pen_up_down:
        t.penup()
        is_pen_up_down = False
        change_pen_up_down.config(text="Pen is Up")
    else:
        t.pendown()
        change_pen_up_down.config(text="Pen is Down")
        print("Now pen is down")
        print(is_pen_up_down)
        is_pen_up_down = True



def change_canvas_color():
    global canvas_color
    canvas_color = colorchooser.askcolor(color='white')[1]
    my_canvas.config(bg=canvas_color)


def clear_canvas():
    global numero_passi, starting_number, updated_starting_number, canvas_width, canvas_height
    # # # canvas_width += 100
    # # # canvas_height += 100
    # # my_canvas.config(width=canvas_width , height= canvas_height)
    # t = turtle.RawTurtle(my_canvas)
    # riposiziono la tartaruga al centro del canvas con l'orientamento iniziale
    t.reset()
    # my_canvas.delete(ALL)  # ATTENZIONE: non devo cancellare il canvas, ma usare turtle.reset()
    numero_passi = 0
    starting_number = updated_starting_number


def start_animation(*args):
    global starting_number, numero_passi, iterations_number, numero_lati, color_prime, canvas_color
    global color_pen
    t.shape('arrow')
    t.showturtle()
    for i in range(iterations_number):
        t.home
        t.pensize(1)
        t.pencolor(color_pen)
        for i in range(numero_lati - 2):  # numero_lati - 2
            for i in range(1, numero_passi):
                if trova_numeri_primi(starting_number):
                    t.dot(turtle_pen_size, color_prime)
                else:
                    t.dot(turtle_pen_size, color_normal_number)
                t.forward(turtle_forward)
                starting_number += 1
            t.left(360 / numero_lati)
        numero_passi += 1
    t.hideturtle()


def change_pen_size(event):
    global turtle_pen_size, turtle_forward
    turtle_pen_size = int(pen_slider.get())
    turtle_forward = int(pen_slider.get())
    slider_label.config(text=f"Grandezza dei punti: {int(pen_slider.get())}")


def change_num_size(event):
    global numero_lati
    numero_lati = int(num_side_slider.get())
    slider_label2.config(text=f"Numero lati: {int(num_side_slider.get())}")


def change_starting_number(*args):
    global starting_number, updated_starting_number
    clear_canvas()
    starting_number = int(entry_numero.get())
    updated_starting_number = int(entry_numero.get())
    label_entry_numero.config(text=f"Starting Number is: {starting_number}")


def change_number_iterations(*args):
    global iterations_number
    iterations_number = int(entry_iterations.get())
    label_entry_iterations.config(text=f"Iterations Number: {iterations_number}")


# We create the commands
frame_comandi = Frame(root)
frame_comandi.pack()

# Button to change the color of prime numbers
change_color_prime_numbers = Button(frame_comandi, text="Prime Color", command=change_prime_color, width=10)
change_color_prime_numbers.grid(row=0, column=0, padx=10, pady=10, sticky=W)
# Button to change the color of normal numbers
change_color_normal_numbers = Button(frame_comandi, text="Normal Color", command=change_normal_color, width=10)
change_color_normal_numbers.grid(row=0, column=1, padx=10, pady=10, sticky=W)
# Button to Change pen color
change_pen_color = Button(frame_comandi, text="Pen Color", command=change_pen_color, width=10)
change_pen_color.grid(row=0, column=2, padx=10, pady=10, sticky=W)
# Button to Set Pen Up and Pen Down
change_pen_up_down = Button(frame_comandi, text="Pen is Down", command=change_pen_up_down, width=10)
change_pen_up_down.grid(row=0, column=3, padx=10, pady=10, sticky=W)

# Button To Change The Canvas Color
change_canvas_color_button = Button(frame_comandi, text="Canvas Color", command=change_canvas_color, width=10)
change_canvas_color_button.grid(row=0, column=4, padx=10, pady=10, sticky=W)
# Button to Clear the Canvas
clear_canvas_button = Button(frame_comandi, text="Clear Canvas", command=clear_canvas, width=10)
clear_canvas_button.grid(row=0, column=5, padx=10, pady=10, sticky=W)

# Button to start animation
start_animation_button = Button(frame_comandi, text="Start Animation", command=start_animation, width=10)
start_animation_button.bind('<s>', start_animation)
start_animation_button.grid(row=0, column=6, padx=10, pady=10, sticky=W)



# Slider for pensize
pen_slider = ttk.Scale(frame_comandi, from_=1, to=30, command=change_pen_size, orient=HORIZONTAL, value=7)
pen_slider.grid(row=1, column=1, padx=10, pady=10)
slider_label = Label(frame_comandi, text=f"Grandezza dei punti: {pen_slider.get()}", font=("Helvetica", 12))
slider_label.grid(row=1, column=2, padx=10, pady=10)

# Slider per il numero lati del poligono
num_side_slider = ttk.Scale(frame_comandi, from_=1, to=30, command=change_num_size, orient=HORIZONTAL, value=3)
num_side_slider.grid(row=2, column=1, padx=10, pady=10)
slider_label2 = Label(frame_comandi, text=f"Numero lati: {num_side_slider.get()}", font=("Helvetica", 12))
slider_label2.grid(row=2, column=2, padx=10, pady=10)

# Entry per il numero di partenza
entry_numero = Entry(frame_comandi, font=("Helvetica", 14), width=10)
entry_numero.bind('<Return>', change_starting_number)
entry_numero.grid(row=3, column=0, padx=10, pady=10)
# Bottone per inserire il numero di partenza
button_entry_numero = Button(frame_comandi, text="Insert", command=change_starting_number)
button_entry_numero.grid(row=3, column=1)
# Label per il numero di lati
label_entry_numero = Label(frame_comandi, text=f"Starting number is: {starting_number}", font=("Helvetica", 14))
label_entry_numero.grid(row=3, column=2)

# Entry per il numero di iterazioni
entry_iterations = Entry(frame_comandi, font=("Helvetica", 14), width=10)
entry_iterations.bind('<Return>', change_number_iterations)
entry_iterations.grid(row=4, column=0, padx=10, pady=10)
# Bottone per inserire il numero di iterazioni
button_entry_iterations = Button(frame_comandi, text="Insert", command=change_number_iterations)
button_entry_iterations.grid(row=4, column=1)
# Label per il numero di iterazioni
label_entry_iterations = Label(frame_comandi, text=f"Iterations Number: {iterations_number}", font=("Helvetica", 14))
label_entry_iterations.grid(row=4, column=2)

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
