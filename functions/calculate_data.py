# Oblicz roznice kwoty faktury i kwoty platnosci
def oblicz_roznice(kwota_faktury, kwota_platnosci):
    roznica = abs(kwota_faktury - kwota_platnosci)
    if roznica < 0.001:
        return "Oplacona", roznica
    elif kwota_faktury < kwota_platnosci:
        return "Za duzo oplacona", roznica
    else:
        return "Nie oplacona", roznica