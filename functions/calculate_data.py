# Oblicz roznice kwoty faktury i kwoty platnosci
def oblicz_roznice(kwota_faktury, kwota_platnosci):
    roznica = round(abs(kwota_faktury - kwota_platnosci), 2)
    if roznica < 0.001:
        print("Faktura zostala oplacona")
        return "Oplacona", roznica
    elif kwota_faktury < kwota_platnosci:
        print("Faktura zostala oplacona, ostatek na koncie: ",roznica)
        return "Oplacona z ostatkiem", roznica
    else:
        print("Faktora nie zostala oplacona, brakuje: ",roznica)
        return "Nie oplacona, brakuje", roznica