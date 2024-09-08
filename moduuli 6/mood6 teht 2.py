import random


def heita_noppaa(tahkot):
    """Palauttaa satunnaisen nopan silmäluvun väliltä 1..tahkot."""
    return random.randint(1, tahkot)


def main():
    try:
        tahkot = int(input("Anna nopan tahkojen määrä: "))
        if tahkot < 1:
            raise ValueError("Tahkojen määrä tulee olla positiivinen kokonaisluku.")
    except ValueError as e:
        print(f"Virhe: {e}")
        return

    maksimi_silmavalu = tahkot
    while silmavalue != maksimi_silmavalu:
        silmavalue = heita_noppaa(tahkot)
        print(f"Nopan silmäluvut: {silmavalue}")