# SPIRALE DI ULAM E ALTRE SPIRALI PER PATTERN IN PRIME NUMBERS!!!
# Ho trovato i suoni su freesound.org
# Ho trovato le immagini su clipart-library.com

#################################
# Author: Paolo Maria Guardiani #
#                               #
#       Deo Gratias!            #
#################################

# TODO: nel titolo automatico devono comparire il numero dei lati, il numero di partenza (magari al fondo in modo che faccia da counter)

# Ho trovato la funzione per trovare numeri primi sul sito:
# http://www.batmath.it/js/primo/primo.htm
# L'ho poi rielaborata per utilizzarla in Python
from tkinter import *
from tkinter import ttk
from tkinter import colorchooser
import turtle
from tkinter import filedialog
from PIL import Image, ImageDraw, ImageGrab, ImageTk
import PIL
from tkinter import messagebox
import pygame
from pygame import mixer

# Importo una libreria che permette di importare una fuzione scritta in C
from ctypes import *

libCalc = CDLL("./trova_numeri_primi.so")

# call C function to check connection
# libCalc.connect()

# chiamo la funzione nel programma scritto in c
# Thanks to: https://www.youtube.com/watch?v=kbRepk-GPs4
# Attenzione la funzione booleana in C non ritorna True o False, ma 0 oppure 1!!!
test_number = libCalc.trova_numeri_primi(4)
print(type(test_number))
print(test_number)

# tracer(0,0) e alla fine update() permettono di disegnare tutto in una volta sola!!!


# Creo la finestra del programma
root = Tk()
root.title("Find Patterns in Prime Numbers")
root.iconbitmap('immagini/logo_di_paolo.ico')
root.geometry("1500x980+25+0")

pygame.mixer.init()
sound_photo = mixer.Sound('suoni/take_a_photo.wav')
sound_click_special = mixer.Sound('suoni/button_special.wav')
sound_click = mixer.Sound('suoni/button_click_soft.wav')
sound_laboratory = mixer.Sound('suoni/laboratorio.wav')

# Preparo le immagini
photo_camera = PhotoImage(file='immagini/photo_camera.png')
one_slide = PhotoImage(file='immagini/one_slide.png')
more_slides = PhotoImage(file='immagini/more_slides.png')

# scrivo le variabili globali
global updated_starting_number
updated_starting_number = 29
global starting_number
starting_number = 29
global iterations_number
iterations_number = 10
global slides_number
slides_number = 3
global numero_passi
numero_passi = 0
global numero_lati
numero_lati = 3
global ripetizioni
ripetizioni = 1

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
canvas_height = 900
global turtle_pen_size
turtle_pen_size = 13
global turtle_forward
turtle_forward = 13

frame_left = Frame(root)
frame_left.grid(row=0, column=0, padx=10, pady=10)

frame_right = Frame(root)
frame_right.grid(row=0, column=1, padx=10, pady=10)

# Creo il canvas
my_canvas = Canvas(frame_left, width=canvas_width, height=canvas_height, bg=canvas_color)
my_canvas.pack(pady=20)

# creo una istanza di turtle che si colleghi a my_canvas
global t

# Thanks to: https://howtofix.io/can-you-turn-off-tracer-for-turtlescreen-embedded-in-tkinter-window-id82013
screen = turtle.TurtleScreen(my_canvas)
global speed_turtle
speed_turtle = 8

screen.tracer(speed_turtle)
t = turtle.RawTurtle(screen)
t.pencolor("blue")
t.speed(0)
t.goto(0, 0)  # per turtle 0, 0 è il centro dello schermo (non è come il canvas normale
t.shape('arrow')
text_turtle = turtle.RawTurtle(my_canvas)
text_turtle.penup()
text_turtle.color(color_prime)
text_turtle.goto(-400, 300)
text_turtle.hideturtle()


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
    sound_click.play()
    color_prime = colorchooser.askcolor()[1]


