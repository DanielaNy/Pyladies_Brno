animals = {"ziggy" : "canary", "Py" : "snake", "Tom" : "cat", "Jerry" : "mouse"}

for k, v in animals.items():
    print(f'{k.capitalize()} is a {v}.'.format(k, v))