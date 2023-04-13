jaka_fukcja = (input("Podaj dla jakiej funkcji obliczyc miejsce zerowe(liniowa,kwadratowa): "))

if jaka_fukcja == "liniowa": # y = ax + b
    a=float(input("Podaj wspolczynnik kierunkowy a: "))
    b=float(input("Podaj wyraz wolny b: "))
    if a == 0:
        if b == 0:
            print("Funkcja posiada nieskończenie wiele miejsc zerowych.")
        else:
            print("Funkcja nie posiada miejsc zerowych.")
    else:
        x = -b/a
        print(x)
elif jaka_fukcja == "kwadratowa": # y = ax**2 + bx + c
    a=float(input("Podaj a funkcji kwadratowej: "))
    b=float(input("Podaj b funkcji kwadratowej: ")) 
    c=float(input("Podaj c funkcji kwadratowej: ")) #delta = b**2-4*a*c
    delta = b**2-4*a*c
    print("delta wynosi:",delta)
    if a == 0:
        if b == 0:
            if c==0:
                print("Funkcja posiada nieskończenie wiele miejsc zerowych.")
    elif delta<0:
        print("Funkcja nie posiada miejsc zerowych.")
    elif delta>0:
        mz1=(-b-delta**(1/2))/(2*a)
        mz2=(-b+delta**(1/2))/(2*a)
        print("Miejsca zerowe funkcji to:", mz1, mz2)        
            

        

            


    

