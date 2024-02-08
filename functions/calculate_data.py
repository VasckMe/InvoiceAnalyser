# Oblicz roznice kwoty faktury i kwoty platnosci
def oblicz_roznice(kwota_faktury, kwota_platnosci):
    roznica = kwota_faktury - kwota_platnosci

    if roznica == 0:
        return "Paid", roznica
    elif roznica > 0:
        return "Overpaid", roznica
    else:
        return "Underpaid", roznica