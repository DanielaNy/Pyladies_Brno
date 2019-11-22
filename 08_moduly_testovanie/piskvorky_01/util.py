
def tah(cislo_policka, symbol, pole):
    """funkcia vracajuca pole podla tahu hraca/pocitaca"""
    list_pole = list(pole)
    list_pole[cislo_policka] = symbol    
    pole = "".join(list_pole)
    print(pole)
    return pole
