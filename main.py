from functions.input_data import wprowadz_dane_faktury, wprowadz_dane_platnosci
from functions.save_data import zapisz_faktury_do_pliku, zapisz_platnosc_do_pliku, zapisz_wynik_platnosci_do_pliku
from functions.calculate_data import oblicz_roznice
from functions.addictive_functions import spoboj_ponownie
from functions.requests import pobierz_kurs_waluty

def main():
    # Wprowadzenie danych
    kwota_faktury, data_faktury, kod_waluty_faktury = wprowadz_dane_faktury()
    kwota_platnosci, data_platnosci, kod_waluty_platnosci = wprowadz_dane_platnosci()

    # Zapis danych do pliku
    zapisz_faktury_do_pliku(kwota_faktury, data_faktury, kod_waluty_faktury)
    zapisz_platnosc_do_pliku(kwota_platnosci, data_platnosci, kod_waluty_platnosci)

    # Pobieranie kursu walut
    kurs_waluty_faktury = pobierz_kurs_waluty(kod_waluty_faktury, data_faktury)
    kurs_waluty_platnosci = pobierz_kurs_waluty(kod_waluty_platnosci, data_platnosci)

    # Sprawdzenie, czy pobrali sie kursy walut, obliczanie roznicy i zapis do pliku
    if kurs_waluty_faktury is not None and kurs_waluty_platnosci is not None:
        wynik_roznicy, roznica = oblicz_roznice(kwota_faktury*kurs_waluty_faktury, kwota_platnosci*kurs_waluty_platnosci)
        zapisz_wynik_platnosci_do_pliku(wynik_roznicy, roznica)

    # Uruchomic program ponownie
    spoboj_ponownie("Chcesz kontynuowac ponownie? TAK/NIE", main)

if __name__ == "__main__":
    main()