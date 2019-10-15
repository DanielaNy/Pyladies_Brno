# pravda = 1 < 3
# print(pravda)


strana = float(input("zadaj cislo v cm: "))
obvod = 4*strana
obsah = strana*strana

cislo_je_spravne = strana>0

if cislo_je_spravne == True:
    print(f"Obvod stvorca so stranou {strana} cm je {obvod} cm.".format(strana, obvod))
    print(f"Obsah stvorca so stranou {strana} cm je {obsah} cm2.".format(strana, obsah))
else:
    print("Cislo je chybne.")