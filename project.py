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
    faktura = {
        "Kwota": kwota,
        "Data_platnosci": data,
        "Waluta": waluta
    }
    
    with open("dane/platnosci.txt", "a") as plik:
        json.dump(faktura, plik)
        plik.write('\n')

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

def main():
    kwota_faktury, data_faktury, kod_waluty_faktury = wprowadz_dane_faktury()
    kwota_platnosci, data_platnosci, kod_waluty_platnosci = wprowadz_dane_platnosci()

    zapisz_faktury_do_pliku(kwota_faktury, data_faktury, kod_waluty_faktury)
    zapisz_platnosc_do_pliku(kwota_platnosci, data_platnosci, kod_waluty_platnosci)
        
    pobierz_kurs_waluty(kod_waluty_faktury, data_faktury)

if __name__ == "__main__":
    main()


