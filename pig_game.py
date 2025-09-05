import random

def roll():
    min_number = 1
    max_number = 6
    rolls = random.randint(min_number, max_number)
    return rolls

while True:
    players = input("Enter the number of player (2 - 4 ): ")
    if  players.isdigit(): # is check digit number
        players = int(players) # change str to int
        if 2 <= players <= 4:
            break
        else:
            print("Must be between 2 - 4 players")
    else:
        print("Invalid , try again")

max_score = 50
player_score = [0 for _ in range(players)]

