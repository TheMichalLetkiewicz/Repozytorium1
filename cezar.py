def cezar(tekst, shift):
  
    szyfr_tekst = ""
    for char in tekst:
        
        if not char.isalpha():
            szyfr_tekst += char
        
        elif char.isupper():
            szyfr_tekst += chr((ord(char) + przesuniecie - 65) % 26 + 65)
        
        else:
            szyfr_tekst += chr((ord(char) + przesuniecie - 97) % 26 + 97)
    return szyfr_tekst


# Przykład użycia.
tekst = input("Podaj tekst: ")
przesuniecie = input("Ile wynosi klucz: ")
ciphered_text = cezar(tekst, przesuniecie)
print(ciphered_text)
