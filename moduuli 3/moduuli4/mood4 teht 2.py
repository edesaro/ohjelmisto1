while True:

    tuuma = float(input("anna tuumien määrä (negatiivinen luku lopettaa):"))

    if tuuma < 0:
        print("negatiivinen luku annettu, ohjelma lopetetaan.")
        break

    sentit = tuuma * 2.54

    print(f"{tuuma} tuumaa on {sentit: .2f} senttimetria")




