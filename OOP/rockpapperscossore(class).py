# Rock, Paper, Scissors game
# using magic methods (dunders)
#
# input "r" for rock, "p" for paper, or "s" for scissors

import random

ROCK = 'r'
PAPER = 'p'
SCISSORS = 's'
WIN="YOU WIN"
LOSE="YOU LOST"
TIE="Tie! are you ready for another game?"
    
class throw:
    def __init__(self, cont=None):
        if cont is None:
            self.cont = self.random()
        else:
            self.cont=cont
    def random(self):
        options = [ROCK, PAPER, SCISSORS]
        return options[random.randint(0,2)]
    def __gt__(self,other):
        beats = {
            PAPER: ROCK ,
            SCISSORS: PAPER,
            ROCK: SCISSORS
        }
        return other.cont == beats[self.cont]
    def __lt__(self,other):
        return other > self
    def name(self):
        pretty_name = {
            ROCK : "rock",
            PAPER : "paper",
            SCISSORS : "scissors"
        }
        return pretty_name[self.cont]

def match_result(your,other):
    if your > other:
        return WIN
    if your < other:
        return LOSE
    return TIE

print ("[r]=rock \n[p]=paper \n[s]=scissor")
a = input("Enter your pick: ")
print("")

check=[ROCK, PAPER, SCISSORS]

if a in check:
    you = throw(a)
    computer = throw()
    print("You selected : " + you.name())
    print("")
    print ("The computer selected :" + computer.name())
    print("")
    print(match_result(you, computer))

else:
    print("Invalid input")

