luvut = []
luku = input("Anna luku tai lopeta painamalla Enter: ")
while luku != "":
    luvut.append(int(luku))
    luku = input("Anna seuraava luku tai lopeta painamalla Enter: ")
luvut.sort(reverse = True)

print("Viisi suurinta lukua ovat:", luvut[:5])