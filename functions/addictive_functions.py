import sys

# Funkcja do powtorzenia programu
def spoboj_ponownie(tekst, funkcja):
    print(tekst)
    wybor = input().upper()

    if wybor == "TAK" or wybor == "YES":
        funkcja()
    elif wybor == "":
        spoboj_ponownie(tekst, funkcja)
    else:
        sys.exit()
