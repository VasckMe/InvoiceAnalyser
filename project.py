import json
from pip._vendor import requests

# Wprowadzenie użytkownikiem danych faktur
def wprowadz_dane_faktury():
    kwota = float(input("Podaj kwotę faktury: "))
    data_faktury = input("Podaj datę faktury (RRRR-MM-DD): ")
    waluta = input("Podaj walutę: ")

    return kwota, data_faktury, waluta

# Wprowadzenie użytkownikiem danych platnosci faktury
def wprowadz_dane_platnosci():
    kwota = float(input("Podaj kwotę płatności: "))
    data_platnosci = input("Podaj datę płatności (RRRR-MM-DD): ")
    waluta = input("Podaj walutę płatności: ")

    return kwota, data_platnosci, waluta

# Zapis danych faktur w plik faktury.txt
def zapisz_faktury_do_pliku(kwota, data, waluta):
    faktura = {
        "Kwota": kwota,
        "Data_faktury": data,
        "Waluta": waluta
    }
    
    with open("dane/faktury.txt", "a") as plik:
        json.dump(faktura, plik)
        plik.write('\n')

# Zapis danych platnosci w plik platnosci.txt
def zapisz_platnosc_do_pliku(kwota, data, waluta):
    platnosc = {
        "Kwota": kwota,
        "Data_platnosci": data,
        "Waluta": waluta
    }
    
    with open("dane/platnosci.txt", "a") as plik:
        json.dump(platnosc, plik)
        plik.write('\n')

# Pobiera kurs waluty metoda "GET" z NBP API
def pobierz_kurs_waluty(kod_waluty, data):
    url = 'http://api.nbp.pl/api/exchangerates/rates/a/%7Bkod_waluty%7D/%7Bdata%7D/?format=json'
    response = requests.get(url)
    match response.status_code:
        case 200:
            kurs_waluty = response.json()['rates'][0]['mid']
            return kurs_waluty
        case 404:
            print(f'404 Błąd podczas pobierania kursu dla {kod_waluty} na dzień {data}')
        case _:
            print(f'{response.status_code} Błąd podczas pobierania kursu dla {kod_waluty} na dzień {data}')

    return None

# Zapis danych platnosci w plik platnosci.txt
def zapisz_wynik_platnosci_do_pliku(wynik, ostatek):
    wynik_platnosci = {
        "Wynik_platnosci": wynik,
        "Ostatek": ostatek
    }
    
    with open("dane/wynik_platnosci.txt", "a") as plik:
        json.dump(wynik_platnosci, plik)
        plik.write('\n')

# Oblicz roznice kwoty faktury i kwoty platnosci
def oblicz_roznice(kwota_faktury, kwota_platnosci):
    roznica = kwota_faktury - kwota_platnosci

    if roznica == 0:
        return "Paid", roznica
    elif roznica > 0:
        return "Overpaid", roznica
    else:
        return "Underpaid", roznica

def main():
    kwota_faktury, data_faktury, kod_waluty_faktury = wprowadz_dane_faktury()
    kwota_platnosci, data_platnosci, kod_waluty_platnosci = wprowadz_dane_platnosci()

    zapisz_faktury_do_pliku(kwota_faktury, data_faktury, kod_waluty_faktury)
    zapisz_platnosc_do_pliku(kwota_platnosci, data_platnosci, kod_waluty_platnosci)
        
    kurs_waluty_faktury = pobierz_kurs_waluty(kod_waluty_faktury, data_faktury)
    kurs_waluty_platnosci = pobierz_kurs_waluty(kod_waluty_platnosci, data_platnosci)

    if kurs_waluty_faktury is not None and kurs_waluty_platnosci is not None:
        wynik, roznica = oblicz_roznice(kwota_faktury*kurs_waluty_faktury, kwota_platnosci*kurs_waluty_platnosci)
        zapisz_wynik_platnosci_do_pliku(wynik, roznica)
    else:
        print("Error appeared, kurs_waluty_faktury or kurs_waluty_platnosci is None")

if __name__ == "__main__":
    main()