import random
heittokertoja = int(input("Monta arpakuutiota heitetään? "))

summa = 0

for i in range (heittokertoja):

    heitto = random.randint(1,6)
    summa+=heitto

print(f"silmälukujen summa on {summa}")