animals = {"ziggy" : "canary", "Py" : "snake", "Tom" : "dog", "Jerry" : "mouse", "dorry" : "fish"}

for k, v in animals.items():
    print(f'{k.capitalize()} is a {v}.'.format(k, v))

def animal_printing(a):
    print('\nPrint from the function:')
    for k, v in a.items():
        print(f'{k.capitalize()} is a {v}.'.format(k, v))

animal_printing(animals)