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



class Talo:
    def __init__(self, alin_kerros, ylin_kerros, hissien_lkm):
        self.hissit = [Hissi(alin_kerros, ylin_kerros) for _ in range(hissien_lkm)]
        print(f"Talo on luotu, jossa on {hissien_lkm} hissiä kerroksissa {alin_kerros} - {ylin_kerros}.")

    def aja_hissia(self, hissin_numero, kohdekerros):
        if 0 <= hissin_numero < len(self.hissit):
            print(f"Ajetaan hissiä {hissin_numero} kohdekerrokseen {kohdekerros}")
            self.hissit[hissin_numero].siirry_kerrokseen(kohdekerros)
        else:
            print("Virhe: Hissin numero ei ole sallittu.")

    def palohalytys(self):
        print("Palohälytys! Kaikki hissit siirtyvät pohjakerrokseen.")
        for i in range(len(self.hissit)):
            print(f"Siirretään hissi {i} pohjakerrokseen.")
            self.hissit[i].siirry_kerrokseen(self.hissit[0].alin_kerros)



talo = Talo(1, 10, 3)

talo.aja_hissia(0, 5)


talo.aja_hissia(1, 8)

talo.aja_hissia(0, 1)
talo.palohalytys()