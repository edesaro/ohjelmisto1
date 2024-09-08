import random

def heittaa_noppa ():
    return random.randint(1,6)

def main ():
    silmaluku = 0
    while silmaluku != 6:
        silmaluku = heittaa_noppa()
        print(f"Heiton tulos: {silmaluku}")


