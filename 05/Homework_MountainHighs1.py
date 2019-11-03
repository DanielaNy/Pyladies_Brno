mountains = {'Mount Everest' : '8,848', 'K2' : '8,611', 'Kangchenjunga' : '8,586','Lhotse' : '8,516','Makalu' : '8,485'}
mountains
for k in mountains:
    print(k)
print()
for v in mountains.values():
    print(v)
print()
for k,v in mountains.items():
    print(f'{k} is {v} meters tall.'.format(k, v))


