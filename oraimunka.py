#1.Feladat: Kérjünk be 5 számot, és írjuk ki hogy páros vagy páratlan.

for x in range(1,6,1)

    szam = int(input("Kérlek adj meg egy számot:"))

    if szam % 2 == 0:
        print("Páros")
    else:
        print("Páratlan")
