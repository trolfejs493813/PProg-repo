def waga_calowita(ekwipunek):
    return sum(item["waga"] * item["ilosc"] for item in ekwipunek.values())

def aktualizuj_wartosci(ekwipunek):
    for item in ekwipunek.values():
        item["wartosc"] = item["waga"] * item["ilosc"]



def opcja1(ekwipunek, waga_maksymalna):
    for item in ekwipunek:
        print(f"{item}: {ekwipunek[item]['ilosc']}, {ekwipunek[item]['wartosc']}")

    print(f"Calkowita waga: {waga_calowita(ekwipunek)}/{waga_maksymalna}")


def opcja2(ekwipunek, waga_maksymalna):
    typ = input("Dodaj/kup: ").lower()

    if typ not in ["dodaj", "kup"]:
        print("Nie ma takiej opcji")
        return
    elif typ == "kup":
        item = input("Co chcesz kupic: ").lower()
        b = int(input(f"Wprowadź ilosc {item} do kupienia: "))
        if item in ekwipunek:
            ekwipunek[item]["ilosc"] += b
            ekwipunek["zloto"]["ilosc"] -= b * ekwipunek[item]["cena"]
        else:
            print("Nie ma takiego przedmiotu w sklepie")
        aktualizuj_wartosci(ekwipunek)

    elif typ == "dodaj":
        item = input("Co chcesz dodac: ").lower()
        b = int(input(f"Wprowadź ilosc {item} do dodania: "))

        if item in ekwipunek:
            ekwipunek[item]["ilosc"] += b
        else:
            waga = int(input(f"Wprowadź wage {item}: "))
            cena = int(input(f"Wprowadź cenę {item}: "))
            ekwipunek[item] = {"waga": waga, "ilosc": b, "cena": cena}
        aktualizuj_wartosci(ekwipunek)

        if waga_calowita(ekwipunek) > waga_maksymalna:
            print("Przekroczono maksymalna wage")
            ekwipunek[item]["ilosc"] -= b


def opcja3(ekwipunek):
    item = input("Co chcesz zuzyc: ").lower()

    if item in ekwipunek:
        b = int(input(f"Wprowadź ilosc {item} do zuzycia: "))

        if b >= ekwipunek[item]["ilosc"]:
            ekwipunek[item]["ilosc"] = 0
            print(f"Zuzyto wszystko")
        else:
            ekwipunek[item]["ilosc"] -= b
        aktualizuj_wartosci(ekwipunek)
    else:
        print("Blad - brak w ekwipunku")


def opcja4(ekwipunek):
    item = input("Co chcesz sprawdzic: ").lower()

    if item in ekwipunek:
        print(f"ilosc = {ekwipunek[item]['ilosc']} ")
        print(f"waga calkowita = {ekwipunek[item]['wartosc']}")
        print(f"waga 1 przedmiotu = {ekwipunek[item]['waga']}")
        print(f"cena 1 przedmiotu = {ekwipunek[item]['cena']}")
    else:
        print("Blad - brak w ekwipunku")



def menu():
    waga_maksymalna = 1000
    ekwipunek = {
                "miecz": {
                    "waga": 100,
                    "ilosc": 1,
                    "cena": 10
                    },
                "mikstura": {
                    "waga": 10,
                    "ilosc": 10,
                    "cena": 100
                    },
                "zloto": {
                    "waga": 1,
                    "ilosc": 50,
                    "cena": 1
                    }}

    aktualizuj_wartosci(ekwipunek)

    print("1 - Wyswietl ekwipunek")
    print("2 - Dodaj/kup przedmiot")
    print("3 - Zużyj przedmiot")
    print("4 - Sprawdź informacje o przedmiocie")
    print("5 - Wyjdź")

    while True:
        m = int(input("Jaka opcja (1-5): "))
        if m == 1:
            opcja1(ekwipunek, waga_maksymalna)
            
        elif m == 2:
            opcja2(ekwipunek, waga_maksymalna)

        elif m == 3:
            opcja3(ekwipunek)

        elif m == 4:
            opcja4(ekwipunek)

        elif m == 5:
            print("koniec")
            break
        else:
            print("Nie ma takiej wartosci")
            continue


menu()