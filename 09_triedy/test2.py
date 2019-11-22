class Kitten:

    def __init__(self, name):
        self.name = name

    def __str__(self):
        

    def meow(self):
        print('{}: Meow!'.format(self.name))
        
    def eat(self, food):
        print('{}: Meow meow! I like {}.'.format(self.name, food))

mourek = Kitten('Mourek')

mourek.meow()
mourek.eat('fish')