def change_normal_color():
    global color_normal_number, canvas_color
    sound_click.play()
    color_normal_number = colorchooser.askcolor(color=canvas_color)[1]


def change_pen_color():
    global color_pen, canvas_color
    sound_click.play()
    color_pen = colorchooser.askcolor(color=canvas_color)[1]


def change_pen_up_down():
    global is_pen_up_down
    sound_click.play()
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


def change_pen_up():
    sound_click.play()
    t.penup()
    messagebox.showinfo("Pen Info", "Pen is Up")


def change_pen_down():
    sound_click.play()
    t.pendown()
    messagebox.showinfo("Pen Info", "Pen is Down")


def change_canvas_color():
    global canvas_color
    sound_click.play()
    canvas_color = colorchooser.askcolor(color='white')[1]
    my_canvas.config(bg=canvas_color)


def clear_canvas():
    global numero_passi, starting_number, updated_starting_number, canvas_width, canvas_height
    global ripetizioni  # serve per le funzioni riguardanti l'esagono e l'ottagono
    sound_click.play()
    # # # canvas_width += 100
    # # # canvas_height += 100
    # # my_canvas.config(width=canvas_width , height= canvas_height)
    # t = turtle.RawTurtle(my_canvas)
    # riposiziono la tartaruga al centro del canvas con l'orientamento iniziale
    t.reset()
    t.hideturtle()
    text_turtle.reset()
    text_turtle.hideturtle()
    # my_canvas.delete(ALL)  # ATTENZIONE: non devo cancellare il canvas, ma usare turtle.reset()
    numero_passi = 0
    starting_number = updated_starting_number
    label_processed_number.config(text=f"Number now is: {starting_number}")
    ripetizioni = 1  # serve per le funzioni riguardanti l'esagono e l'ottagono!!! (per reimpostare i passi della tartaruga)


# do_one_step funzione che utilizza la funzione trova_numeri_primi scritta in Python
# def do_one_step():
#     global starting_number
#     if trova_numeri_primi(starting_number):
#         t.dot(turtle_pen_size, color_prime)
#     else:
#         t.dot(turtle_pen_size, color_normal_number)
#     t.forward(turtle_forward)
#     starting_number += 1
#     label_processed_number.config(text=f"Number now is: {starting_number}")


# do_one_step funzione che fa fare i passettini alla tartaruga con funzione in C
def do_one_step():
    global starting_number
    if libCalc.trova_numeri_primi(starting_number) == 1:
        t.dot(turtle_pen_size, color_prime)
    else:
        t.dot(turtle_pen_size, color_normal_number)
    t.forward(turtle_forward)
    starting_number += 1
    label_processed_number.config(text=f"Number now is: {starting_number}")


def start_animation_6(*args):
    global starting_number, numero_passi, iterations_number, numero_lati, color_prime, canvas_color
    global ripetizioni
    global color_pen
    print(numero_lati)
    t.shape('arrow')
    t.showturtle()
    t.pencolor(color_pen)

    for i in range(iterations_number):
        for i in range(numero_lati - 2):
            for i in range(ripetizioni):
                do_one_step()
            t.left(360 / numero_lati)

        for i in range(ripetizioni + 1):
            do_one_step()
        t.left(360 / numero_lati)

        for i in range(ripetizioni):
            do_one_step()
        t.left(360 / numero_lati)
        ripetizioni += 1
    t.hideturtle()


def start_animation_triangle_square(*args):
    global starting_number, numero_passi, iterations_number, numero_lati, color_prime, canvas_color
    global color_pen
    print(numero_lati)
    t.shape('arrow')
    t.showturtle()
    t.pencolor(color_pen)
    for i in range(iterations_number):
        for i in range(numero_lati - 2):  # numero_lati - 2
            for i in range(1, numero_passi):
                do_one_step()
                # if trova_numeri_primi(starting_number):
                #     t.dot(turtle_pen_size, color_prime)
                # else:
                #     t.dot(turtle_pen_size, color_normal_number)
                # t.forward(turtle_forward)
                # starting_number += 1
            t.left(360 / numero_lati)
        numero_passi += 1
    t.hideturtle()


