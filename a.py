
import random

ile = random.randint(8,13) 

haslo = ""
znaki = "abcdefghijklmnopqrstuwvxyzABCDEFGHIJKLMNOPRSTUVWXYZ1234567890!@$%^&*"
for i in range(0,ile):
	los = random.randint(0,67)
	haslo = str(haslo)+znaki[los]
	
print("---------------------------")
print("Twoje hasło to: ", haslo)
print("---------------------------")
	

