from math import pi

a = int(input('Zadaj sirku elipsy v cm: '))
b = int(input('Zadaj vysku elipsy v cm: '))
c = int(input('Zadaj vysku valca v cm: '))

def obsah_elipsy(a,b):
    return round(pi * a * b, 2) # zaokruhlenie na 2 desatinne miesta

def objem_eliptickeho_valca(a, b, c):
    return obsah_elipsy(a, b) * c

print('Obsah elipsy je: ', obsah_elipsy(a, b), 'cm2.')
print('Objem eliptickeho valca je: ', objem_eliptickeho_valca(a, b, c), 'cm2.')