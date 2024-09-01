vuosi = int(input("Anna vuosiluku: "))

if vuosi % 400 == 0 or (vuosi % 4 == 0 and not vuosi % 100 == 0):
    print("On karkausvuosi.")

else:
    print("Ei ole karkausvuosi")


# bonus: tulostaa kaikki karkausvuodet annettuun vuosilukuun asti

iterator = 0
while iterator < vuosi:
    iterator+= 4
    if iterator % 400 == 0 or not iterator % 100 == 0:
        print(f"{iterator} on karkausvuosi")