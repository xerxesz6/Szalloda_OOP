import random

class Szoba:
    def __init__(self, szobaszam, foglalt, ar):
        self.szobaszam = szobaszam
        self.foglalt = foglalt
        self.ar = ar

class Egyagyas(Szoba):
    extrak = []
    
class Ketagyas(Szoba):
    extrak = ["Panoráma"]
    
class Lakosztaly(Szoba):
    extrak = ["Panoráma", "klíma", "jacuzzi"]
    
szobak = []

def Feltoltes(szobak):
    for i in range(10):
        szobaszam = i + 1
        foglalt = random.choice([True, False])
        ar = random.randint(25000, 65000)
        szoba_tipus = random.choice([Egyagyas, Ketagyas, Lakosztaly])
        if szoba_tipus == Egyagyas:
            szobak.append(Egyagyas(szobaszam, foglalt, ar))
        elif szoba_tipus == Ketagyas:
            szobak.append(Ketagyas(szobaszam, foglalt, ar))
        elif szoba_tipus == Lakosztaly:
            szobak.append(Lakosztaly(szobaszam, foglalt, ar))
            
Feltoltes(szobak)

while True:
    print("Válassz egy lehetőséget:")
    print("1. Foglalások lekérdezése")
    print("2. Árak lekérdezése")
    print("3. Új foglalás leadása")
    print("4. Kilépés")

    valasztas = input("Választás (1/2/3/4): ")

    if valasztas == "1":
        for szoba in szobak:
            if szoba.foglalt:
                print(f"Szobaszám: {szoba.szobaszam}, Foglalt: Igen, Ár: {szoba.ar}, Extrák: {szoba.extrak if hasattr(szoba, 'extrak') else 'Nincs'}")
            else:
                print(f"Szobaszám: {szoba.szobaszam}, Foglalt: Nem, Ár: {szoba.ar}")
    elif valasztas == "2":
        for szoba in szobak:
            print(f"Szobaszám: {szoba.szobaszam}, Ár: {szoba.ar}")
    elif valasztas == "3":
        while True:
            szobaszam = int(input("Kérlek add meg a foglalandó szoba számát: "))
            talalt = False
            for szoba in szobak:
                if szoba.szobaszam == szobaszam:
                    talalt = True
                    if szoba.foglalt:
                        print("Ez a szoba már foglalt!")
                    else:
                        szoba.foglalt = True
                        print("Sikeres foglalás")
                    break
            if talalt:
                break
            else:
                print("Nincs ilyen szobaszám!")
                folytatni = input("Szeretnéd újra megpróbálni? (igen/nem): ")
                if folytatni.lower() != "igen":
                    break
    elif valasztas == "4":
        break
    else:
        print("Érvénytelen választás. Kérlek válassz újra.")