import random
N = 100
n = 0
iterator = 0
while iterator < N:
    iterator += 1
    x = random.uniform(-1,1)
    y = random.uniform(-1,1)
    print(f"arvioitu piste: ({x:.2f}, {y:.2f})")
    if x**2 + y**2 <1:
        print("Piste on yksikköympyrässä.")
        n += 1


piin_likiarvo = 4 * n / N
print(f"piin likiarvo: {piin_likiarvo:2f}")