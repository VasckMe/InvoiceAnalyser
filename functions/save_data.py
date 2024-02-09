import json

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

# Zapis danych platnosci w plik platnosci.txt
def zapisz_wynik_platnosci_do_pliku(wynik_string, ostatek):
    wynik_platnosci = {
        "Wynik_platnosci": wynik_string,
        "Ostatek": ostatek
    }
    
    with open("dane/wynik_platnosci.txt", "a") as plik:
        json.dump(wynik_platnosci, plik)
        plik.write('\n')