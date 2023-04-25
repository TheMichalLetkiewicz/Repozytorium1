#cezar szyfr caly ten

male_litery={
"a":1,
"ą":2,
"b":3,
"c":4,
"ć":5,
"d":6,
"e":7,
"ę":8,
"f":9,
"g":10,
"h":11,
"i":12,
"j":13,
"k":14,
"l":15,
"ł":16,
"m":17,
"n":18,
"ń":19,
"o":20,
"ó":21,
"p":22,
"q":23,
"r":24,
"s":25,
"ś":26,
"t":27,
"u":28,
"v":29,
"w":30,
"x":31,
"y":32,
"z":33,
"ź":34,
"ż":35
}

duze_litery={
"A":1,
"Ą":2,
"B":3,
"C":4,
"Ć":5,
"D":6,
"E":7,
"Ę":8,
"F":9,
"G":10,
"H":11,
"I":12,
"J":13,
"K":14,
"L":15,
"Ł":16,
"M":17,
"N":18,
"Ń":19,
"O":20,
"Ó":21,
"P":22,
"Q":23,
"R":24,
"S":25,
"Ś":26,
"T":27,
"U":28,
"V":29,
"W":30,
"X":31,
"Y":32,
"Z":33,
"Ź":34,
"Ż":35
}

klucz = int(input("Podaj klucz: "))
tekst_uzytkownika = input("Podaj tekst: ")


szyfr = ""
for znak in tekst_uzytkownika:
    if znak in male_litery:
        indeks = male_litery[znak]
        indeks_szyfru = (indeks + klucz) % 36
        nowy_znak = list(male_litery.keys())[list(male_litery.values()).index(indeks_szyfru)]
        szyfr += nowy_znak
    elif znak in duze_litery:
        indeks = duze_litery[znak]
        indeks_szyfru = (indeks + klucz) % 36
        nowy_znak = list(duze_litery.keys())[list(duze_litery.values()).index(indeks_szyfru)]
        szyfr += nowy_znak
    else:
        szyfr += znak

print("Szyfrowany tekst:", szyfr)



