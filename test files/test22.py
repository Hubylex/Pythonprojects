class Player:
    def __init__(self, name, level):
        self.name = name
        self.level = level

    def intro(self):
        print(f'{self.name} (level {self.level})')

#your code goes here
a = input('enter player name')
b = input('enter level')
instance = Player(str(a),b)
instance.intro()