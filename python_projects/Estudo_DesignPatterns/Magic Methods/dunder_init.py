import random
#Python call __init__ upon object instantiation

class MyClass:
    def __init__(self):
        print('The __init__ method is running.')

class Dice:
    def __init__(self, sides=6):
        self.sides = sides

    def roll(self):
        return random.randint(1, self.sides)
if __name__ == '__main__':
    myclass = MyClass()

    die = Dice(sides=20)
    print(die.sides)
    print(die.roll())
