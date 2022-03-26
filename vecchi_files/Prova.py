# PROVA

# Esempio tratto dal sito: https://docs.python.org/3/library/turtle.html?highlight=turtle#module-turtle

from turtle import *
color('red', 'yellow')
begin_fill()
while True:
    forward(200)
    left(170)
    if abs(pos()) < 1:
        break
end_fill
done()