def start_animation_8(*args):  # forse non è proprio precisa questa funzione dal punto di vista grafico...
    global starting_number, numero_passi, iterations_number, numero_lati, color_prime, canvas_color
    global ripetizioni
    global color_pen
    print(numero_lati)
    t.shape('arrow')
    t.showturtle()
    t.pencolor(color_pen)

    for i in range(5):
        for i in range(numero_lati - 2):
            for j in range(ripetizioni):
                do_one_step()
            t.left(360 / numero_lati)

        for i in range(ripetizioni + 1):
            do_one_step()
        t.left(360 / numero_lati)

        for i in range(ripetizioni):
            do_one_step()
        t.left(360 / numero_lati)

        for i in range(ripetizioni):
            do_one_step()
        t.left(360 / numero_lati)

        for i in range(ripetizioni + 1):
            do_one_step()
        t.left(360 / numero_lati)

        for i in range(ripetizioni + 1):
            do_one_step()
        t.left(360 / numero_lati)

        for i in range(ripetizioni):
            do_one_step()
        t.left(360 / numero_lati)
        ripetizioni += 1
    # secondo ciclo
    #     for i in range(numero_lati - 2):
    #         for j in range(ripetizioni):
    #             do_one_step()
    #         t.left(360 / numero_lati)

    # do_one_step()
    # do_one_step()
    # t.left(360 / numero_lati)
    #
    # do_one_step()
    # t.left(360 / numero_lati)
    #
    # do_one_step()
    # t.left(360 / numero_lati)
    #
    # do_one_step()
    # do_one_step()
    # t.left(360 / numero_lati)
    #
    # do_one_step()
    # do_one_step()
    # t.left(360 / numero_lati)
    #
    # do_one_step()
    # t.left(360 / numero_lati)
    # do_one_step()
    # do_one_step()
    # t.left(360 / numero_lati)
    #
    # do_one_step()
    # do_one_step()
    # t.left(360 / numero_lati)
    #
    # do_one_step()
    # do_one_step()
    # t.left(360 / numero_lati)
    #
    # do_one_step()
    # do_one_step()
    # t.left(360 / numero_lati)
    #
    # do_one_step()
    # do_one_step()
    # t.left(360 / numero_lati)
    #
    # do_one_step()
    # do_one_step()
    # t.left(360 / numero_lati)

    # ripetizioni += 1
    # for i in range(numero_lati - 2):
    #     for j in range(ripetizioni):
    #         do_one_step()
    #     t.left(360 / numero_lati)

    t.hideturtle()


def start_animation(*args):
    global numero_lati
    sound_laboratory.play()
    # if numero_lati == 3:
    # t.setheading(120)
    if numero_lati == 3 or numero_lati == 4:
        start_animation_triangle_square()
    elif numero_lati == 6:
        start_animation_6()
    elif numero_lati == 8:
        start_animation_8()
    elif numero_lati == 30:
        scrivi_autore()
    else:
        start_animation_triangle_square()


def change_pen_size(event):
    global turtle_pen_size, turtle_forward
    turtle_pen_size = int(pen_slider.get())
    turtle_forward = int(pen_slider.get())
    slider_label.config(text=f"Size Pen: {int(pen_slider.get())}")


def change_num_size(event):
    global numero_lati
    numero_lati = int(num_side_slider.get())
    slider_label2.config(text=f"Sides: {int(num_side_slider.get())}")


