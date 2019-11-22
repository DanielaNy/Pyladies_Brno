from random import randint, choice
pole = '--------------------'
list_pole = list(pole)
cislo_policka = False
print(pole)
mozne_policka1 = []
mozne_policka2 = []

def tah(pole, cislo_policka, symbol):
    """funkcia vracajuca pole podla tahu hraca/pocitaca"""
    list_pole[cislo_policka] = symbol    
    pole = "".join(list_pole)
    print(pole)
    return pole
    
def tah_hraca(pole, cislo_policka):
    """funkcia, ktora si vypyta tah hraca, skontroluje ho a zavola funkciu 'tah'"""
    symbol = "X"
    list_pole = list(pole)
    while True:
        try:
            cislo_policka = int(input('\nNa ktore policko chces umiestnit svoje \'X\'? Zadaj hodnotu 0 - 19: '))
            break
        except ValueError:
            print('Pozor! Musis zadat CISLO.')
            continue
    if cislo_policka in range(0, 20):
        if list_pole[cislo_policka] == "-":
            print('Ok. Policko je volne. Tvoj tah:')
            pole = tah(pole, cislo_policka, symbol)            
            return pole
        else:
            print('Pozor! Toto policko je uz obsadene.')
            return tah_hraca(pole, cislo_policka)
    else:
        print('Pozor! Toto policko neexistuje.')
        return tah_hraca(pole, cislo_policka)


def strategia_pocitaca(pole):
    """vrati cislo_policka s prioritou pre vyhru"""
    dict_pole = dict(enumerate(list_pole))
    cislo_policka = False

    for k, v in dict_pole.items():
        print(type(k), v)
        k1_idx = int(k)
        k2_idx = False
        k3_idx = False
        k0_idx = False
        if v == "O":
            print("O found")
            k1_idx = int(k)
            k2_idx = k + 1
            k3_idx = k + 2
            k0_idx = k - 1
            if k <=18:
                if dict_pole[k2_idx] == "O" and dict_pole[k3_idx] == "-":
                    if k3_idx not in mozne_policka1:
                        mozne_policka1.append(k3_idx)
                    
                elif dict_pole[k3_idx] == "O" and dict_pole[k2_idx] == "-":
                    if k2_idx not in mozne_policka1:
                        mozne_policka1.append(k2_idx)

                elif dict_pole[k2_idx] == "-":
                    if k2_idx not in mozne_policka2:
                        mozne_policka2.append(k2_idx)

                elif dict_pole[k3_idx] == "-":
                    if k3_idx not in mozne_policka2:
                        mozne_policka2.append(k3_idx)

                elif dict_pole[k0_idx] == "-":
                    if k0_idx not in mozne_policka2:
                        mozne_policka2.append(k0_idx)

                else:           
                    cislo_policka = randint(0,19)
            else:
                cislo_policka = False
    print(cislo_policka, mozne_policka1, mozne_policka2)
    for x in range(0, 20):
        try:
            mozne_policka1.remove(20)
            mozne_policka1.remove(21)
            mozne_policka2.remove(20)
            mozne_policka2.remove(21)
        except:
            ValueError
    return cislo_policka, mozne_policka1, mozne_policka2
        
                
def tah_pocitaca(pole, cislo_policka, mozne_policka1, mozne_policka2):
    """funkcia, ktora vygeneruje tah pocitaca, zavola funkciu 'tah'"""
    symbol = "O"
    strategia_pocitaca(pole)
    if mozne_policka1:
        cislo_policka = choice(mozne_policka1)
    elif mozne_policka2:
        cislo_policka = choice(mozne_policka2)
    else:
        cislo_policka = cislo_policka
        
    if cislo_policka == False:
        cislo_policka = randint(0,20)
        return tah_pocitaca(pole, cislo_policka, mozne_policka1, mozne_policka2)
    elif list_pole[cislo_policka] == "-":
        print(f"\nPocitac si vybral policko: {cislo_policka}. Tah pocitaca:")
        pole = tah(pole, cislo_policka, symbol)    
        return pole
    else:
        return tah_pocitaca(pole, cislo_policka, mozne_policka1, mozne_policka2)

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
            pole = tah_pocitaca(pole, cislo_policka, mozne_policka1, mozne_policka2)
    if "-" not in pole:
        vyhodnot(pole)
    return print("Dakujem za hru.")

piskvorky(pole)
