# MÓDULO - DICES
from random import randint


class Dice:
    def __init__(self,name:str = 'dice', faces: int = 6):
        self.name = name
        self.faces = faces

    def roll(self):
        '''
        This method simulates rolling a dice.
        '''
        print(f'Você rolou um {self.name}.')
        result = randint(1, self.faces)
        print(f'O resultado é {result}.')
        return result

d4 = Dice('d4', 4)
d6 = Dice('d6', 6)
d8 = Dice('d8', 8)
d10 = Dice('d10', 10)
d12 = Dice('d12', 12)
d20 = Dice('d20', 20)
d100 = Dice('d100', 100)


class Coin:
    Head = '"cara"'
    Tail = '"coroa"'
    def __init__(self, name:str = 'coin'):
        self.name = name

    def flip(self):
        '''
        This method simulates flipping a coin. Being able to get 'heads' or 'tails' as a result.
        '''
        print(f'Você jogou uma {self.name}.')
        result = randint(0, 1)
        if result == 0:
            face = self.Head
        else:
            face = self.Tail
        print(f'O resultado é {face}.')
        return face

moeda = Coin('moeda')


if __name__ == '__main__':

    d100.roll()
    moeda.flip()
