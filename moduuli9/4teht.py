import random
class Auto:
    def __init__(self, rekisteritunnus, huippunopeus,):
        self.rekisteritunnus = rekisteritunnus
        self.huippunopeus = huippunopeus
        self.nopeus = 0
        self.matka = 0

    def kiihdyta(self, muutos):
        uusi_nopeus = self.nopeus + muutos
        if uusi_nopeus > self.huippunopeus:
            self.nopeus = self.huippunopeus
        elif uusi_nopeus < 0:
            self.nopeus = 0
        else:
            self.nopeus = uusi_nopeus


    def kulje(self, tuntia):
        self.matka += self.nopeus * tuntia

    def __str__(self):
        return f"{self.rekisteritunnus}  Huippunopeus: {self.huippunopeus} km/h  Nopeus: {self.nopeus} km/h  Kuljettu matka: {self.matka:.1f} km"


def luo_autot(maara):
    autot=[]
    for i in range(1,maara+1):
        rekisteritunnus = f'ABC-{i}'
        huippunopeus = random.randint(100,200)
        autot.append(Auto(rekisteritunnus, huippunopeus))
    return autot

def kilpailu(autot):
    kilpailu_jatkuu = True
    tunti = 0

    while kilpailu_jatkuu:
        tunti += 1
        print(f'Tunti {tunti}')

        for auto in autot:
            nopeuden_muutos = random.randint(-10,15)
            auto.kiihdyta(nopeuden_muutos)
            auto.kulje(1)

            if auto.matka>=10000:
                kilpailu_jatkuu = False

    print('Kilpailu päättyi')
    for auto in autot:
        print(auto)

autot = luo_autot(10)
kilpailu(autot)




