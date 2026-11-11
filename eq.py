def menu():
    ekwipunek = {
        "miecz": {
            "waga": 10,
            "ilosc": 1,
            "wartosc": 1},
        "mikstura": {
            "waga": 10,
            "ilosc": 1,
            "wartosc": 1},
        "zloto": {
            "waga": 10,
            "ilosc": 1,
            "wartosc": 1}}
    while True:
        m = int(input("Jaka opcja (1-5): "))
        if m == 1:
            opcja1()
            
        elif m == 2:
            item = input("Co chcesz dodac: ")
            b = int(input(f"Wprowadź ilosc {item} do dodania: "))
            ekwipunek[item] = ekwipunek.get(item, 0) + b
            if ekwipunek[item] > 100:
                print("Za duza waga")
                ekwipunek[item] = ekwipunek.get(item, 0) - b

        elif m == 3:
            item = input("Co chcesz zuzyc: ")
            if item.lower() in ekwipunek:
                b = int(input(f"Wprowadź ilosc {item} do zuzycia: "))
                if b >= ekwipunek[item]:
                    ekwipunek[item] = 0
                    print(f"Zuzyto wszystko")
                else:
                    ekwipunek[item] = ekwipunek.get(item, 0) - b

            else:
                print("Blad")

        elif m == 4:
            item = input("Co chcesz sprawdzic: ")
            print(ekwipunek[item])

        elif m == 5:
            print("koniec")
            break
        else:
            print("Nie ma takiej wartosci")
            continue

def opcja1():
    print(ekwipunek)




menu()