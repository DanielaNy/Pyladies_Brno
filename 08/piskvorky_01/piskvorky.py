from util import tah
from ai import tah_pocitaca

pole = '--------------------'
list_pole = list(pole)
cislo_policka = False
    
def tah_hraca(pole, cislo_policka):
    """funkcia, ktora si vypyta tah hraca, skontroluje ho a zavola funkciu 'tah'"""
    symbol = "X"
    list_pole = list(pole)
    while True:
        try:
            # cislo_policka = int(input('\nNa ktore policko chces umiestnit svoje \'X\'? Zadaj hodnotu 0 - 19: '))
            break
        except ValueError:
            print('Pozor! Musis zadat CISLO.')
            continue
    if cislo_policka in range(0, 20):
        if list_pole[cislo_policka] == "-":
            print('Ok. Policko je volne. Tvoj tah:')
            pole = tah(cislo_policka, symbol, pole)            
            return pole
        else:
            print('Pozor! Toto policko je uz obsadene.')
            return tah_hraca(pole, cislo_policka)
    else:
        print('Pozor! Toto policko neexistuje.')
        return tah_hraca(pole, cislo_policka)

def vyhodnot(pole):
    """funkcia vyhodnocujuca, ci hra skoncila"""
    if "OOO" in pole:
        print('O pocitac vyhral')
        return False
    elif "XXX" in pole:
        print('X vyhral/a si!')
        return False
    elif "-" not in pole:
        print("! remiza")
        return False
    else:
        print("- hra je aktivna")
        return 

def piskvorky(pole):
    """Spusta tahy hraca a pocitaca, vyhodnocuje po kazdom tahu hru"""

    print('Ahoj. Toto je hra 1D piskvorky. Pocitac hra so symbolmi \'O\', ty hras so symbolmi \'X\'.')   
    while "-" in pole:
        if vyhodnot(pole) == False:
            break
        else:
            pole = tah_hraca(pole, cislo_policka)
        if vyhodnot(pole) == False:
            break
        else:
            pole = tah_pocitaca(pole, cislo_policka)
    if "-" not in pole:
        vyhodnot(pole)
    return print("Dakujem za hru.")