# Cambio la velocità dell'animazione
def change_speed_turtle(event):
    global speed_turtle
    speed_turtle = int(speed_turtle_slider.get())
    screen.tracer(speed_turtle)
    speed_turtle_label.config(text=f"Speed: {int(speed_turtle_slider.get())}")
    if speed_turtle == 0:
        speed_turtle_label.config(
            text=f"No Animation")
        speed_turtle_label2.config(text="Please Wait!")
    else:
        speed_turtle_label2.config(text="")


def change_starting_number(*args):
    global starting_number, updated_starting_number
    sound_click_special.play()
    clear_canvas()
    starting_number = int(entry_numero.get())
    updated_starting_number = int(entry_numero.get())
    label_entry_numero.config(text=f"Starting Number is: {starting_number}")


def change_number_iterations(*args):
    global iterations_number
    sound_click_special.play()
    iterations_number = int(entry_iterations.get())
    label_entry_iterations.config(text=f"Iterations Number: {iterations_number}")


def scrivi_autore():
    text_turtle.goto(-400, 300)
    sound_laboratory.play()
    text_turtle.showturtle()
    text_turtle.write("Autore: Paolo Maria Guardiani", font=('Courier', 30, 'italic'), align='left', move=True)


def save_as_png():  # thanks to the John Elder's course on Udemy!!!
    sound_photo.play()
    result = filedialog.asksaveasfilename(initialdir='home/paolomaria',
                                          filetypes=(("png files", "*.png"), ("all files", "*.*")))

    if result.endswith('.png'):
        pass
    else:
        result = result + '.png'

    if result:
        x = root.winfo_rootx() + my_canvas.winfo_x()
        y = root.winfo_rooty() + my_canvas.winfo_y()
        x1 = x + my_canvas.winfo_width()
        y1 = y + my_canvas.winfo_height()
        ImageGrab.grab().crop((x, y, x1, y1)).save(result)

        # messagebox.showinfo("Image Saved", "You Image Has Been Saved!")
        messagebox.showinfo("Image Saved", "L'immagine è stata salvata con successo!")


global numero_diapositiva, is_possible_to_save
numero_diapositiva = 0
is_possible_to_save = False

# Salva una diapositiva in modo automatico (scrive il nome del file e aumenta di uno lo starting_number)
def save_automatic_photo():
    global starting_number, updated_starting_number, speed_turtle, color_pen, numero_diapositiva, numero_passi, is_possible_to_save, numero_lati, color_prime, canvas_color

    is_possible_to_save
    numero_iniziale = starting_number

    # cancello tutto dallo schermo
    clear_canvas()

    numero_diapositiva += 1

    # # setto la velocità al massimo senza animazioni
    # speed_turtle = 0;
    # # cambio il numero nell'etichetta della slider bar
    # speed_turtle_label.config(text="No Aminations")
    # speed_turtle_label2.config(text="Please Wait!")

    # faccio partire l'animazione
    print(numero_lati)
    t.shape('arrow')
    t.showturtle()
    t.pencolor(color_pen)
    for i in range(iterations_number):
        for i in range(numero_lati - 2):  # numero_lati - 2
            for i in range(1, numero_passi):
                if libCalc.trova_numeri_primi(numero_iniziale) == 1:
                    t.dot(turtle_pen_size, color_prime)
                else:
                    t.dot(turtle_pen_size, color_normal_number)
                t.forward(turtle_forward)
                numero_iniziale += 1
                label_processed_number.config(text=f"Number now is: {numero_iniziale}")
            t.left(360 / numero_lati)
        numero_passi += 1
    t.hideturtle()
    is_possible_to_save = True

    result = f"slides/automatic_photo_sides_{numero_lati}_starting_number_{starting_number}.png";

    if is_possible_to_save:
        if result:
            x = root.winfo_rootx() + my_canvas.winfo_x()
            y = root.winfo_rooty() + my_canvas.winfo_y()
            x1 = x + my_canvas.winfo_width()
            y1 = y + my_canvas.winfo_height()
            ImageGrab.grab().crop((x, y, x1, y1)).save(result)

    sound_photo.play();
    # aumento di una unità il numero di partenza
    starting_number = starting_number + 1
    updated_starting_number = starting_number
    label_entry_numero.config(text=f"Starting Number is: {starting_number}")
    entry_numero.delete(0, END)
    entry_numero.insert(0, starting_number)


