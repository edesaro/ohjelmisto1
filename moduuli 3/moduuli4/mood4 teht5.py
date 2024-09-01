oikea_tunnus = "python"
oikea_salasana = "rules"

yrityskerta = 0

while yrityskerta < 5:
    tunnus = input ("syötä käyttäjätunnus:")
    salasana = input("syötä salasana")

    if tunnus == oikea_tunnus and salasana == oikea_salasana:
        print("Tervetuloa")
        break
    else:
        yrityskerta =+ 1
        print(f"virheellinen tunnus tai salasana. Yrityksiä jäljella: {5-yrityskerta}")

if yrityskerta == 5:
    print("päsit sisään")
