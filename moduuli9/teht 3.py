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
        print(f'Nopeus on {self.nopeus} km/h')


    def kulje(self, tuntia):
        kuljettu_matka = self.nopeus * tuntia
        print(f'Auto kulki {kuljettu_matka}')



auto = Auto('ABC-123', 142 )

auto.kiihdyta(60)
auto.kulje(1.5)