def change_number_slides(*args):
    global slides_number
    sound_click_special.play()
    slides_number = int(entry_slides.get())
    label_entry_slides.config(text=f"Number of slides: {slides_number}")
    print(slides_number)


# genera una serie di diapositive in base al numero di diapositive selezionato
def save_automatic_slides():
    global slides_number
    for i in range(slides_number):
        save_automatic_photo()


# Button to change the color of prime numbers
change_color_prime_numbers = Button(frame_right, text="Prime Color", command=change_prime_color, width=10)
change_color_prime_numbers.grid(row=0, column=0, padx=10, pady=10, sticky=W)
# Button to change the color of normal numbers
change_color_normal_numbers = Button(frame_right, text="Normal Color", command=change_normal_color, width=10)
change_color_normal_numbers.grid(row=0, column=1, padx=10, pady=10, sticky=W)
# Button To Change The Canvas Color
change_canvas_color_button = Button(frame_right, text="Canvas Color", command=change_canvas_color, width=10)
change_canvas_color_button.grid(row=0, column=2, padx=10, pady=10, sticky=W)

# Button to Change pen color
change_pen_color = Button(frame_right, text="Pen Color", command=change_pen_color, width=10)
change_pen_color.grid(row=1, column=0, padx=10, pady=10, sticky=W)
# Button to Set Pen Up
change_pen_up_down = Button(frame_right, text="Pen Up", command=change_pen_up, width=10)
change_pen_up_down.grid(row=1, column=1, padx=10, pady=10, sticky=W)
# Button to Set Pen Down
change_pen_up_down = Button(frame_right, text="Pen Down", command=change_pen_down, width=10)
change_pen_up_down.grid(row=1, column=2, padx=10, pady=10, sticky=W)

# Button to Clear the Canvas
clear_canvas_button = Button(frame_right, text="Clear Canvas", command=clear_canvas, width=10)
clear_canvas_button.grid(row=2, column=0, padx=10, pady=10, sticky=W)
# Button to start animation
start_animation_button = Button(frame_right, text="Start Anim.", command=start_animation, bg="#434448", fg="yellow",
                                width=10)
start_animation_button.bind('<s>', start_animation)
start_animation_button.grid(row=2, column=1, padx=10, pady=10, sticky=W)

# Slider for pensize
pen_slider = ttk.Scale(frame_right, from_=1, to=30, command=change_pen_size, orient=HORIZONTAL, value=13)
pen_slider.grid(row=3, column=0, padx=10, pady=10)
slider_label = Label(frame_right, text=f"Size Pen: {pen_slider.get()}", font=("Helvetica", 12))
slider_label.grid(row=3, column=1, padx=10, pady=10, sticky=W)

# Slider per il numero lati del poligono
num_side_slider = ttk.Scale(frame_right, from_=3, to=30, command=change_num_size, orient=HORIZONTAL, value=3)
num_side_slider.grid(row=4, column=0, padx=10, pady=10)
slider_label2 = Label(frame_right, text=f"Sides: {num_side_slider.get()}", font=("Helvetica", 12))
slider_label2.grid(row=4, column=1, padx=10, pady=10, sticky=W)

# Slider per la velocità dell'animazione
speed_turtle_slider = ttk.Scale(frame_right, from_=0, to=30, command=change_speed_turtle, orient=HORIZONTAL, value=8)
speed_turtle_slider.grid(row=5, column=0, padx=10, pady=10, sticky=W)
speed_turtle_label = Label(frame_right, text=f"Speed: {speed_turtle_slider.get()}", font=('Helvetica', 12))
speed_turtle_label.grid(row=5, column=1, padx=10, pady=10, sticky=W)
speed_turtle_label2 = Label(frame_right, text=f"", font=('Helvetica', 12))
speed_turtle_label2.grid(row=5, column=2, padx=10, pady=10, sticky=W)

