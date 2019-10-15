# komentar / tento program pocita obvod a obsah stvorca v cm
strana = int(input("zadaj cislo: "))


obvod = 4*strana
obsah = strana*strana
print ("Obvod stvorca so stranou", strana,  "cm je", strana * 4,  "cm.")


print(f"Obvod stvorca so stranou {strana} cm je {obvod} cm.".format(strana, obvod))
print(f"Obsah stvorca so stranou {strana} cm je {obsah} cm2.".format(strana, obsah))