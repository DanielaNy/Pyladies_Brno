from random import randrange

hraci = []

for hrac in [1, 2, 3]:
    hod = True
    hody = []
    while hod != 6:
        hod = randrange(1,7)
        hody.append(hod)
        continue
    pocet_hodov = len(hody)
    hraci.append(([pocet_hodov, str(hrac), hody]))

hraci_sorted = list(hraci)
hraci_sorted.sort(reverse = True)

print(f'Vyhral hrac c. {hraci_sorted[0][1]}.'.format(hraci_sorted[0][1]))

for i in hraci:
    print(f'Hrac c.{i[1]} hadzal {i[0]}-krat. Hody: {i[2]}.'.format(i[1], i[0], i[2])) 