# Entry per il numero di partenza
entry_numero = Entry(frame_right, font=("Helvetica", 14), width=10)
entry_numero.insert(0, starting_number)
entry_numero.bind('<Return>', change_starting_number)
entry_numero.grid(row=6, column=0, padx=10, pady=10, sticky=W)
# Bottone per inserire il numero di partenza
button_entry_numero = Button(frame_right, text="Insert", command=change_starting_number, width=10)
button_entry_numero.grid(row=6, column=1, padx=10, pady=10, sticky=W)
# Label per il numero di lati
label_entry_numero = Label(frame_right, text=f"Starting number is: {starting_number}", font=("Helvetica", 14))
label_entry_numero.grid(row=6, column=2, padx=10, pady=10, sticky=W)

# Entry per il numero di iterazioni
entry_iterations = Entry(frame_right, font=("Helvetica", 14), width=10)
entry_iterations.insert(0, iterations_number)
entry_iterations.bind('<Return>', change_number_iterations)
entry_iterations.grid(row=7, column=0, padx=10, pady=10, sticky=W)
# Bottone per inserire il numero di iterazioni
button_entry_iterations = Button(frame_right, text="Insert", command=change_number_iterations, width=10)
button_entry_iterations.grid(row=7, column=1, padx=10, pady=10, sticky=W)
# Label per il numero di iterazioni
label_entry_iterations = Label(frame_right, text=f"Iterations Number: {iterations_number}", font=("Helvetica", 14))
label_entry_iterations.grid(row=7, column=2, padx=10, pady=10, sticky=W)

# Entry per il numero di slides da generare
entry_slides = Entry(frame_right, font=("Helvetica", 14), width=10)
entry_slides.insert(0, 3)
entry_slides.bind('<Return>', change_number_slides)
entry_slides.grid(row=8, column=0, padx=10, pady=10, sticky=W)
# Bottone per configurare il numero di slides
button_entry_slides = Button(frame_right, text="Insert", command=change_number_slides, width=10)
button_entry_slides.grid(row=8, column=1, padx=10, pady=10, sticky=W)
# Label per il numero di slides
label_entry_slides = Label(frame_right, text=f"Number of slides: {slides_number}", font=("Helvetica", 14))
label_entry_slides.grid(row=8, column=2, padx=10, pady=10, sticky=W)

# update() insieme a tracer(0,0) vedi le prime righe permette di visualizzare l'immagine in una sola volta senza animazioni
# importante: devo eliminare done() alla fine, altrimenti apre un'altra finestra di turtle
# done()

# Label per l'aggiornamento del numero
label_processed_number = Label(frame_right, text=f"Number now is: {starting_number}", font=("Helvetica", 14))
label_processed_number.grid(row=9, column=0, columnspan=3, padx=10, pady=10, sticky=W)

# pulsante per salvare l'immagine scrivendo il nome del file
save_as_png_btn = Button(frame_right, image=photo_camera, command=save_as_png, borderwidth=0)
save_as_png_btn.grid(row=10, column=0, padx=10, pady=10, sticky=W)

# Pulsante per salvare automaticamente una diapositiva
save_automatic_photo_btn = Button(frame_right, image=one_slide, command=save_automatic_photo, borderwidth=0)
save_automatic_photo_btn.grid(row=10, column=1, padx=10, pady=10, sticky=W)

save_automatic_slides_btn = Button(frame_right, image=more_slides, command=save_automatic_slides, borderwidth=0)
save_automatic_slides_btn.grid(row=10, column=2, padx=10, pady=10, sticky=W)


screen.update()
root.mainloop()
