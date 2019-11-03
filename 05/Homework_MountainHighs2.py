mountains = {'Mount Everest' : '8,848', 'K2' : '8,611', 'Kangchenjunga' : '8,586','Lhotse' : '8,516','Makalu' : '8,485'}
mountains_list_of_lists = []

for k,v in mountains.items():
    mountains_list_of_lists.append([k,v])
    
mountains_list_of_lists.sort()

for item in mountains_list_of_lists:
    print(f'{item[0]} is {item[1]} meters tall.'.format(item[0], item[1]))
