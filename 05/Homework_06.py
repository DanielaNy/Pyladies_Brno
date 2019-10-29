pets = ['pes', 'kocka', 'kralik', 'had', 'andulka']
pets2 = []
pets3 = []
pets4 = []

for pet in pets:
    pets2.append(pet[1])
    pets3.append((pet[1], pet))
    continue

pets2.sort()
dictionary = dict(pets3)

for x in pets2:
    if x in dictionary:
        pets4.append(dictionary[x])
        continue

print(pets4)
