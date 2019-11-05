import random
import sys

tah_cloveka = True
knp  = ['kamen', 'nuzky', 'papir']

def knp_hra(tah_cloveka):
    "hra kamen, nuzky, papir"    
    tah_cloveka = input('\nZvol 1 z moznosti (bez diakritiky): kamen, nuzky, nebo papir? \nPre ukoncenie, zadaj \'konec\'\n\nTvoja volba: ')
    if tah_cloveka in ['kamen', 'nuzky', 'papir']:
        tah_pocitace = random.choice(knp)
        print(f'\nPocitac si zvolil {tah_pocitace}.'.format(tah_pocitace))
        if tah_cloveka == 'kamen' and tah_pocitace == 'kamen' or tah_cloveka == 'nuzky' and tah_pocitace == 'nuzky' or tah_cloveka == 'papir' and tah_pocitace == 'papir':
            print('Plichta.')
            knp_hra(tah_cloveka)
        elif tah_cloveka == 'kamen' and tah_pocitace == 'nuzky' or tah_cloveka == 'nuzky' and tah_pocitace == 'papir' or tah_cloveka == 'papir' and tah_pocitace == 'kamen':
            print('Vyhrál jsi!')
            knp_hra(tah_cloveka)
        else:
            print('Počítač vyhrál.')
            knp_hra(tah_cloveka)
    elif tah_cloveka == 'konec':
        sys.exit("Diky za hru. Pekny den!")
    else:
        print('Tve volbe nerozumím.')
        knp_hra(tah_cloveka)

knp_hra(tah_cloveka)
