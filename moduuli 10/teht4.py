import random


class Auto:
    def __init__(self, nimi, huippunopeus, matka=0):
        self.nimi = nimi
        self.nopeus = 0
        self.huippunopeus = huippunopeus
        self.matka = matka

    def kiihdyta(self, muutos):
        self.nopeus += muutos
        if self.nopeus > self.huippunopeus:
            self.nopeus = self.huippunopeus
        elif self.nopeus < 0:
            self.nopeus = 0

    def kulje(self, tunnit=1):
        self.matka += self.nopeus * tunnit

class Kilpailu:
    def __init__(self, nimi, pituus_km, autot):
        self.nimi = nimi
        self.pituus_km = pituus_km
        self.autot = autot

    def tunti_kuluu(self):
        for auto in self.autot:
            nopeuden_muutos = random.randint(-10, 15)
            auto.kiihdyta(nopeuden_muutos)
            auto.kulje()

    def tulosta_tilanne(self):
        print(f"{'Auto':<15}{'Nopeus (km/h)':<15}{'Matka (km)':<10}")
        print("-" * 40)
        for auto in self.autot:
            print(f"{auto.nimi:<15}{auto.nopeus:<15}{auto.matka:<10.1f}")

    def kilpailu_ohi(self):
        for auto in self.autot:
            if auto.matka >= self.pituus_km:
                return True
        return False




autot = [Auto(f"Auto {i+1}", random.randint(100, 200)) for i in range(10)]
kilpailu = Kilpailu("Suuri romuralli", 8000, autot)
tunti = 0
while not kilpailu.kilpailu_ohi():
    kilpailu.tunti_kuluu()
    tunti += 1
    if tunti % 10 == 0:
            print(f"Tunti {tunti}: Tilannekatsaus")
            kilpailu.tulosta_tilanne()

    print(f"Kilpailu päättynyt tunnilla {tunti}. Lopputilanne:")
    kilpailu.tulosta_tilanne()