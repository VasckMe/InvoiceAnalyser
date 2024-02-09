from functions.verify_data import is_valid_date, is_float
from functions.addictive_functions import spoboj_ponownie

# Wprowadzenie użytkownikiem danych platnosci faktury
def wprowadz_dane_platnosci():
    kwota = input("Podaj kwotę płatności: ")

    if is_float(kwota):
        kwota_float = float(kwota)
    else:
        print("Nieprawidlowy format kwoty")
        spoboj_ponownie("Chcesz kontynuowac ponownie? TAK/NIE", wprowadz_dane_platnosci)

    data = input("Podaj datę płatności (RRRR-MM-DD): ")

    if not is_valid_date(data):
        print("Nieprawidlowy format daty")
        spoboj_ponownie("Chcesz kontynuowac ponownie? TAK/NIE", wprowadz_dane_platnosci)

    waluta = input("Podaj walutę płatności: ").upper()

    return kwota_float, data, waluta

# Wprowadzenie użytkownikiem danych faktur
def wprowadz_dane_faktury():
    kwota = input("Podaj kwotę faktury: ")

    if is_float(kwota):
        kwota_float = float(kwota)
    else:
        print("Nieprawidlowy format kwoty")
        spoboj_ponownie("Chcesz kontynuowac ponownie? TAK/NIE", wprowadz_dane_faktury)

    data = input("Podaj datę faktury (RRRR-MM-DD): ")

    if not is_valid_date(data):
        print("Nieprawidlowy format daty")
        spoboj_ponownie("Chcesz kontynuowac ponownie? TAK/NIE", wprowadz_dane_faktury)

    waluta = input("Podaj walutę faktury: ").upper()

    return kwota_float, data, waluta