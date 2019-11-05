meno = input('Napis svoje priezvisko: ')

if meno[-3:] in ['ova', 'ová', 'ská', 'ska']:
    pohlavie = 'zenske'
else:
    pohlavie = 'muzske'

print(f'Podla mna si {pohlavie}ho pohlavia.'.format(pohlavie))
