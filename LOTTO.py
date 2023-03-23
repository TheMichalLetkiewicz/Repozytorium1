import random

zwycieskie_liczby = []
while len(zwycieskie_liczby) < 6:
    liczba = random.randint(1, 49)
    if liczba not in zwycieskie_liczby:
            zwycieskie_liczby.append(liczba)
        
        
        

    
print("Podaj lczbe w zakresie od 1 do 49.")

twoje_liczby=[]
while len(twoje_liczby) < 6:
      skreslona_liczba = input("Udawaj ze skreslasz jakas liczbe (ale w rzeczywistosci wpisz: )")
      if skreslona_liczba in twoje_liczby:
            print("Juz ja wybrales")
      elif skreslona_liczba < 1 or skreslona_liczba > 49:
            print("Podaj lczbe w zakresie od 1 do 49.")
      elif skreslona_liczba not in twoje_liczby:
            twoje_liczby.append(skreslona_liczba)



            
    
Iles_wygral = set(twoje_liczby)&set(zwycieskie_liczby)
Iles_trafil = len(Iles_wygral)
print("Liczby wylosowane: " , zwycieskie_liczby)
print("Liczby skreslone: " , twoje_liczby)
print("Liczb trafionych: " , Iles_trafil)
    