import turtle
import random
import tkinter as tk
window = turtle.Screen()

B = 700
X = - 135
Y = 136

ODSTĘP = 136

window.setup(700,700)
window.title('Gra z zapałkami nie pamietam nazwy')
window.bgcolor('green yellow')
zolw = turtle.Turtle()
turtle.speed(100)


tablica = [
    [None, None, None, None, None, None, None],
    [None, None, None, 'I', None, None, None],
     [None, None, 'I', 'I', 'I', None, None],
      [None, 'I', 'I', 'I', 'I', 'I', None],
       ['I', 'I', 'I', 'I', 'I', 'I', 'I'],
    [None, None, None, None, None, None, None],
    [None, None, None, None, None, None, None]
]




row1 = tablica[0]
row2 = tablica[1]
row3 = tablica[2]
row4 = tablica[3]
row5 = tablica[4]
row6 = tablica[5]
row7 = tablica[6]

for i in range(0,6):
    for j in range(0,6):
        if tablica[i][j] != None:
            print(i,j)
            zolw.penup
            zolw.goto(35+i*70,35+j*70)
            zolw.pendown
            zolw.pencolor("Black")
            zolw.width(2)
            


