import turtle
import random

window = turtle.Screen()
win = window.setup(700,700)
window.title('Gra')
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





            






#def ruch_gracza(x, y):
    
    #global pierwsza_funkcja_wykonana
    
    









def klikniecie(x,y):
    
    global pierwsza_funkcja_wykonana
    global druga_funkcja
    druga_funkcja = False
    if druga_funkcja == False:
        pierwsza_funkcja_wykonana = False
        print("Kliknięto na obrazek w punkcie", x, y)
        if -56.0 < x < -32.0 and 255.0 < y < 290.0:
            pierwsza_funkcja_wykonana = True
            #Ile(0, 1)
            druga_funkcja = True
        elif -16.0 < x < 16.0 and 255.0 < y < 290.0:
            pierwsza_funkcja_wykonana = True
            #Ile(0, 2)
            druga_funkcja = True
        elif 32.0 < x < 56.0 and 255.0 < y < 290.0:
            pierwsza_funkcja_wykonana = True
            #Ile(0, 3)
            druga_funkcja = True
    
    
    

    if pierwsza_funkcja_wykonana == True and druga_funkcja == True:
        print("djgsdgaaghjsjghas")
        druga_funkcja = True

        if -10.0 < x < 10.0 and 17.0 < y < 90.0:
                tablica[1][3] = None
                turtle.penup()
                turtle.goto(-10.0, 90.0)
                turtle.pendown()
                turtle.begin_fill()
                turtle.color("green yellow")
                for _ in range(2):
                    turtle.forward(image_width)
                    turtle.right(90)
                    turtle.forward(image_height)
                    turtle.right(90)
                turtle.end_fill()
        elif -40.0 < x < -20.0 and -70 < y < 5.0:
                tablica[2][2] = None
                turtle.penup()
                turtle.goto(-40.0, 5.0)
                turtle.pendown()
                turtle.begin_fill()
                turtle.color("green yellow")
                for _ in range(2):
                    turtle.forward(image_width)
                    turtle.right(90)
                    turtle.forward(image_height)
                    turtle.right(90)
                turtle.end_fill()
        elif -10.0 < x < 10.0 and -70 < y < 5.0:
                tablica[2][3] = None
                turtle.penup()
                turtle.goto(-10.0, 5.0)
                turtle.pendown()
                turtle.begin_fill()
                turtle.color("green yellow")
                for _ in range(2):
                    turtle.forward(image_width)
                    turtle.right(90)
                    turtle.forward(image_height)
                    turtle.right(90)
                turtle.end_fill()
        elif 20.0 < x < 40.0 and -70 < y < 5.0:
                tablica[2][4] = None
                turtle.penup()
                turtle.goto(20.0, 5.0)
                turtle.pendown()
                turtle.begin_fill()
                turtle.color("green yellow")
                for _ in range(2):
                    turtle.forward(image_width)
                    turtle.right(90)
                    turtle.forward(image_height)
                    turtle.right(90)
                turtle.end_fill()                                                                                           
        elif -70.0 < x < -50.0 and -155.0 < y < -80.0:
                tablica[3][1] = None
                turtle.penup()
                turtle.goto(-70.0, -80.0)
                turtle.pendown()
                turtle.begin_fill()
                turtle.color("green yellow")
                for _ in range(2):
                    turtle.forward(image_width)
                    turtle.right(90)
                    turtle.forward(image_height)
                    turtle.right(90)
                turtle.end_fill()
        elif -40.0 < x < -20.0 and -155.0 < y < -80.0:
                tablica[3][2] = None
                turtle.penup()
                turtle.goto(-40.0, -80.0)
                turtle.pendown()
                turtle.begin_fill()
                turtle.color("green yellow")
                for _ in range(2):
                    turtle.forward(image_width)
                    turtle.right(90)
                    turtle.forward(image_height)
                    turtle.right(90)
                turtle.end_fill()
        elif -10.0 < x < 10.0 and -155.0 < y < -80.0:
                tablica[3][3] = None
                turtle.penup()
                turtle.goto(-10.0, -80.0)
                turtle.pendown()
                turtle.begin_fill()
                turtle.color("green yellow")
                for _ in range(2):
                    turtle.forward(image_width)
                    turtle.right(90)
                    turtle.forward(image_height)
                    turtle.right(90)
                turtle.end_fill()
        elif 20.0 < x < 40.0 and -155.0 < y < -80.0:
                tablica[3][4] = None
                turtle.penup()
                turtle.goto(20.0, -80.0)
                turtle.pendown()
                turtle.begin_fill()
                turtle.color("green yellow")
                for _ in range(2):
                    turtle.forward(image_width)
                    turtle.right(90)
                    turtle.forward(image_height)
                    turtle.right(90)
                turtle.end_fill()
        elif 50.0 < x < 70.0 and -155.0 < y < -80.0:
                tablica[3][5] = None
                turtle.penup()
                turtle.goto(50.0, -80.0)
                turtle.pendown()
                turtle.begin_fill()
                turtle.color("green yellow")
                for _ in range(2):
                    turtle.forward(image_width)
                    turtle.right(90)
                    turtle.forward(image_height)
                    turtle.right(90)
                turtle.end_fill()
        elif -100.0 < x < -80.0 and -240.0 < y < -165.0: 
                tablica[4][0] = None
                turtle.penup()
                turtle.goto(-100.0, -165.0)
                turtle.pendown()
                turtle.begin_fill()
                turtle.color("green yellow")
                for _ in range(2):
                    turtle.forward(image_width)
                    turtle.right(90)
                    turtle.forward(image_height)
                    turtle.right(90)
                turtle.end_fill()
        elif -70.0 < x < -50.0 and -240.0 < y < -165.0:
                tablica[4][1] = None
                turtle.penup()
                turtle.goto(-70.0, -165.0)
                turtle.pendown()
                turtle.begin_fill()
                turtle.color("green yellow")
                for _ in range(2):
                    turtle.forward(image_width)
                    turtle.right(90)
                    turtle.forward(image_height)
                    turtle.right(90)
                turtle.end_fill()
        elif -40.0 < x < -20.0 and -240.0 < y < -165.0:
                tablica[4][2] = None
                turtle.penup()
                turtle.goto(-40.0, -165.0)
                turtle.pendown()
                turtle.begin_fill()
                turtle.color("green yellow")
                for _ in range(2):
                    turtle.forward(image_width)
                    turtle.right(90)
                    turtle.forward(image_height)
                    turtle.right(90)
                turtle.end_fill()
        elif -10.0 < x < 10.0 and -240.0 < y < -165.0:
                tablica[4][3] = None
                turtle.penup()
                turtle.goto(-10.0, -165.0)
                turtle.pendown()
                turtle.begin_fill()
                turtle.color("green yellow")
                for _ in range(2):
                    turtle.forward(image_width)
                    turtle.right(90)
                    turtle.forward(image_height)
                    turtle.right(90)
                turtle.end_fill()
        elif 20.0 < x < 40.0 and -240.0 < y < -165.0:
                tablica[4][4] = None
                turtle.penup()
                turtle.goto(20.0, -165.0)
                turtle.pendown()
                turtle.begin_fill()
                turtle.color("green yellow")
                for _ in range(2):
                    turtle.forward(image_width)
                    turtle.right(90)
                    turtle.forward(image_height)
                    turtle.right(90)
                turtle.end_fill()
        elif 50.0 < x < 70.0 and -240.0 < y < -165.0:
                tablica[4][5] = None
                turtle.penup()
                turtle.goto(50.0, -165.0)
                turtle.pendown()
                turtle.begin_fill()
                turtle.color("green yellow")
                for _ in range(2):
                    turtle.forward(image_width)
                    turtle.right(90)
                    turtle.forward(image_height)
                    turtle.right(90)
                turtle.end_fill()
        elif 80.0 < x < 100.0 and -240.0 < y < -165.0:
                tablica[4][6] = None
                turtle.penup()
                turtle.goto(80.0, -165.0)
                turtle.pendown()
                turtle.begin_fill()
                turtle.color("green yellow")
                for _ in range(2):
                    turtle.forward(image_width)
                    turtle.right(90)
                    turtle.forward(image_height)
                    turtle.right(90)
                turtle.end_fill()
    

   
     

