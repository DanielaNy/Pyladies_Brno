from random import randint
pole = 'a-----'
list_pole = list(pole)

symbol = "O"
cislo_policka = randint(0,20)
print(type(cislo_policka))
print(cislo_policka)
#cislo_policka = randint(0,20)
if cislo_policka in range(0, 6): 
    if list_pole[cislo_policka] == "-":
        print(f"Pocitac si vybral policko: {cislo_policka}.".format(cislo_policka))  

    else:
        print('else')

 
