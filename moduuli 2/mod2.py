# Syötteen lukeminen
import age

name = input ("Anna nimesi: ")
# name = "Matti"
# \ on escape-merkki, jolla voi tuottaa esim. tabin tai rivi
print("Moi ´\t " + name) # "Moi " + Matti" -> "Moi Matti"

# age = "7"
# käyttäjän syöte on aina merkkijono

print("Anna ikäsi; " + age)
# Muutetaan merkkijono (str) kokonaisluvuksi (int) ja lisätään

age = int(age) + 1 # "7" -> 7 + 1 -> = 8
age_string = str(age) # muutetaan  int -> string, esim. 8 -> "8"
print("Ikäsi on vuoden päästä" + age)

age = age + 1
print("Ikäsi on kahden vuoden päästä " + str(age))

# käyttäjän pituus metreinä liukuluku (float)
height = input("Anna pituus: ")

# tulos f-string muodossa, ei tarvita  str() - funktiota
print(f"Nimi: {name}, Ikä: {age*2}, Pituus: {height}." )



# kokonaisluvun kokonaisluvun arpominen väliltä 1-6