'''
def Ile(licznik, k):
    licznik = 0
    for wiersz in tablica:
        for element in wiersz:
            if element == 'I':
                licznik += 1
        

    klikniecie(x=any,y=any)

    licznik2 = 0
    for wiersz in tablica:
        for element in wiersz:
            if element == 'I':
                licznik2 += 1
    roznica = licznik2 - licznik
    print(roznica)
    if k == roznica:
        ruch_komputera(0,0,0,0)


    
                

def ruch_gracza(x, y):
    
    global pierwsza_funkcja_wykonana
    pierwsza_funkcja_wykonana = False
    print("Kliknięto na obrazek w punkcie", x, y)
    if -56.0 < x < -32.0 and 255.0 < y < 290.0:
        pierwsza_funkcja_wykonana = True
        Ile(0, 1)
    elif -16.0 < x < 16.0 and 255.0 < y < 290.0:
        pierwsza_funkcja_wykonana = True
        Ile(0, 2)
    elif 32.0 < x < 56.0 and 255.0 < y < 290.0:
        pierwsza_funkcja_wykonana = True
        Ile(0, 3)



                
    '''

    

    
    







       







      

        
    
    









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
            
            #turtle.onscreenclick(ruch_gracza,1)
            turtle.onscreenclick(klikniecie,1)
            

