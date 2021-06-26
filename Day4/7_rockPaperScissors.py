import random, rpsModule

print("Rock Paper Scissors Game")
print("""
    01 : Rock
    02 : Paper
    03 : Scissors
""")

inputGiven = int(input("Enter a number : "))
print("Your choice")
if inputGiven == 1:
    print(rpsModule.Rock)
elif inputGiven == 2:
    print(rpsModule.Paper)
elif inputGiven == 3:
    print(rpsModule.Scissors)
else:
    print("invalid Input")
    print("You Lose")
    SystemExit(-1)

inputOpponent = random.randint(1,3)
print("Computer's choice")
if inputOpponent == 1:
    print(rpsModule.Rock)
elif inputOpponent == 2:
    print(rpsModule.Paper)
elif inputOpponent == 3:
    print(rpsModule.Scissors)

states = [[1,2,3], [3,1,2], [2,3,1]]
stateChosen = states[inputGiven-1][inputOpponent-1]

if stateChosen == 1:
    print("Draw")
elif stateChosen == 2:
    print("You Loose")
else:
    print("You won")
