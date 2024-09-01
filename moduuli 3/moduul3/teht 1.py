
alamitta = 37


pituus = float(input("Kuhan pituus senttimetreina: "))



if pituus < alamitta:
    saamatta = alamitta - pituus
    print(f"Palauta kuha. Kuha on {saamatta} cm liian  lyhyt.")


else:
    print(" Voit ottaa kuhan, sopivan kokoinen.")