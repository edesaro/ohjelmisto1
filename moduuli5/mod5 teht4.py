kaupungit = []

for i in range(5):
    kaupunki = input(f"anna {i+1}, kaupungin nimi:")
    kaupungit.append(kaupunki)

print("Syöttämäsi kaupungit")
for kaupunki in kaupungit:
    print(kaupunki)