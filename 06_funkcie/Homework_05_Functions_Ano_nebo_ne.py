print('Odpovídej "ano" nebo "ne".')

def anonebone(stastna_retezec, bohata_retezec):
    "hra Jsi stastna"
    if stastna_retezec.lower() in ["ano", "a", " ano", "ano ", " ano "]:
        stastna = True
        if bohata_retezec.lower() in ["ano", "a", " ano", "ano ", " ano "]:
            bohata = True
        else:
            bohata = False
    else:
        stastna = False
        if bohata_retezec.lower() in ["ano", "a", " ano", "ano ", " ano "]:
            bohata = True
        else:
            bohata = False

    if bohata:
        if stastna:
            print('Gratuluji!')
        else:
            print('Zkus se víc usmívat.')
    elif stastna:
        print('Zkus míň utrácet.')
    else:
        print('To je mi líto.')
        
stastna_retezec = input('Jsi šťastná? ')
bohata_retezec = input('Jsi bohatá? ')

if stastna_retezec.lower() in ["ano", "a", " ano", "ano ", " ano ", "ne", "n", " ne", "ne ", " ne "] and bohata_retezec.lower() in ["ano", "a", " ano", "ano ", " ano ", "ne", "n", " ne", "ne ", " ne "]:
    anonebone(stastna_retezec, bohata_retezec)
else:
    print('Nerozumím!')
