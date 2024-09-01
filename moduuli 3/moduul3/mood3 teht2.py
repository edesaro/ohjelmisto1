

hyttiluokka = (input(" anna hyttiluokan LUX, A, B, C:"))


if hyttiluokka == "Lux" or "lux":
  print(f"LUX on parvekkeellinen hytti yläkannella")

elif hyttiluokka == "A" or "a":
  print(f"A on ikkunallinen hytti autokannen yläpuolella")
elif hyttiluokka == "B" or "b":
  print(f"B on ikkunaton hytti autokannen yläpuolella.")

elif hyttiluokka == "C" or "c":
  print(f"C on ikkunaton hytti autokannen alapuolella.")

else:
 print(f"Virheellinen hyttiluokka")

