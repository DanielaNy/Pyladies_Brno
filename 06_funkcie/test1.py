from math import pi

a = int(input('Zadaj sirku elipsy v cm: '))
b = int(input('Zadaj vysku elipsy v cm: '))

def obsah_elipsy(a,b):
    return round(pi * a * b, 2) # zaokruhlenie na 2 desatinne miesta

print('Obsah elipsy je: ', obsah_elipsy(a, b), 'cm2.')