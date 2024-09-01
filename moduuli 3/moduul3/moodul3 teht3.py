sukupuoli = input("Anna sukupuolesi (nainen/mies)")
hemoglobiini = int(input("Anna hemoglobiini (g/l"))



if sukupuoli == "nainen" or sukupuoli == "Nainen":
    if hemoglobiini < 117:
        print("hemoglobini on alhainen")
    elif 117 <= hemoglobiini <= 175:
        print("hemoblobiini on normaali")
    else:
        print("hemoglobiini korkea")

elif sukupuoli == "mies" or sukupuoli == "Mies":
    if hemoglobiini < 134:
        print("hemoglobiini on alhainen")
    elif 134 <= hemoglobiini <= 195:
        print("hemoblobiini on normaali")
    else:
        print("hemoglobiini korkea")