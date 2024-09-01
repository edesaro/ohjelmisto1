import random

oikea_luku = random.randint (1, 10)

while True:
    arvaus = int(input("Arvaa luku väliltä 1-10:"))
    if arvaus < oikea_luku:
        print(" Liian pieni luku")

    elif arvaus > oikea_luku:
        print("Liian suuri luku")

    else:
        print("Arvasit oikein")
        break