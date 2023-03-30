jaka_fukcja = int(input("Podaj dla jakiej funkcji obliczyc miejsce zerowe(liniowa,kwadratowa): "))

if jaka_fukcja == "liniowa": # y = ax + b
    a=float(input("Podaj wspolczynnik kierunkowy: "))
    b=float(input("Podaj wyraz wolny: "))
    if a == 0:
        if b == 0:
            print("Funkcja posiada nieskończenie wiele rozwiązań.")
        else:
            print("Funkcja nie posiada rozwiązań.")
    else:
        x = -b/a
        print(x)

    

