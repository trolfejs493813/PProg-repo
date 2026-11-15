def opcja1(ekwipunek):
    print(ekwipunek)

def opcja2(ekwipunek):
    item = input("Co chcesz dodac: ")
    b = int(input(f"Wprowadź ilosc {item} do dodania: "))
    if ekwipunek[item]["ilosc"] > 100:
        print("Za duza waga")
    else:
        ekwipunek[item]["ilosc"] += b



def opcja3(ekwipunek):
    item = input("Co chcesz zuzyc: ")
    if item.lower() in ekwipunek:
        b = int(input(f"Wprowadź ilosc {item} do zuzycia: "))
        if b >= ekwipunek[item]:
            ekwipunek[item] = 0
            print(f"Zuzyto wszystko")
        else:
            ekwipunek[item]["ilosc"] -= b
    else:
        print("Blad")

def opcja4(ekwipunek):
    item = input("Co chcesz sprawdzic: ")
    print(ekwipunek[item])


def menu():
    ekwipunek = {
                "miecz": {
                    "waga": 10,
                    "ilosc": 1,
                    },
                "mikstura": {
                    "waga": 10,
                    "ilosc": 10,
                    },
                "zloto": {
                    "waga": 10,
                    "ilosc": 50,
                    }}

    while True:
        m = int(input("Jaka opcja (1-5): "))
        if m == 1:
            opcja1(ekwipunek)
            
        elif m == 2:
            opcja2(ekwipunek)

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