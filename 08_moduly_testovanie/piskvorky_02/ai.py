from random import randint
from util import tah

def tah_pocitaca(pole, symbol="O"):
    """funkcia, ktora vygeneruje tah pocitaca, zavola funkciu 'tah'"""
    cislo_policka = randint(0,len(pole)-1)
    list_pole = list(pole)
    if list_pole[cislo_policka] == "-":
        print(f"\nPocitac si vybral policko: {cislo_policka}. Tah pocitaca:")
        pole = tah(cislo_policka, symbol, pole)    
        return pole
    else:
        return tah_pocitaca(pole, symbol="O")
