# Rules:
# There are 21 sticks.
# A player (computer or human) can pick up 1-4 sticks each turn.
# The aim is to not pick up the last stick; if you do, you lose.
# This doesn't validate user input being less than remaining sticks always.
from random import randrange

sticks = 21
max_pickup = 4

while True:
    print("Remaining sticks: ", sticks)
    sticks_taken = int(input("Select quantity (1-4) sticks to pick up: "))

    if sticks == 1:
        print("You lose! You picked up the last stick.")
        break
    if sticks_taken >= 5 or sticks_taken <= 0:
        print("Please enter a valid amount to pick up")
        continue

    sticks -= sticks_taken
    print("There are %s sticks remaining." % sticks)

    if sticks == 1:
        print("You left 1 stick: the computer loses, and you've won!")
        break
    elif sticks < 4:
        max_pickup = sticks

    print("Now it's the computer's turn: ")
    computer_choice = randrange(1, (max_pickup + 1))
    print("The computer took: ", computer_choice)
    sticks -= computer_choice
    if sticks == 0:
        print("Oops! The computer just lost - you've won!")
        break
