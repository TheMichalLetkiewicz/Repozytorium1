
import random

ile = random.randint(8,16) 


haslo = ""
znaki = "abcdefghijklmnopqrstuwvxyzABCDEFGHIJKLMNOPRSTUVWXYZ12345678901234567890!@$%^&*"

for i in range(0,ile):
	
	haslo = str(haslo)+znaki[random.randint(0,77)]
	
print("---------------------------")
print("Twoje hasło to: ", haslo)
print("---------------------------")
	

