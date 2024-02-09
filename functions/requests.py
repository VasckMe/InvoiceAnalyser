from pip._vendor import requests

# Pobiera kurs waluty metoda "GET" z NBP API
def pobierz_kurs_waluty(kod_waluty, data):
    if kod_waluty == "PLN":
        return 1.0

    url = f'http://api.nbp.pl/api/exchangerates/rates/A/{kod_waluty}/{data}/?format=json'
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