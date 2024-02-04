import json

# Wprowadzenie użytkownikiem danych faktur
def wprowadz_dane_faktury():
    kwota = float(input("Podaj kwotę faktury: "))
    data_faktury = input("Podaj datę faktury (w formacie YYYY-MM-DD): ")
    waluta = input("Podaj walutę: ")

    return kwota, data_faktury, waluta



