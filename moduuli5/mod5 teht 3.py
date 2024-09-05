def is_prime_number(num):
    if num < 1:
        return False
    for i in range(2,num):
        #print(i)

        if  num % i == 0:
            # jos jaollinen jollain i:n arvolla, palautetaan falce
            # ja funtion suoritus loppuu siihen
            return False
    # jos funktion suoritus on jatkunut tänne asti, niin palautetaan True
    return True

user_input = int(input("Anna testattava luku(>8: "))


if is_prime_number(user_input):
    print(f"Luku{user_input} on alkuluku")
else:
    print(f"Luku {user_input} ei ole alkuluku")
#print(is_prime_number(17))
#print(is_prime_number(17))
#print(is_prime_number(8))