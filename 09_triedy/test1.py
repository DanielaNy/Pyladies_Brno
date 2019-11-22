class Kitten:
    def meow(self):
        print('Meow!')

kitten = Kitten()           # vytvoreny objekt kitten triedy Kitten
kitten.meow()

mourek = Kitten()
mourek.name = 'Mourek'      # vytvoreny atribut name

micka = Kitten()
micka.name = 'Micka'        # vytvoreny atribut name

print(mourek.name)
print(micka.name)