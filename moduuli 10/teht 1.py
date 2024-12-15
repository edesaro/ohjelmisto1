class Hissi:
    def __init__(self,alin_kerros, ylin_kerros):
        self.alin_kerros = alin_kerros
        self.ylin_kerros = ylin_kerros
        self.nykyinen_kerros = alin_kerros
        print(f'Hissi on nyt alimassa kerroksessa {self.nykyinen_kerros}')

    def kerros_ylos (self):
        if self.nykyinen_kerros < self.ylin_kerros:
            self.nykyinen_kerros += 1
            print(f'Hissi on siirtynyt kerrokseen {self.nykyinen_kerros}')
        else:
            print('Hissi on ylimmässä kerroksessa')

    def kerros_alas(self):
        if self.nykyinen_kerros > self.alin_kerros:
            self.nykyinen_kerros -= 1
            print(f'Hissi on siirtynyt kerrokseen {self.nykyinen_kerros}')
        else:
            print('Hissi on alimmassa kerroksessa!')

    def siirry_kerrokseen (self, tavoite_kerros):
        if tavoite_kerros > self.nykyinen_kerros:
            while self.nykyinen_kerros < tavoite_kerros:
                self.kerros_ylos ()
        elif tavoite_kerros < self.nykyinen_kerros:
            while self.nykyinen_kerros > tavoite_kerros:
                self.kerros_alas ()
        else:
            print(f'Hissi on no kerroksessa {tavoite_kerros}')


hissi = Hissi(1, 10)


hissi.siirry_kerrokseen(5)

hissi.siirry_kerrokseen(1)