# Rysowanie liczby w prawym górnym rogu
def draw_number(number, x, y):
    turtle.penup()
    turtle.goto(x, y)
    turtle.write(number, align="right", font=("Arial", 33, "normal"))

# Umieszczenie liczb 1, 2, 3 w prawym górnym rogu
draw_number(1, -30, 245)
draw_number(2, 15, 245)
draw_number(3, 60, 245)

# Uruchomienie pętli głównej turtle
turtle.mainloop()




def ruch_komputera(kol, rzad, ile, g):
    
        print("Ruch komputera")
        kol = random.randint(0, 6)
        rzad = random.randint(0, 6)
        ile = random.randint(1, 3)
        g = random.choice([-1, 1])
        if ile == 1:
            while tablica[kol][rzad] == None:
                rzad = random.randint(0, 6)
                kol = random.randint(0, 6)
            tablica[kol][rzad] = None
            turtle.penup()
            turtle.goto(-70.0 + 30.0 * (rzad - 1), 90.0 - 85 * (kol - 1))
            turtle.pendown()
            turtle.begin_fill()
            turtle.color("green yellow")
        elif ile == 2:
            while tablica[kol][rzad] == None:
                rzad = random.randint(0, 6)
                kol = random.randint(0, 6)
            tablica[kol][rzad] = None
            turtle.penup()
            turtle.goto(-70.0 + 30.0 * (rzad - 1), 90.0 - 85 * (kol - 1))
            turtle.pendown()
            turtle.begin_fill()
            turtle.color("green yellow")
            tablica[kol][rzad + g] = None
            turtle.penup()
            turtle.goto(-70.0 + 30.0 * (rzad + g - 1), 90.0 - 85 * (kol - 1))
            turtle.pendown()
            turtle.begin_fill()
            turtle.color("green yellow")
        elif ile == 3:
            while tablica[kol][rzad] == None:
                rzad = random.randint(0, 6)
                kol = random.randint(0, 6)
            tablica[kol][rzad] = None
            turtle.penup()
            turtle.goto(-70.0 + 30.0 * (rzad - 1), 90.0 - 85 * (kol - 1))
            turtle.pendown()
            turtle.begin_fill()
            turtle.color("green yellow")
            tablica[kol][rzad + g] = None
            turtle.penup()
            turtle.goto(-70.0 + 30.0 * (rzad + g - 1), 90.0 - 85 * (kol - 1))
            turtle.pendown()
            turtle.begin_fill()
            turtle.color("green yellow")
            tablica[kol][rzad - g] = None
            turtle.penup()
            turtle.goto(-70.0 + 30.0 * (rzad - g - 1), 90.0 - 85 * (kol - 1))
            turtle.pendown()
            turtle.begin_fill()
            turtle.color("green yellow")
