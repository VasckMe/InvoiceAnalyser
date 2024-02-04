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