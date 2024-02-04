import json

# Wprowadzenie użytkownikiem danych platnosci faktury
def wprowadz_dane_platnosci():
    kwota = float(input("Podaj kwotę płatności: "))
    data_platnosci = input("Podaj datę płatności (RRRR-MM-DD): ")
    waluta = input("Podaj walutę płatności: ")

    return kwota, data_platnosci, waluta

# Wprowadzenie użytkownikiem danych faktur
def wprowadz_dane_faktury():
    kwota = float(input("Podaj kwotę faktury: "))
    data_faktury = input("Podaj datę faktury (RRRR-MM-DD): ")
    waluta = input("Podaj walutę: ")

    return kwota, data_faktury, waluta

# Zapis danych faktur w plik faktury.txt
def zapisz_faktury(kwota, data, waluta):
    faktura = {
        "Kwota": kwota,
        "Data_faktury": data,
        "Waluta": waluta
    }
    
    with open("faktury.txt", "a") as plik:
        json.dump(faktura, plik)
        plik.write('\n')

# Zapis danych platnosci w plik platnosci.txt
def zapisz_platnosc(kwota, data, waluta):
    faktura = {
        "Kwota": kwota,
        "Data_platnosci": data,
        "Waluta": waluta
    }
    
    with open("platnosci.txt", "a") as plik:
        json.dump(faktura, plik)
        plik.write('\n')