from util import tah
from ai import tah_pocitaca

pole = '--------------------'
list_pole = list(pole)
str_policka = None

def input_cislo_policka():
    """Funkcia, ktora si od hraca vypita cislo policka"""
    str_policka = input('\nNa ktore policko chces umiestnit svoje \'X\'? Zadaj hodnotu 0 - 19: ')
    return str_policka

def tah_hraca(pole, str_policka):
    """funkcia, ktora skontroluje input hraca a zavola funkciu 'tah'"""
    symbol = "X"
    list_pole = list(pole)
    if str_policka == None:
        str_policka = input_cislo_policka()
    while True:
        try:
            cislo_policka = int(str_policka)
            break
        except ValueError:
            print('Pozor! Musis zadat CISLO.')
            continue
    print(cislo_policka)
    if cislo_policka in range(0, 20):
        if list_pole[cislo_policka] == "-":
            print('Ok. Policko je volne. Tvoj tah:')
            pole = tah(cislo_policka, symbol, pole)            
            return pole
        else:
            print('Pozor! Toto policko je uz obsadene.')
            return tah_hraca(pole, str_policka)
    else:
        print('Pozor! Toto policko neexistuje.')
        return tah_hraca(pole, str_policka)

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
            pole = tah_hraca(pole, str_policka)
        if vyhodnot(pole) == False:
            break
        else:
            pole = tah_pocitaca(pole, symbol="O")
    if "-" not in pole:
        vyhodnot(pole)
    return print("Dakujem za hru.")
