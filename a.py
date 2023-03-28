zbior=[]
dlugosc_zbioru = int(input("Ile liczb chcesz posortowac: "))
while len(zbior) < dlugosc_zbioru:
    element_zbioru = int(input("Podaj liczbe: "))
    zbior.append(element_zbioru)

def sortuj(zbior):
    zbior.sort()
    return zbior


zbior_posortowany = sortuj(zbior)
print(zbior_posortowany) 