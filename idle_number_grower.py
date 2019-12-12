import time

galaxy1 = 0
galaxy2 = 0

while galaxy1 < 50:
    for n in range(1):
        galaxy1 += 5
    print(galaxy1)
    time.sleep(.2)

while galaxy1 < 100:
    for n in range(1):
        galaxy1 += 10
    print(galaxy1)
    time.sleep(.2)

while galaxy1 < 500:
    for n in range(1):
        galaxy1 += 100
    print(galaxy1)
    time.sleep(.2)

while galaxy1 < 1000:
    for n in range(1):
        galaxy1 += 500
        galaxy2 += 100
    print(galaxy1, '  ', galaxy2)
    time.sleep(.2)

while galaxy1 < 5000:
    for n in range(1):
        galaxy1 += 800
        galaxy2 += 1000
    print(galaxy1, '  ', galaxy2)
    time.sleep(.2)