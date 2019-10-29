zaznamy = ['pepa novak', 'Jiri Sladek', 'Ivo navratil', 'jan Polednik']

nespravne_zaznamy = []
for meno in zaznamy:    
    meno1 = meno.split(' ')
    for i in meno1:
        if i[0].islower() == True:
            nespravne_zaznamy.append(meno1)
        else:
            pass

print(nespravne_zaznamy)
