mountains_w_meters = {'Mount Everest' : '8848', 'K2' : '8611', 'Kangchenjunga' : '8586','Lhotse' : '8516','Makalu' : '8485'}
mountains_list_of_lists = []
mountains_w_meters_and_feet = {}

for k,v in mountains_w_meters.items():
    mountains_list_of_lists.append([k,v,round(int(v)*3.28)])
    
mountains_list_of_lists.sort()

for item in mountains_list_of_lists:
    mountains_w_meters_and_feet[item[0]] = [item[1], item[2]]
print()

for x in mountains_w_meters_and_feet:
    print(x)
print()

for y in mountains_w_meters_and_feet.values():
    print(y[0])
print()

for y in mountains_w_meters_and_feet.values():
    print(y[1])
print()

for x,y in mountains_w_meters_and_feet.items():
    print(f'{x} is {y[0]} meters or {y[1]} feet tall.'.format(x, y[0], y[1]))
