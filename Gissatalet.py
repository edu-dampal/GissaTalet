import random as rand

namn = input("Vad heter du?")
print ("")

print (f"Välkommen till spelet {namn}!")
print ("")

rätt_tal = rand.randint(1,11)
print (f"{rätt_tal}")

gissning = int(input("Gissa ett tal mellan 1 och 10:"))
print ("")

print ("Försök 1")
if gissning == rätt_tal:
    print ("Du har gissat rätt")
else:
    print ("Du har gissat fel")
    print (f"Rätta svaret var {rätt_tal}")
