# Questa funzione l'ho trovata sul sito:
# http://www.batmath.it/js/primo/primo.htm

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

for i in range(2, 100):
    print(num, end=" ")
    print(trova_numeri_primi(num))
    num += 1

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