mountains = {'Mount Everest' : {'elevation':'8848', 'range':'Himalayas'}, 'K2' : {'elevation':'8611', 'range':'Karakoram'}, 'Kangchenjunga' : {'elevation':'8586', 'range':'Himalayas'},'Lhotse' : {'elevation':'8516', 'range':'Himalayas'},'Makalu' : {'elevation':'8485', 'range':'Himalayas'}}
for mountain_name in mountains:
    print(mountain_name)
print()

for mountain_elevation in mountains.values():
    print(mountain_elevation['elevation'])
print()

for mountain_elevation in mountains.values():
    print(mountain_elevation['range'])
print()

for mountain_name, mountain_properties in mountains.items():
    print(f"{mountain_name} is an {mountain_properties['elevation']}-meter tall mountain in the {mountain_properties['range']}.".format(mountain_name, mountain_properties['elevation'], mountain_properties['range']))