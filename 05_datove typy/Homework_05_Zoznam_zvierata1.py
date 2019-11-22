pets = ['pes', 'kocka', 'kralik', 'had']
wild_animals = ['tiger', 'slon', 'zirafa', 'panda', 'had']
cisla = [1, 2, 4, 3]
pismena = ["a", "b", "d", "c"]

# 1
for zviera in pets:
    if len(zviera) > 5:
        print(zviera)
    
# 2
for zviera in pets:
    if zviera[0] == 'k':
        print(zviera)

# 3
print('Je toto zviera v zozname? ')
zadane_zviera = input('Zadaj zviera: ')
for zviera in pets:    
    if zviera == zadane_zviera:
        a = True
        break
    else:
        a = False
        continue
print(a)

# 4
choice = input("""Ktory zoznam zierat chces vidiet? [zadaj: a / b / c ] 
\na: Domace a divoke zvierata
\nb: Iba domace zvierata
\nc: Iba divoke zvierata
\n Tvoja volba: """)

pets2 = list(pets)
wild_animals2 = list(wild_animals)
if choice == "a":
    print(pets + wild_animals)
elif choice == "b":
    for pet in pets:
        if pet in wild_animals:
            pets2.remove(pet)
            continue
        else:
            continue
    print(pets2)

elif choice == "c":
    for pet in wild_animals:
        if pet in pets:
            wild_animals2.remove(pet)
            continue
        else:
            continue
    print(wild_animals2)

else:
    print('Takato volba neexistuje.')

# 5
pets3 = list(pets)
pets3.sort()
print(pets3)
