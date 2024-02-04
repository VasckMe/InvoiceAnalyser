import json

# Wprowadzenie użytkownikiem danych faktur
def wprowadz_dane_faktury():
    kwota = float(input("Podaj kwotę faktury: "))
    data_faktury = input("Podaj datę faktury (RRRR-MM-DD): ")
    waluta = input("Podaj walutę: ")

    return kwota, data_faktury, waluta



# 
def zapisz_faktury(kwota, data, waluta):
    faktura = {
        "Kwota": kwota,
        "Data_faktury": data,
        "Waluta": waluta
    }
    
    with open("faktury.txt", "a") as plik:
        json.dump(faktura, plik)
        plik.write('\n')
    
    return faktura




    



