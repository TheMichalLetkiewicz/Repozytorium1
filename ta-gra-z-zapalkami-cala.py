import turtle
import tkinter as tk


window = turtle.Screen()

B = 700
X = - 135
Y = 136

ODSTĘP = 136

win = window.setup(700,700)
window.title('Gra z zapałkami nie pamietam nazwy')
window.bgcolor('green yellow')
turtle.speed(10)


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





# Funkcja obsługująca kliknięcie na obrazek
def handle_click(x, y):
    print("Kliknięto na obrazek w punkcie", x, y)




# Ustawienia rozmiaru i położenia obrazka
image_width = 20
image_height = 75
image_x_offset = -100
image_y_offset = 175

# Rysowanie prostokąta jako zastępcowego obrazka
def draw_image(image_x, image_y):
    turtle.penup()
    turtle.goto(image_x, image_y)
    turtle.pendown()
    turtle.begin_fill()
    for _ in range(2):
        turtle.forward(image_width)
        turtle.right(90)
        turtle.forward(image_height)
        turtle.right(90)
    turtle.end_fill()

# Iteracja po tablicy i rysowanie obrazków
for row_index, row in enumerate(tablica):
    for col_index, element in enumerate(row):
        if element == 'I':
            # Obliczanie współrzędnych obrazka
            image_x = image_x_offset + col_index * (image_width + 10)
            image_y = image_y_offset - row_index * (image_height + 10)

            # Rysowanie zastępcowego obrazka
            draw_image(image_x, image_y)

            # Dodanie obsługi kliknięcia na obrazek
            turtle.onscreenclick(handle_click, 1)

# Rysowanie liczby w prawym górnym rogu
def draw_number(number, x, y):
    turtle.penup()
    turtle.goto(x, y)
    turtle.write(number, align="right", font=("Arial", 33, "normal"))

# Umieszczenie liczb 1, 2, 3 w prawym górnym rogu
draw_number(1, 290, 290)
draw_number(2, 290, 250)
draw_number(3, 290, 210)

# Uruchomienie pętli głównej turtle
turtle.mainloop()

