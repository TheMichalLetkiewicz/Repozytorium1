import turtle
import random
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


            


