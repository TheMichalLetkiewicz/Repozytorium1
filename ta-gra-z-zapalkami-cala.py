import turtle
import random
window = turtle.Screen()

B = 700

X = - 135

Y = 136

ODSTĘP = 136

window.setup(B,B)
window.title('Gra z zapałkami nie pamietam nazwy')
window.bgcolor('green yellow')
zolw = turtle.Turtle()



tablica = [
    [None, None, None, None, None, None, None],
    [None, None, None, 'I', None, None, None],
    [None, None, 'I', 'I', 'I', None, None],
    [None, 'I', 'I', 'I', 'I', 'I', None],
    ['I', 'I', 'I', 'I', 'I', 'I', 'I'],
    [None, None, None, None, None, None, None],
    [None, None, None, None, None, None, None]
]












zolw.width(1)
zolw.speed(111000)
square_size = window.window_width() / 7
for i in range(0,7):
    for j in range(0,7):
        
        zolw.penup()
        zolw.goto(-window.window_width() / 2 + j * square_size,
               window.window_height() / 2 - (i + 1) * square_size)
        zolw.pendown()

        
        for k in range(4):
            zolw.forward(square_size)
            zolw.right(90)


turtle.done()




