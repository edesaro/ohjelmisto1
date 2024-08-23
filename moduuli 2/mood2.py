import random
import math


käyttäjä = input('Anna nimesi: ')

print("Terve, " + käyttäjä + "!")



r = float(input("Anna ympyrän säde (m): "))
#ympyran_sade circle_radius
area = math.pi * r * r
print(f"Ympyrän, jona säde on {r}, pinta-ala on {area:.1f} neliömetriä.")


one = float(input("Anna kanta: "))
kaks = float(input("Anna korkeus: "))

pinta_ala = one * kaks
print("Pinta-ala on " + str(pinta_ala))

print(f"Kanta on {one}, Korkeus on {kaks}. Pinta-ala on {pinta_ala}")

nelja = float(input("Anna kanta"))
vis = float(input("Anna korkeus"))

piiri = nelja + nelja + vis + vis
print("piiri on " + str(piiri))

print(f"kanta on {nelja}, korkeus on {vis}. piiri on {piiri}")

luku_1 = float(input("Anna luku: "))
luku_2 = float(input("Anna luku: "))
luku_3 = float(input("Anna luku: "))

summa = luku_1 + luku_2 + luku_3
print("summa on " + str(summa))

tulo = luku_1 * luku_2 * luku_3
print("tulo on " + str(tulo))

keskiarvo = (summa/3)
print("keskiarvo on " + str(keskiarvo))


leiviskat = float(input("Anna leviskat: "))
naulat = float(input("Anna naulat: "))
luodit = float(input("Anna luodit: "))

leiviskat_grammoina = leiviskat * 20.0 * 32.0 * 13.3

naulat_grammoina = naulat * 32.0 * 13.3

luodit_grammoina = luodit * 13.3


kokonaispaino_grammoina = float(leiviskat_grammoina + naulat_grammoina + luodit_grammoina)

kilogrammat = int(kokonaispaino_grammoina // 1000)
grammat = kokonaispaino_grammoina % 1000

print(f"tulos kilogrammoina ja grammoina:")
print(f"{kilogrammat} kilogrammaa ja {grammat:.2f} grammaa.")

random_number1 = random.randint(0,9)
random_number2 = random.randint(0,9)
random_number3 = random.randint(0,9)

print(f"satunnainen luku 0-9: {random_number1}{random_number2}{random_number3}")


random_number1 = random.randint(0,6)
random_number2 = random.randint(0,6)
random_number3 = random.randint(0,6)
random_number4 = random.randint(0,6)

print(f"satunnainen luku 0-9: {random_number1}{random_number2}{random_number3}{random_number4}")





