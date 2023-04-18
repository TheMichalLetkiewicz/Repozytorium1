#X = 10
#L = 50
#C = 100
#D = 500
#M = 1000

jednosci = ["", "I", "II", "III", "IV", "V", "VI", "VII", "IIX", "IX"]
dziesiatki = ["", "X", "XX", "XXX", "XL", "L", "LX", "LXX", "XXC", "CX"]
setki = ["", "C", "CC", "CCC", "CD", "D", "DC", "DCC", "CCM", "CM"]


arab = input("podaj liczbę")
while len(arab) < 4:
	arab = "0" + arab
print (int(arab[-4]) * "M" + setki[int(arab[-3])] + dziesiatki[int(arab[-2])] + jednosci[int(arab[-1])])



