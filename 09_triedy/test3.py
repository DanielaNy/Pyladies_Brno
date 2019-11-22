class Kitten:

    def __init__(self, name):
        self.name = name
        self.life = 9

    def meow(self):
        print('{}: Meow!'.format(self.name))

    def lose_life(self):
        if self.is_alive():        
            self.life = self.life -1
        else:
            print("Mrtvu macku uz nezabijes.")

    def is_alive(self):
        return False if self.life == 0 else True        # ternarny operator

        # return not bool(self.life == 0)

        # if self.life == 0:
        #     print("{} bohuzel zemrela.".format(self.name))
        #     return False
        # else:
        #      return True


    def eat(self, food):
        print('{}: Meow meow! I like {}.'.format(self.name, food))
        if food == "fish":
            if self.is_alive() and self.life < 9:
                self.life = self.life +1



mourek = Kitten('Mourek')
mourek.meow()
mourek.eat('fish')
print(mourek.life)
mourek.lose_life()
print(mourek.life)
mourek.eat('fish')
print(mourek.life)
mourek.lose_life()
mourek.eat('mouse')
print(mourek.life)
mourek.eat('mouse')
print(mourek.life)
